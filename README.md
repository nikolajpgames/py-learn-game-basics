# PyGameTeaching

Learning to code by building a game, one small session at a time.
Forty-one sessions, ending in a Geometry Dash clone with a level editor.

**These are the teaching notes — for Dad, not for the student.** The student
reads the lesson pages.

---

## Getting started

Once, ever:

```
setup.bat
```

That builds a `.venv` folder with its own private Python and installs
`pygame-ce`. Nothing is installed system-wide, and deleting `.venv` undoes it
completely.

Then, per session:

```
.\learn.bat 6    opens the lesson page in a browser
.\run.bat 6      runs that session's game
```

The `.\` on the front is not optional. PowerShell will not run anything
from the folder you are standing in without it, and says
`The term 'run.bat' is not recognized` if you leave it off. The `.\` form
works in PowerShell, cmd.exe and the VS Code terminal alike.

Two separate commands on purpose. The lesson page gets opened once at the
start; the game gets run thirty times during the session, and a browser tab
popping up each time would drive everyone mad.

---

## How a session works

**25–40 minutes.** One new *theme* per session. The test is whether you can
say what the session is about in a single sentence — not whether it introduces
exactly one keyword. Session 8 brings tuples, lists and looping over a list
all at once, and that's fine, because they arrive as one idea: *many things
under one name*.
If you can't say it in a sentence, it's two sessions.

Every lesson page has the same seven parts, in the same order, every time:

| Part | What it's for |
|---|---|
| What you're making | The target, before any explanation |
| New this session | Three or four sentences. No more |
| Steps | Clickable checklist, remembers itself |
| Turn the knobs | Numbers to fiddle with, and what each one does |
| Stuck? | Hints that escalate, ending in the actual code |
| Challenge | Optional, for good days |
| How it could break | The errors *this* session really produces |

### Two rules worth keeping

**Never end a session on broken code.** Always stop at something that runs,
even if the last five minutes are just backing a change out. Coming back to a
broken program is how projects die.

**Session boundaries are for stopping, not pacing.** If he's on a roll at
minute 40, keep going — you'll just do 12 and 13 together. The numbering is a
map, not a timetable.

### On the hints

The hints deliberately end with the full working code. The bet is that
unblocking beats stalling, and that someone who reads the answer at Session 6
usually doesn't need it by Session 9. If that turns out to be wrong for him,
delete the last `<details>` block from the page — the rest still works.

---

## The plan

Forty-one sessions. At two a week that is about five months, with natural
stopping points along the way.

### Arc 0 · Getting started

No graphics at all. Five short sessions on the language itself, so that when a
window finally opens, nothing in the file is a mystery.

| # | Build | New this session |
|---|---|---|
| 1 | The computer says things | `print`, comments, top-to-bottom order |
| 2 | A tiny scoreboard | Variables; words vs. numbers; f-strings |
| 3 | It reacts to a number | `if`/`else`, comparisons, **the indent is the block** |
| 4 | Two counters | `for`, `while`, `range` — and how to hang a program |
| 5 | Words you invented | `def`, arguments, `return`, **scope** |

### Arc 1 · First pixels

| # | Build | New this session |
|---|---|---|
| 6 | Window opens, background colour | A program that stays open needs a loop |
| 7 | Points, lines, rects, circles | Coordinates — and y counts *downwards* |
| 8 | **Three stars, by hand** | Tuples and lists; one loop replaces four draw lines |
| 9 | **Two hundred stars** | A loop that *builds* data; `.append`, `random` |

Sessions 8 and 9 are deliberately two sessions rather than one. Eight is about
a loop that walks a list you wrote; nine is about a loop that writes the list
for you. Those are different ideas, and eight has to hurt a little — four
near-identical draw lines — before nine feels like a rescue.

### Arc 2 · Motion and time

| # | Build | New this session |
|---|---|---|
| 10 | One box slides across | `update` changes the game state, `draw` paints a frame of it |
| 11 | Speed in pixels per *second* | Delta time |
| 12 | **The DVD logo bouncer** | Four questions in a row |
| 13 | Fifty bouncers | Dicts — many things, same code |
| 14 | **When boxes meet** | Box-on-box collision, by hand |
| 15 | Three files | Splitting a program up; `import` between files |

**Classes are deliberately not here.** They would mean `class`, `self`,
`__init__` and instantiation all at once, which is a lot on top of everything
else in this arc — and dicts plus functions carry the whole of Pong and
Arkanoid perfectly well. They can arrive in Arc 5, where the player, blocks and
spikes each start needing their own behaviour and the case for them makes
itself. If he takes to all this easily, bring them forward; if not, the course
works without them.

### Arc 3 · Input, and a finished game — a shooter

| # | Build | New this session |
|---|---|---|
| 16 | A ship you steer | Held keys; input read in `main`, movement in `state` |
| 17 | **Press to fire** | Key *events*; adding to a list while the game runs |
| 18 | Shots that clean up after themselves | **Removing from a list** without the classic trap |
| 19 | Something to shoot | Collision put to work; removing both sides |
| 20 | Score and game over | Text on screen, and a state machine |

Session 20 is the first finished game — score, an end, and a restart. Worth
stopping on for a week and letting him show someone.

Pong was the obvious choice here and is the weaker one. A shooter forces things
to be *created* and *destroyed* while the game runs, which Pong never does —
and removing items from a list is both the trickiest everyday Python trap and
exactly what Arc 4 needs for breaking bricks.

### Arc 4 · Levels are data — Arkanoid

| # | Build | New this session |
|---|---|---|
| 21 | Bat and ball | Nothing. Assembly from parts he already has |
| 22 | The bat hits back | Bounce *response*, and aiming by where you hit |
| 23 | A wall of bricks | Nested loops; rows and columns into x and y |
| 24 | Knock them out | Ball-vs-brick, and removing while looping — again |
| 25 | **Which side did it hit?** | Overlap *depth*; flipping the right axis |
| 26 | Three lives | Losing the ball; lives; reusing the state machine |
| 27 | **Levels from a text file** | Reading files, parsing strings into a grid |
| 28 | More levels | Progression, and a win screen |

Eight, not the four this used to say. Arkanoid has to build its own bat, ball
and brick wall before it can get anywhere near levels, and the two starred
sessions are each a full sitting on their own.

**The three things this arc exists for are all Geometry Dash prerequisites.**
Grids (28 needs them for the level format), loading a level from a file (28
again), and working out which side of something you hit — which is exactly the
difference between landing on a block and clipping its edge. Better learned
here, on a bouncing ball, than later with gravity and scrolling on top.

Session 21 is a deliberately easy one: a whole new game's skeleton assembled in
half an hour from things he has already written. Good for a low-energy evening,
and a fair measure of how much has stuck.

### Arc 5 · Geometry Dash, in rectangles

| # | Build | New this session |
|---|---|---|
| 29 | A square that jumps | Gravity: acceleration vs. velocity |
| 30 | Landing on the ground | One-way collision, being "grounded" |
| 31 | The world scrolls past | World coordinates vs. screen coordinates |
| 32 | Level from a file: blocks and spikes | Reusing the Session 27 loader |
| 33 | Die on spikes, instant restart | Resetting state cleanly |
| 34 | Attempt counter, progress bar | State that survives a restart |
| 35 | The cube rotates mid-jump | `transform.rotate` |

### Arc 6 · Juice

| # | Build | New this session |
|---|---|---|
| 36 | Jump and death sounds | `mixer`, loading assets |
| 37 | Music, obstacles on the beat | `x = beat × speed` |
| 38 | Sprites instead of rectangles | Images and transparency |
| 39 | Death explosion, cube trail | Particles — a list of short-lived things |
| 40 | Pulsing background | Time-based animation |
| 41 | **Click-to-place level editor** | Mouse input, and *writing* files |

Session 41 is the real destination: a tool he built, making levels for a game
he built.

### Where to stop, if you need to

There are three points where he has a finished thing and could put it down for
a month without it feeling abandoned:

- **Session 12** — the DVD bouncer. Not a game, but a satisfying object.
- **Session 20** — the shooter. A complete game with a score and an ending.
- **Session 28** — Arkanoid, with levels he wrote himself in Notepad.

If momentum flags in Arc 4, it compresses to six sessions: fold 21 into 22, and
27 into 28. It gets denser, not shorter — but it keeps moving.


## How the folders work

Sessions 1–28 are **frozen snapshots**. Each folder is complete and runnable on
its own, so he can go back and run Session 12 any time to watch the bouncer
again, and `diff` between two folders shows exactly what one session added.

From Session 29 the game stops being snapshotted and becomes one living project
in `geometrydash/`. That's the point where "a real project changes over time"
is itself the lesson, and the natural moment to introduce git as a time machine
(`git tag s31`, so any session can still be replayed). Before then git is
overhead he doesn't need.

```
PyGameTeaching/
  setup.bat            once, ever
  .\run.bat 6         run session 6
  .\learn.bat 6       open session 6's lesson page
  sessions/
    _shared/
      lesson.css       all forty-one pages share these two
      lesson.js        ticks + checklist persistence
    s01_hello/
      main.py
      lesson.html
    ...
  geometrydash/        appears at session 29
  assets/              images, sounds, music
  tools/               level editor, session 41
