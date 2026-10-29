# Azcorra Academy

Isaac's personal academy: an **IQ Lab** of adaptive reasoning games and full **courses** (Math, Vocabulary, Writing, Science) from 7th grade to AP level.

**Live:** https://doctorslapabih.github.io/azcorra-academy/

## Install it as an app (Ubuntu)
1. Open the link above in **Chrome** or **Chromium**.
2. Click the install icon at the right end of the address bar (or ⋮ → *Cast, save and share* → *Install page as app*).
3. It gets its own window and shows up in your Ubuntu app launcher. It works offline for anything you've opened before.

## How it's built
Plain HTML, CSS and JavaScript. No build step. Progress is saved in the browser (localStorage); the Journal page can copy entries for logging in Notion and make a backup to move between devices.

- `js/games/` — IQ Lab games (matrix reasoning, number series, digit span, n-back, symbol search, mental rotation, analogies, logic)
- `data/courses/index.json` — course roadmaps
- `data/lessons/<course>/<lesson>.json` — lesson content
- `data/iq/` — Lab readings
