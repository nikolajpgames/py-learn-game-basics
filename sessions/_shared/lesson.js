/* ============================================================
   Lesson pages — shared behaviour

     * THE CURRICULUM lives here, once. Adding a session means
       editing the ARCS list below and nothing else.
     * builds the left-hand menu for the current arc
     * the progress ticks in the eyebrow
     * checklist state, remembered per session

   Reads data-session="9" from the <html> element.
   ============================================================ */

var ARCS = [
  { name: "Getting Started", sessions: [
    { n: 1,  title: "Making It Talk",      dir: "s01_hello" },
    { n: 2,  title: "Boxes With Names",    dir: "s02_variables" },
    { n: 3,  title: "Asking Questions",    dir: "s03_questions" },
    { n: 4,  title: "Doing It Again",      dir: "s04_again" },
    { n: 5,  title: "Your Own Words",      dir: "s05_functions" }
  ]},
  { name: "First Pixels", sessions: [
    { n: 6,  title: "Your First Window",   dir: "s06_first_window" },
    { n: 7,  title: "Drawing By Numbers",  dir: "s07_drawing" },
    { n: 8,  title: "Three Stars By Hand", dir: "s08_stars_by_hand" },
    { n: 9,  title: "Two Hundred Stars",   dir: "s09_stars" }
  ]},
  { name: "Motion & Time", sessions: [
    { n: 10, title: "It Moves",            dir: "s10_it_moves" },
    { n: 11, title: "Real Speed",          dir: "s11_real_speed" },
    { n: 12, title: "The DVD Bouncer",     dir: "s12_dvd" },
    { n: 13, title: "Fifty Bouncers",      dir: "s13_many" },
    { n: 14, title: "When Boxes Meet",     dir: "s14_collide" },
    { n: 15, title: "Three Files",         dir: "s15_tidy" }
  ]},
  { name: "Shooter", sessions: [
    { n: 16, title: "Your Ship",           dir: "s16_ship" },
    { n: 17, title: "Press To Fire",       dir: "s17_fire" },
    { n: 18, title: "Cleaning Up",         dir: "s18_cleanup" },
    { n: 19, title: "Something To Shoot",  dir: "s19_targets" },
    { n: 20, title: "Score And Game Over", dir: "s20_score" }
  ]},
  { name: "Arkanoid", sessions: [
    { n: 21, title: "Bat And Ball", dir: "s21_batball" },
    { n: 22, title: "The Bat Hits Back", dir: "s22_bounce" },
    { n: 23, title: "A Wall Of Bricks", dir: "s23_bricks" },
    { n: 24, title: "Knock Them Out", dir: "s24_break" },
    { n: 25, title: "Which Side Did It Hit?", dir: "s25_side" },
    { n: 26, title: "Three Lives", dir: "s26_lives" },
    { n: 27, title: "Levels From A File", dir: "s27_file" },
    { n: 28, title: "More Levels", dir: "s28_more" }
  ]},
  { name: "Geometry Dash", sessions: [
    { n: 29, title: "A Square That Jumps" },
    { n: 30, title: "Landing" },
    { n: 31, title: "The World Scrolls" },
    { n: 32, title: "Blocks And Spikes" },
    { n: 33, title: "Death And Restart" },
    { n: 34, title: "Attempts" },
    { n: 35, title: "The Cube Rotates" }
  ]},
  { name: "Juice", sessions: [
    { n: 36, title: "Sounds" },
    { n: 37, title: "On The Beat" },
    { n: 38, title: "Sprites" },
    { n: 39, title: "Particles" },
    { n: 40, title: "Pulsing Background" },
    { n: 41, title: "The Level Editor" }
  ]}
];

