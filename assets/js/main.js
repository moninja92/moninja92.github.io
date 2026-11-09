// Booklet behaviours: Screen Guide callout linking, leader-line draw-in,
// copy-email button, footer year.
(function () {
  document.documentElement.classList.add('js');

  // Link each numbered callout on a plate with its legend row.
  document.querySelectorAll('.guide').forEach(function (guide) {
    var parts = guide.querySelectorAll('[data-n]');
    function set(n, on) {
      parts.forEach(function (el) {
        if (el.getAttribute('data-n') === n) el.classList.toggle('is-hot', on);
      });
    }
    parts.forEach(function (el) {
      var n = el.getAttribute('data-n');
      el.addEventListener('mouseenter', function () { set(n, true); });
      el.addEventListener('mouseleave', function () { set(n, false); });
      el.addEventListener('focusin', function () { set(n, true); });
      el.addEventListener('focusout', function () { set(n, false); });
    });
  });

  // Leader lines draw in once when a Screen Guide enters view.
  var guides = document.querySelectorAll('.guide');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('seen'); io.unobserve(e.target); }
      });
    }, { threshold: 0.35 });
    guides.forEach(function (g) { io.observe(g); });
  } else {
    guides.forEach(function (g) { g.classList.add('seen'); });
  }

  // Copy email.
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    var status = document.getElementById(btn.getAttribute('aria-describedby'));
    btn.addEventListener('click', function () {
      var text = btn.getAttribute('data-copy');
      function say(msg) { if (status) status.textContent = msg; }
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(
          function () { say('Copied ' + text + ' to your clipboard.'); },
          function () { say('Copy was blocked by the browser. Select the address above instead.'); }
        );
      } else {
        say('Copy is not available here. Select the address above instead.');
      }
    });
  });

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
