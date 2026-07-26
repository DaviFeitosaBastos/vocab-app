# vocab-app

> A personal English vocabulary trainer — surfaces a new word daily, tracks progress, and lets you search a 13,000+ entry dictionary. Runs as a native desktop app powered by Python and PyWebView.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-green?style=flat-square) ![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## About

`vocab-app` is a desktop application built to make daily English vocabulary practice frictionless. Each session surfaces a new, previously unseen word from a local 13,500+ entry dictionary, tracks what you've already reviewed, and lets you search any word by name. The interface runs inside a native window built with PyWebView — HTML/CSS/JS on the front, Python on the back. Built as both a practical learning tool and a hands-on Python project covering JSON persistence, file I/O, class design, and frontend integration.

---

## Features

- **Daily word** — loads a random unseen word on startup and marks it as seen automatically
- **Next word** — cycle through new words one at a time within a session
- **Search** — look up any word by name, with part of speech, definition, and synonyms
- **Progress tracking** — view stats (words seen, remaining, percentage) and the full list of reviewed words
- **Persistent state** — progress saved to disk between sessions via `progress.json`
- **Local dictionary** — 13,500+ entries with grammatical class, definition, and synonyms, pre-built from frequency-ranked word data
- **Native window** — runs as a desktop app via PyWebView, no browser required

---

## Project Structure

```
vocab-app/
├── app/
│   ├── app.py               # Entry point — starts the PyWebView window
│   ├── api.py               # Api class — exposes Python functions to JS
│   ├── utils.py             # Core logic — load/save dictionary and progress
│   ├── log_utils.py         # Logging setup (console + file, via RichHandler)
│   ├── progress.json        # Auto-created on first run
│   └── frontend/
│       ├── index.html       # App UI — three screens (daily, search, progress)
│       ├── style.css        # Dark theme, Inter + Space Mono typography
│       └── script.js        # Navigation and PyWebView API calls
├── data/
│   ├── raw/                 # Source word list + frequency data
│   └── processed/
│       └── dictionary.json  # Final built dictionary consumed by the app
├── scripts/
│   └── build_dictionary.py  # Merges raw data into dictionary.json
├── requirements.txt
└── .gitignore
```

---

## Requirements

- Python 3.11+
- Linux: `webkit2gtk4.1-devel` system package required for PyWebView
- No external API calls at runtime — the dictionary is fully local

---

## Installation

```bash
# Clone the repository
git clone https://github.com/DaviFeitosaBastos/vocab-app.git
cd vocab-app

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux
venv\Scripts\Activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Linux only — install WebKit system dependency
sudo dnf install webkit2gtk4.1-devel   # Fedora
sudo apt install libwebkit2gtk-4.1-dev # Ubuntu/Debian
```

---

## Usage

```bash
cd app
python3 app.py
```

The app opens a native window with three screens:

- **Daily** — shows today's word with definition and synonyms; click "Next word" to advance
- **Search** — type any word to look it up in the full dictionary
- **Progress** — shows how many words you've seen, how many remain, and the full reviewed list

---

## Output

| File | Content |
|---|---|
| `app/progress.json` | List of word IDs reviewed (auto-created on first run) |
| `app/app.log` | Timestamped log file with events and errors |

---

## Rebuilding the Dictionary

The dictionary in `data/processed/dictionary.json` is generated from two raw sources: a word frequency list and a raw English dictionary. To rebuild after changing the source data:

```bash
cd scripts
python build_dictionary.py
```

This produces a frequency-ordered JSON of 13,500+ entries, each with `Id`, `Word`, `Meanings`, and `Synonyms`.

---

## Dependencies

| Package | Purpose |
|---|---|
| `pywebview` | Native desktop window with HTML/CSS/JS frontend |
| `rich` | Terminal logging and CLI output |

---

## Roadmap

- [ ] Spaced-repetition scheduling instead of pure random selection
- [ ] NSFW word toggle in settings
- [ ] Package as AppImage (Linux)
- [x] Desktop app with PyWebView
- [x] Daily word with automatic progress tracking
- [x] Search by word name
- [x] Progress screen with stats and word list
- [x] Local dictionary built from frequency-ranked data
- [x] Structured logging to file and console

---

## Author

[DaviFeitosaBastos](https://github.com/DaviFeitosaBastos)