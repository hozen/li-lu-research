/**
 * tts-player.js — 李录研究网站文章语音播报
 * 使用浏览器原生 Web Speech API，无需后端
 * 依赖: 无外部库
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
  var queue     = [];     // 待朗读的段落队列
  var currentIdx = 0;

  // ── 创建 TTS 按钮 ───────────────────────────────────────────
  function createButton() {
    var btn = document.createElement('button');
    btn.id = 'tts-toggle-btn';
    btn.setAttribute('aria-label', '文章语音播报');
    btn.title = '点击播放文章内容（需要浏览器支持语音）';
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

  // ── 分段朗读（避免超长文本） ─────────────────────────────────
  function splitIntoChunks(text, maxLen) {
    maxLen = maxLen || 200;
    // 按句子分割（中文句号/感叹号/问号）
    var sentences = text.split(/(?<=[。！？；\.\!\?])/g).filter(function (s) { return s.trim().length > 0; });
    var chunks = [];
    var current = '';
    for (var i = 0; i < sentences.length; i++) {
      var s = sentences[i].trim();
      if (current.length + s.length <= maxLen) {
        current += s;
      } else {
        if (current) chunks.push(current);
        current = s;
      }
    }
    if (current) chunks.push(current);
    return chunks.length > 0 ? chunks : [text.substring(0, maxLen)];
  }

  // ── 朗读队列 ────────────────────────────────────────────────
  function buildQueue() {
    if (queue.length > 0) return; // 已有则不复建
    var texts = extractTextNodes();
    texts.forEach(function (para) {
      splitIntoChunks(para).forEach(function (chunk) {
        queue.push(chunk);
      });
    });
  }

  function playNext() {
    if (currentIdx >= queue.length) {
      finishPlaying();
      return;
    }
    var text = queue[currentIdx];
    utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'zh-CN';
    utterance.rate = 1.0;
    utterance.pitch = 1.0;

    utterance.onend = function () {
      currentIdx++;
      playNext();
    };
    utterance.onerror = function (e) {
      // 网络或语音不可用时，跳过继续
      if (e.error !== 'interrupted') {
        currentIdx++;
      }
      playNext();
    };

    window.speechSynthesis.speak(utterance);
  }

  function startPlaying() {
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
    playNext();
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
    // 找到插入按钮的位置：hero 区域的合适位置
    var hero = document.querySelector('.hero');
    var insertTarget = hero || document.querySelector('.main-content') || document.body;
    var btn = createButton();

    if (hero) {
      // 放在 hero 底部（subtitle 之后）
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
