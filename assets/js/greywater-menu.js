// Greywater title menu: hover and keyboard resolve to the same selected row (roving tabindex).
(function () {
  var menu = document.querySelector('.gw-menu');
  if (!menu) return;
  var rows = Array.prototype.slice.call(menu.querySelectorAll('.gw-row'));
  var status = document.querySelector('.gw-status');
  var current = 0;

  function select(i, focus) {
    current = (i + rows.length) % rows.length;
    rows.forEach(function (r, n) {
      var on = n === current;
      r.classList.toggle('is-selected', on);
      r.setAttribute('tabindex', on ? '0' : '-1');
    });
    if (focus) rows[current].focus();
  }

  rows.forEach(function (row, i) {
    row.addEventListener('mouseenter', function () { select(i, false); });
    row.addEventListener('focus', function () { select(i, false); });
    row.addEventListener('click', function () {
      select(i, false);
      var label = row.childNodes[0].textContent.trim();
      if (status) status.textContent = 'Selected: ' + label;
    });
  });

  menu.addEventListener('keydown', function (e) {
    var k = e.key;
    if (k === 'ArrowDown' || k === 's' || k === 'S') { e.preventDefault(); select(current + 1, true); }
    else if (k === 'ArrowUp' || k === 'w' || k === 'W') { e.preventDefault(); select(current - 1, true); }
    else if (k === 'Escape') { if (status) status.textContent = ''; select(0, true); }
  });
})();
