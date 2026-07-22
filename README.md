# vocab-app
> A terminal-based English vocabulary trainer that surfaces a new word each day, tracks what you've learned, and lets you search any word in a 13,000+ entry dictionary.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-green?style=flat-square) ![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## About
`vocab-app` is a CLI tool built to make daily English vocabulary practice frictionless. Each session shows a new, previously unseen word with its meaning, keeps track of which words you've already reviewed, and lets you look up any word by name or ID. The whole experience runs in the terminal with a styled interface built on Rich. It exists as both a practical English-learning tool and a playground for practicing Python fundamentals (I/O, JSON persistence, logging, CLI UX).

---

## Features
- Daily word — pulls a random unseen word from the dictionary and marks it as seen
- Progress tracking — view every word you've reviewed so far, in order
- Search — look up any word by name or ID, with meaning and synonyms
- Persistent state — progress is saved to disk between sessions
- Structured logging — errors and events logged to both console (Rich) and file
- Local dictionary — 13,500+ words with grammatical class, definition, and synonyms, pre-built from raw word/frequency data

---

## Project Structure
```
vocab-app/
├── app/
│   ├── main.py            # Entry point — menu loop and command dispatch
│   ├── ui.py               # Rich-based CLI display (menus, panels, tables)
│   ├── utils.py             # Core logic — dictionary lookup, progress persistence
│   ├── log_utils.py         # Logging setup (console + file, via RichHandler)
│   └── frontend/            # Early-stage web UI prototype (HTML/CSS/JS, not yet wired to the app)
├── data/
│   ├── raw/                 # Source word list + frequency data
│   └── processed/           # Built dictionary.json consumed by the app
├── scripts/
│   └── build_dictionary.py  # Merges raw data into the final dictionary.json
├── requirements.txt
└── .gitignore
```

---

## Requirements
- Python 3.11+
- No external services — the dictionary is fully local, no API calls at runtime

---

## Installation
```bash
# Clone the repository
git clone https://github.com/DaviFeitosaBastos/vocab-app.git
cd vocab-app

# Create and activate a virtual environment
python -m venv venv

# Linux
source venv/bin/activate
# Windows
venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage
```bash
cd app

# Linux
python3 main.py
# Windows
python main.py
```

On launch, you'll see a menu with three options: get today's word, view your progress, or search for a specific word by name or ID. Type the number of the option and press Enter; type `0` to exit.

---

## Output
| Folder / File | Content |
|---|---|
| `app/progress.json` | List of word IDs you've already seen (auto-created on first run) |
| `app.log` | Log file with timestamped events and errors |

---

## Rebuilding the dictionary
The dictionary shipped in `data/processed/dictionary.json` is generated from raw sources. To rebuild it after changing the raw data:
```bash
cd scripts
python build_dictionary.py
```

---

## Dependencies
| Package | Purpose |
|---|---|
| `rich` | Terminal UI — panels, tables, prompts, progress bars, logging handler |

---

## Roadmap
- [ ] Finish and wire up the web frontend (`app/frontend/`)
- [ ] Packaged executable (PyInstaller)
- [ ] Spaced-repetition scheduling instead of pure random selection
- [x] CLI with daily word, progress tracking, and search
- [x] Structured logging to file and console

---

## Notes
- The `app/frontend/` folder is an early, disconnected prototype for a future web version — it is not yet integrated with the Python backend.
- `progress.json` is created automatically on first run if it doesn't exist yet.

---

## Author
[DaviFeitosaBastos](https://github.com/DaviFeitosaBastos)