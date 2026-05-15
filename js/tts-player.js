/**
 * tts-player.js — 李录研究网站文章语音播报 v2
 * 改进：自然语调、句子间停顿、高质量语音选择
 * 依赖: 浏览器原生 Web Speech API，无需后端
 */
(function () {
  'use strict';

  // ── 检测是否支持 Web Speech API ──────────────────────────────
  if (!window.SpeechSynthesisUtterance) {
    console.warn('[TTS] 当前浏览器不支持 Web Speech API，请使用 Chrome/Edge/Safari');
    return;
  }

  // ── 状态 ────────────────────────────────────────────────────
  var isPlaying = false;
  var isPaused  = false;
  var utterance = null;
  var queue     = [];
  var currentIdx = 0;

  // ── 语音质量排序函数 ─────────────────────────────────────────
  function getBestVoice() {
    var voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return null;

    // 优先顺序：
    // 1. zh-CN 本地语音（质量最高）
    // 2. zh-CN 云端语音（质量高）
    // 3. zh 通用
    // 4. 任何中文
    var preferred = voices.filter(function (v) { return v.lang === 'zh-CN' && v.localService; });
    if (preferred.length > 0) return preferred[0];

    preferred = voices.filter(function (v) { return v.lang === 'zh-CN'; });
    if (preferred.length > 0) return preferred[0];

    preferred = voices.filter(function (v) { return v.lang.startsWith('zh'); });
    if (preferred.length > 0) return preferred[0];

    return voices[0];
  }

  // ── 等待语音列表加载 ─────────────────────────────────────────
  function waitForVoices(callback) {
    var voices = window.speechSynthesis.getVoices();
    if (voices && voices.length > 0) {
      callback(getBestVoice());
    } else {
      window.speechSynthesis.onvoiceschanged = function () {
        callback(getBestVoice());
      };
    }
  }

  // ── 创建 TTS 按钮 ───────────────────────────────────────────
  function createButton() {
    var btn = document.createElement('button');
    btn.id = 'tts-toggle-btn';
    btn.setAttribute('aria-label', '文章语音播报');
    btn.title = '点击播放文章内容（需要浏览器支持语音，推荐使用 Chrome】';
    updateButtonUI(btn, 'idle');
    btn.addEventListener('click', handleToggle);
    return btn;
  }

  // ── 更新按钮 UI ─────────────────────────────────────────────
  function updateButtonUI(btn, state) {
    if (!btn) return;
    var labels = {
      idle:    '🔊 朗读',
      playing: '⏸ 暂停',
      paused:  '▶ 继续',
      done:    '✅ 播完'
    };
    btn.textContent = labels[state] || '🔊 朗读';
    btn.className = 'tts-btn tts-' + state;
  }

  // ── 从文章提取正文段落 ──────────────────────────────────────
  function extractTextNodes() {
    var main = document.querySelector('.main-content') ||
               document.querySelector('main') ||
               document.querySelector('article') ||
               document.body;
    var nodes = [];
    var walk = document.createTreeWalker(main, NodeFilter.SHOW_TEXT, null, false);
    var t;
    while ((t = walk.nextNode())) {
      var text = t.textContent.trim();
      // 跳过太短的、纯数字的、导航/页脚中的文字
      if (text.length < 20) continue;
      if (/^\d+$/.test(text)) continue;
      if (t.parentElement) {
        var tag = t.parentElement.tagName.toLowerCase();
        if (['script', 'style', 'nav', 'footer', 'header', 'meta', 'noscript'].indexOf(tag) !== -1) continue;
        // 跳过导航链接和脚注
        if (t.parentElement.closest('nav, footer, header, .sub-nav, .page-footer, .nav-links')) continue;
      }
      // 清理多余空白
      text = text.replace(/\s+/g, ' ');
      nodes.push(text);
    }
    return nodes;
  }

  // ── 改进的分段朗读（按句子，保留标点停顿） ──────────────────
  function splitIntoSentences(text, maxLen) {
    maxLen = maxLen || 150; // 缩短单段长度，便于浏览器语音引擎处理

    // 中文标点分割（句号、感叹号、问号、逗号、分号）
    // 分割后保留标点
    var sentences = text.split(/(?<=[。！？；，、])/g).filter(function (s) {
      return s.trim().length > 0;
    });

    var chunks = [];
    var current = '';

    for (var i = 0; i < sentences.length; i++) {
      var s = sentences[i].trim();
      if (!s) continue;

      // 如果单句就超过 maxLen，继续细分
      if (s.length > maxLen) {
        if (current) {
          chunks.push(current);
          current = '';
        }
        // 按子句继续分割
        var subChunks = splitLongSentence(s, maxLen);
        for (var j = 0; j < subChunks.length; j++) {
          chunks.push(subChunks[j]);
        }
      } else if (current.length + s.length <= maxLen) {
        current += s;
      } else {
        if (current) chunks.push(current);
        current = s;
      }
    }
    if (current) chunks.push(current);
    return chunks.length > 0 ? chunks : [text.substring(0, maxLen)];
  }

  // ── 长句细分（用于超长单句） ────────────────────────────────
  function splitLongSentence(text, maxLen) {
    var chunks = [];
    // 按顿号、逗号继续分割
    var parts = text.split(/(?<=[、，])/g).filter(function (s) { return s.trim().length > 0; });
    var current = '';

    for (var i = 0; i < parts.length; i++) {
      var p = parts[i].trim();
      if (!p) continue;
      if (current.length + p.length <= maxLen) {
        current += p;
      } else {
        if (current) chunks.push(current);
        current = p;
      }
    }
    if (current) chunks.push(current);
    return chunks.length > 0 ? chunks : [text.substring(0, maxLen)];
  }

  // ── 朗读队列 ────────────────────────────────────────────────
  function buildQueue() {
    if (queue.length > 0) return;
    var texts = extractTextNodes();
    texts.forEach(function (para) {
      splitIntoSentences(para).forEach(function (chunk) {
        queue.push(chunk);
      });
    });
  }

  // ── 播放下一段 ──────────────────────────────────────────────
  function playNext(bestVoice) {
    if (currentIdx >= queue.length) {
      finishPlaying();
      return;
    }
    var text = queue[currentIdx];

    utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'zh-CN';
    utterance.voice = bestVoice;

    // 语速：0.85（稍慢，便于跟上理论内容）
    utterance.rate = 0.85;
    // 语调：0.95（略低，增加自然感）
    utterance.pitch = 0.95;
    // 音量：0.9
    utterance.volume = 0.9;

    utterance.onend = function () {
      currentIdx++;
      // 段与段之间短暂停顿（100ms）
      setTimeout(function () {
        playNext(bestVoice);
      }, 100);
    };
    utterance.onerror = function (e) {
      // 网络或语音不可用时，跳过继续
      if (e.error !== 'interrupted' && e.error !== 'canceled') {
        currentIdx++;
      } else {
        currentIdx++;
      }
      playNext(bestVoice);
    };

    window.speechSynthesis.speak(utterance);
  }

  function startPlaying() {
    waitForVoices(function (bestVoice) {
      if (!bestVoice) {
        alert('未找到中文语音，请使用 Chrome 或 Edge 浏览器。');
        return;
      }
      queue = [];
      currentIdx = 0;
      buildQueue();
      if (queue.length === 0) {
        alert('无法提取文章内容，或文章内容过短。');
        return;
      }
      isPlaying = true;
      isPaused  = false;
      var btn = document.getElementById('tts-toggle-btn');
      updateButtonUI(btn, 'playing');
      playNext(bestVoice);
    });
  }

  function pausePlaying() {
    window.speechSynthesis.pause();
    isPaused = true;
    isPlaying = false;
    var btn = document.getElementById('tts-toggle-btn');
    updateButtonUI(btn, 'paused');
  }

  function resumePlaying() {
    window.speechSynthesis.resume();
    isPaused = false;
    isPlaying = true;
    var btn = document.getElementById('tts-toggle-btn');
    updateButtonUI(btn, 'playing');
  }

  function stopPlaying() {
    window.speechSynthesis.cancel();
    isPlaying = false;
    isPaused  = false;
    queue     = [];
    currentIdx = 0;
    var btn = document.getElementById('tts-toggle-btn');
    updateButtonUI(btn, 'idle');
  }

  function finishPlaying() {
    isPlaying = false;
    isPaused  = false;
    var btn = document.getElementById('tts-toggle-btn');
    if (btn) updateButtonUI(btn, 'done');
    setTimeout(function () {
      stopPlaying();
    }, 2000);
  }

  // ── 主切换逻辑 ──────────────────────────────────────────────
  function handleToggle() {
    if (isPlaying) {
      pausePlaying();
    } else if (isPaused) {
      resumePlaying();
    } else {
      startPlaying();
    }
  }

  // ── 初始化 ───────────────────────────────────────────────────
  function init() {
    var hero = document.querySelector('.hero');
    var insertTarget = hero || document.querySelector('.main-content') || document.body;
    var btn = createButton();

    if (hero) {
      var subtitle = hero.querySelector('.subtitle');
      if (subtitle) {
        subtitle.insertAdjacentElement('afterend', btn);
      } else {
        hero.appendChild(btn);
      }
    } else {
      insertTarget.insertBefore(btn, insertTarget.firstChild);
    }
  }

  document.addEventListener('DOMContentLoaded', init);

})();
