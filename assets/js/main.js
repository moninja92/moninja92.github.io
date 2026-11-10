// Booklet behaviours: Screen Guide callout linking, leader-line draw-in,
// copy-email button, footer year.
(function () {
  document.documentElement.classList.add('js');

  // Link each numbered callout on a plate with its legend row.
  // Hover previews a number; focus or a click/tap selects it until another
  // entry is chosen, so the link works with a mouse, a keyboard and a finger.
  var canHover = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  document.querySelectorAll('.guide').forEach(function (guide) {
    var parts = guide.querySelectorAll('[data-n]');
    var rows = guide.querySelectorAll('.legend li[data-n]');
    var plate = guide.querySelector('.plate');
    var picked = null;
    var buttons = {};

    function show(n) {
      parts.forEach(function (el) { el.classList.toggle('is-hot', n !== null && el.getAttribute('data-n') === n); });
      guide.classList.toggle('has-hot', n !== null);
    }
    function pick(n) {
      picked = n;
      Object.keys(buttons).forEach(function (k) { buttons[k].setAttribute('aria-pressed', String(k === n)); });
      show(n);
    }
    // Bring the plate's pin into view when it is off screen (phones, tall plates).
    function reveal(n) {
      if (!plate || n === null) return;
      var pin = plate.querySelector('.pin[data-n="' + n + '"]');
      if (!pin) return;
      var r = pin.getBoundingClientRect();
      var bar = window.innerWidth < 1000 ? 64 : 0;
      if (r.top < 8 || r.bottom > window.innerHeight - bar - 8) {
        var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        pin.scrollIntoView({ block: 'center', behavior: reduce ? 'auto' : 'smooth' });
      }
    }

    // Each legend name becomes a real button, so rows are reachable by Tab.
    rows.forEach(function (row) {
      var n = row.getAttribute('data-n');
      var name = row.querySelector('b');
      if (!name) return;
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'legend-pick';
      btn.setAttribute('aria-pressed', 'false');
      while (name.firstChild) btn.appendChild(name.firstChild);
      name.appendChild(btn);
      buttons[n] = btn;
      btn.addEventListener('focus', function () { pick(n); });
      btn.addEventListener('click', function () { pick(n); reveal(n); });
      // The whole row is a tap target; the button keeps the keyboard semantics.
      row.addEventListener('click', function (e) { if (e.target !== btn && !btn.contains(e.target)) btn.click(); });
    });

    // Pins on the plate: tapping one selects its row.
    guide.querySelectorAll('.plate .pin, .plate .co').forEach(function (el) {
      el.addEventListener('click', function () {
        var n = el.getAttribute('data-n');
        pick(n);
        var row = guide.querySelector('.legend li[data-n="' + n + '"]');
        if (row && !canHover) row.scrollIntoView({ block: 'nearest' });
      });
    });

    if (canHover) {
      parts.forEach(function (el) {
        var n = el.getAttribute('data-n');
        el.addEventListener('mouseenter', function () { show(n); });
        el.addEventListener('mouseleave', function () { show(picked); });
      });
    }

    // Leaving the guide by keyboard clears the selection.
    guide.addEventListener('focusout', function (e) {
      if (!guide.contains(e.relatedTarget) && !guide.matches(':hover')) pick(null);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && picked !== null) pick(null);
    });

    // The hint names the input the visitor actually has.
    var hint = guide.querySelector('.plate-cap .how');
    if (hint) hint.textContent = canHover ? 'Hover or select an entry to find it on the screen.' : 'Tap an entry or a pin to match them up.';
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

  // Phone tab bar: start with the current chapter in view, and drop the
  // right-edge fade once the strip is scrolled to its end.
  var strip = document.querySelector('.tabs ol');
  if (strip) {
    var current = strip.querySelector('[aria-current="page"]');
    if (current && strip.scrollWidth > strip.clientWidth) {
      strip.scrollLeft = Math.max(0, current.parentElement.offsetLeft - 8);
    }
    var edge = function () {
      strip.classList.toggle('at-end', strip.scrollLeft + strip.clientWidth >= strip.scrollWidth - 4);
    };
    strip.addEventListener('scroll', edge, { passive: true });
    window.addEventListener('resize', edge);
    edge();
  }

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
