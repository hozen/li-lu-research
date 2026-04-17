/* ===================================================================
   main.js — 李录研究网站共享 JavaScript
   包含: drawer 开关、主题切换、back-to-top、自动暗模式、搜索
   =================================================================== */

(function () {
  'use strict';

  /* ── 0. 自动暗模式（跟随系统偏好） ─────────────────────────── */
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.body.classList.add('dark-mode');
  }

  /* ── 1. Drawer 开关 ─────────────────────────────────────────── */
  function initDrawer() {
    var hamBtn     = document.getElementById('uniHamBtn');
    var overlay    = document.getElementById('uniOverlay');
    var drawer     = document.getElementById('uni-drawer');
    var drawerClose = document.getElementById('uniDrawerClose');

    if (hamBtn) {
      hamBtn.onclick = function () {
        overlay && overlay.classList.add('open');
        drawer  && drawer.classList.add('open');
      };
    }
    if (overlay) {
      overlay.onclick = function () {
        overlay.classList.remove('open');
        drawer && drawer.classList.remove('open');
      };
    }
    if (drawerClose) {
      drawerClose.onclick = function () {
        overlay && overlay.classList.remove('open');
        drawer && drawer.classList.remove('open');
      };
    }
  }

  /* ── 2. 主题切换 ────────────────────────────────────────────── */
  function initTheme() {
    var navBtn   = document.getElementById('uniThemeBtn');
    var drawerBtn = document.getElementById('uniDrawerThemeBtn');

    function toggle() {
      var isDark = document.body.classList.toggle('dark-mode');
      if (navBtn) {
        navBtn.innerHTML = isDark ? '&#9788; 亮色' : '&#9790; 暗色';
      }
    }

    if (navBtn)    navBtn.onclick    = toggle;
    if (drawerBtn) drawerBtn.onclick = toggle;
  }

  /* ── 3. Back-to-top ─────────────────────────────────────────── */
  function initBackToTop() {
    var btn = document.getElementById('backToTop');
    if (!btn) return;
    window.addEventListener('scroll', function () {
      btn.style.display = window.scrollY > 300 ? 'flex' : 'none';
    }, { passive: true });
    btn.onclick = function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    };
  }

  /* ── 4. 搜索功能 ────────────────────────────────────────────── */
  function initSearch() {
    var input = document.getElementById('searchInput');
    if (!input) return;
    input.addEventListener('keyup', function () {
      var filter = input.value.toUpperCase();
      var sections = document.querySelectorAll('section,.card,.quote-card,.book-card,.video-card,.principle-card,.lesson-card');
      sections.forEach(function (s) {
        var text = s.textContent || s.innerText;
        s.style.display = (filter === '' || text.toUpperCase().indexOf(filter) > -1) ? '' : 'none';
      });
    });
  }

  /* ── 5. 资料库下拉菜单点击切换 (5-R2-1) ─────────────────── */
  function initDropdown() {
    var drops = document.querySelectorAll('.uni-dropdown > .uni-link');
    drops.forEach(function (link) {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        var menu = link.nextElementSibling;
        if (!menu) return;
        var isOpen = menu.style.display === 'block';
        // close all
        document.querySelectorAll('.uni-dropdown-menu').forEach(function (m) { m.style.display = ''; });
        if (!isOpen) menu.style.display = 'block';
      });
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.uni-dropdown')) {
        document.querySelectorAll('.uni-dropdown-menu').forEach(function (m) { m.style.display = ''; });
      }
    });
    // highlight active page link
    var path = location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.uni-links a, .uni-dropdown-menu a').forEach(function (a) {
      var href = a.getAttribute('href');
      if (href === path || (path === '' && href === 'index.html')) {
        a.style.color = '#c9a227';
        a.style.fontWeight = '600';
      }
    });
  }

  /* ── 6. 移动端旧式 hamburger（兼容） ───────────────────────── */
  function initLegacyMenu() {
    var btn = document.getElementById('mobileMenuBtn');
    if (!btn) return;
    btn.onclick = function () {
      var overlay = document.getElementById('mobileOverlay');
      var drawer  = document.getElementById('mobileDrawer');
      if (overlay) overlay.classList.toggle('open');
      if (drawer)  drawer.classList.toggle('open');
    };
  }

  /* ── 初始化 ─────────────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', function () {
    initDrawer();
    initTheme();
    initBackToTop();
    initSearch();
    initLegacyMenu();
    initDropdown();
  });

})();