```

### The menu, and where the curriculum lives

Every page grows a left-hand menu listing the sessions in **its own part** of
the course, with links up to the part before and down to the part after. It
also ticks off sessions whose checklists are fully complete, so he can see how
far he's got without opening anything.

All of that is built from one list — `ARCS` at the top of
`sessions/_shared/lesson.js`. That list is the single source of truth for the
whole curriculum. Sessions with a `dir` are live links; sessions without one
show greyed out as "not written yet", which is why the menu already shows the
whole plan out to Session 36.

### Adding a session

1. Copy the previous folder, rename it `sNN_short_name`, and edit `main.py`
   down to the **starting** state.
2. Copy a `lesson.html` as the template and set `data-session="N"` on the
   `<html>` tag. That one attribute drives the ticks, the checklist's storage
   key, and which menu entry is highlighted.
3. Add `dir: "sNN_short_name"` to that session's entry in `ARCS`.

That's it — no navigation to fix up by hand anywhere. Renaming a folder means
changing it in `ARCS` too, and nothing else.

### A detail worth knowing

Sessions 11 and 12 ship in a deliberately **unfinished** state — Session 11's box
is still tied to the frame rate, Session 12's box escapes off the screen. The
bug is the lesson. Don't "fix" them before he sees them.

---

## Editor warnings

Zed uses **basedpyright** as its Python language server, and its default mode
(`recommended`) demands type annotations on everything. On these files that
produced **252 warnings across the first six pygame programs** — squiggles under
`pygame.init()`, under every parameter, under `screen.fill(...)`. For a beginner
that reads as "you did it wrong", when the code is perfectly ordinary pygame.

`pyrightconfig.json` in the project root fixes it, and brings that 252 down to
zero. It travels with the repo, so it works on any machine that opens the
project — no per-editor setup.

The three rules turned off by name are the ones that fire on normal teaching code:

- `reportUnusedCallResult` — `pygame.init()` and `screen.fill()` both return
  something we ignore, which is completely standard.
- `reportUnusedVariable` — `for i in range(200):` never uses `i`, and that's fine.
- `reportMissingTypeStubs` — noise about libraries we don't control.

If you'd rather have this apply to every Python project you open, the same
settings can go in Zed's own config instead — but the project file is the one
tested here.

### A note on the Python install

`.venv` was built by the **Microsoft Store** Python. Its `pyvenv.cfg` points
`home` at a WindowsApps alias folder that contains no standard library, and the
real one sits under `C:\Program Files\WindowsApps` behind locked-down
permissions. Tools that follow `home` to find the stdlib can come up empty.

Nothing is broken today and the games all run. But if the editor ever claims
`import random` can't be resolved, that's the cause — and installing Python from
python.org and re-running `setup.bat` is the durable fix.

## Notes

- **pygame-ce**, not pygame. Drop-in replacement, same `import pygame`, but
  actively maintained where upstream has been stop-start.
- **Fonts need internet** the first time a lesson page loads. Offline it falls
  back to system fonts and everything still works, just plainer.
- **Lesson pages are plain local files.** No server, no build step. Double-click
  one and it opens.
- **Session folders have to stay put**, one level under `sessions/`. Each page
  reaches its stylesheet with `../_shared/lesson.css`, so a folder moved to a
  different depth loses all its styling. If you ever need to send a single
  lesson page to someone on its own, send the `_shared` folder with it.
- Checklist ticks live in the browser's local storage, per session. Clearing
  browser data resets them; nothing else does.
#   p y - b e g i n n e r - g a m e - c o u r s e - v 1  
 #   p y - l e a r n - g a m e - b a s i c s  
 