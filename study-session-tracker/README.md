# Study Session Tracker

A command-line study session tracker to log, view, and analyze your study sessions by subject. This tool helps you track time spent studying, add notes, and review session statistics.

---

## Features

- add study sessions with subject, duration, date, and optional notes  
- view all sessions organized by subject  
- track session statistics: total time, total sessions, average session, most/least studied subjects  
- save and load sessions to/from a file  
- seed data for initial testing

---

## Getting Started

### Requirements

- python 3.8 or higher  
- works on windows, mac, and linux

### Installation

1. clone the repository:

git clone https://github.com/onederlnd/study-session-tracker.git

2. navigate into the project folder:

cd study-session-tracker

3. run the main program:

python main.py

---

## Usage

When you run the program, you will see a menu:

choose an option:  
1 - add session  
2 - view sessions  
3 - session stats  
4 - save sessions  
5 - quit

- add session → enter subject, session length, date (optional), and notes (optional)  
- view sessions → see all logged sessions grouped by subject  
- session stats → view total study time, number of sessions, average session time, most/least studied subjects  
- save sessions → save all sessions to sessions.json  
- quit → save sessions and exit the program

---

## File Structure

study-session-tracker/  
├─ main.py          # main program loop and menu  
├─ utils.py         # helper functions for input validation and date parsing  
├─ sessions.py      # functions to add and view sessions  
├─ stats.py         # functions to calculate and display statistics  
├─ persistence.py   # functions to save/load sessions to/from file  
└─ seed.py          # initial seed session data  

---

## Example Seed Data

- math → 15, 30 min sessions  
- science → 50 min session  
- reading → 30, 65, 50 min sessions  
- history → 90 min session  

---

## Contributing

This project is self-contained for personal use, but contributions are welcome:

- add session editing  
- add search/filter by date or subject  
- improve statistics (weekly/monthly summaries)  
- enhance CLI experience with colors or menus  

---

## License

MIT License