(function () {
  "use strict";

  var session = parseInt(document.documentElement.getAttribute("data-session"), 10) || 1;

  var TOTAL = 0;
  var arcIndex = 0;
  ARCS.forEach(function (arc, i) {
    TOTAL += arc.sessions.length;
    arc.sessions.forEach(function (s) { if (s.n === session) arcIndex = i; });
  });

  /* ---- has a session been finished? ---- */

  function isDone(n) {
    try {
      var raw = localStorage.getItem("pygameteaching-s" + n);
      if (!raw) return false;
      var saved = JSON.parse(raw);
      return Array.isArray(saved) && saved.length > 0 && saved.every(Boolean);
    } catch (e) {
      return false;               /* storage blocked — just show nothing */
    }
  }

  /* ---- the left-hand menu ---- */

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }

  function arcLink(dir, kind, label, name) {
    var wrap = el("div", "arc-jump " + kind);
    wrap.appendChild(el("span", "arc-jump-label", label));
    if (dir) {
      var a = el("a", "arc-jump-name", name);
      a.href = "../" + dir + "/lesson.html";
      wrap.appendChild(a);
    } else {
      wrap.appendChild(el("span", "arc-jump-name empty", name + " — not written yet"));
    }
    return wrap;
  }

  function buildNav() {
    var arc = ARCS[arcIndex];
    var nav = el("nav", "sidenav");
    nav.setAttribute("aria-label", "Sessions in this part of the course");

    var first = arc.sessions[0].n, last = arc.sessions[arc.sessions.length - 1].n;
    nav.appendChild(el("div", "sidenav-kicker", "SESSIONS " + first + "–" + last));
    nav.appendChild(el("h2", "sidenav-arc", arc.name));

    if (arcIndex > 0) {
      var prev = ARCS[arcIndex - 1];
      nav.appendChild(arcLink(prev.sessions[0].dir, "up", "↑ Before this",
                              prev.name));
    }

    var list = el("ol", "sidenav-list");
    arc.sessions.forEach(function (s) {
      var li = el("li");
      var isHere = s.n === session;
      var done = !isHere && isDone(s.n);

      var inner = s.dir && !isHere ? el("a") : el("span");
      inner.className = "sidenav-item"
        + (isHere ? " here" : "")
        + (!s.dir ? " todo" : "")
        + (done ? " done" : "");
      if (s.dir && !isHere) inner.href = "../" + s.dir + "/lesson.html";
      if (isHere) inner.setAttribute("aria-current", "page");

      inner.appendChild(el("span", "sidenav-num", String(s.n)));
      inner.appendChild(el("span", "sidenav-title", s.title));
      inner.appendChild(el("span", "sidenav-mark", done ? "✓" : ""));

      li.appendChild(inner);
      list.appendChild(li);
    });
    nav.appendChild(list);

    if (arcIndex < ARCS.length - 1) {
      var next = ARCS[arcIndex + 1];
      nav.appendChild(arcLink(next.sessions[0].dir, "down", "Next ↓", next.name));
    }

    document.body.insertBefore(nav, document.body.firstChild);
  }

  buildNav();

  /* ---- progress ticks ---- */

  var ticks = document.getElementById("ticks");
  if (ticks) {
    for (var t = 1; t <= TOTAL; t++) {
      var i = document.createElement("i");
      if (t < session) i.className = "on";
      if (t === session) i.className = "now";
      ticks.appendChild(i);
    }
  }

  /* ---- checklist ---- */

  var list = document.getElementById("checks");
  if (!list) return;

  var KEY = "pygameteaching-s" + session;
  var boxes = Array.prototype.slice.call(list.querySelectorAll("input[type=checkbox]"));
  var tally = document.getElementById("tally");
  var clear = document.getElementById("clear");

  function load() {
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return;
      var saved = JSON.parse(raw);
      if (!Array.isArray(saved)) return;
      boxes.forEach(function (b, n) { b.checked = !!saved[n]; });
    } catch (e) {
      /* storage blocked or unavailable — the page still works, it just forgets */
    }
  }

  function save() {
    try {
      localStorage.setItem(KEY, JSON.stringify(boxes.map(function (b) { return b.checked; })));
    } catch (e) {
      /* nothing sensible to do */
    }
  }

  function count() {
    if (!tally) return;
    var n = boxes.filter(function (b) { return b.checked; }).length;
    tally.textContent = n + " of " + boxes.length + " done";
  }

  boxes.forEach(function (b) {
    b.addEventListener("change", function () { save(); count(); });
  });

  if (clear) {
    clear.addEventListener("click", function () {
      boxes.forEach(function (b) { b.checked = false; });
      save();
      count();
    });
  }

  load();
  count();
})();
