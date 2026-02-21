"""
- edit session
- subtopics
"""


import datetime
import time
import sys

# Text colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Text styles
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

filename = "sessions.txt"
SESSION_LIST = {}

SEED_LIST = {
        "Math": [
            {"sess_length": 15, "sess_date": datetime.date(2026, 3, 20), "sess_note": "these are notes"},
            {"sess_length": 30, "sess_date": datetime.date(2026, 3, 20), "sess_note": "these are notes"},
        ],
        "Science": [
            {"sess_length": 50, "sess_date": datetime.date(2026, 3, 20), "sess_note": "these are notes"},

        ],
        "Reading": [
            {"sess_length": 30, "sess_date": datetime.date(2026, 3, 20), "sess_note": "these are notes"},
            {"sess_length": 65, "sess_date": datetime.date(2026, 3, 20), "sess_note": "these are notes"},
            {"sess_length": 50, "sess_date": datetime.date(2026, 3, 20), "sess_note": "these are notes"},
        ],
        "History": [
            {"sess_length": 90, "sess_date": datetime.date(2026, 3, 20), "sess_note": "these are notes"},
        ]
}
# sample list
# SEED_LIST = {
#         "Math": [
#             {"sess_length": 15, "sess_date": datetime.date(2026, 3, 20)},
#             {"sess_length": 30, "sess_date": datetime.date(2026, 3, 20)},
#         ],
#         "Science": [
#             {"sess_length": 50, "sess_date": datetime.date(2026, 3, 20)},
#         ],
#         "Reading": [
#             {"sess_length": 30, "sess_date": datetime.date(2026, 3, 20)},
#         ],
#         "History": [
#             {"sess_length": 180, "sess_date": datetime.date(2026, 3, 20)},
#         ]
# }

def handle_menu(choice):
    if choice not in NAV_MENU:
        print("Invalid option, try again.")
    else:
        do_action = NAV_MENU[choice]["nav_action"]
        do_action()
        

def show_menu():
    for choice, data in NAV_MENU.items():
        nav_desc = data["nav_desc"]
        print(f"{BOLD}{choice}{RESET} - {nav_desc}")

def add_session(sess_date=None):
    print(F"\n{BOLD}{RED}================= ADD SESSION ================={RESET}")
    while True:
        sess_subject = input("Subject: ").strip().title()
        if sess_subject:
            break
        if sess_subject not in SESSION_LIST:
            SESSION_LIST[sess_subject] = []

    while True:
        raw = sess_length = input("How long was this session? (minutes): ").strip()
        if not raw:
            print("Minutes cannot be empty.")
            continue

        try:
            sess_length = int(raw)
            if sess_length <= 0:
                print("Minutes can not be less than 0.")
                continue
            break
        except ValueError:    
            print("Invalid number of minutes")
    
    if sess_date is None:
        while True:
            raw_date = input("When did this happen? (Format: MM/DD/YYYY): ")
            
            if not raw_date:
                sess_date = datetime.date.today()
                print("(No date entered - using todays' date.)")
                break
            try:
                month, day, year = map(int, sess_date.split('/'))
                sess_date = datetime.date(year, month, day)
                break
            except ValueError:
                print("[ERROR] Invalid date format. Using today as default")
    
    sess_note = input("Note (optional): ").strip()
    
    SESSION_LIST.setdefault(sess_subject,[]).append({
        "sess_length": sess_length, 
        "sess_date": sess_date,
        "sess_note": sess_note,})
    
    print("Adding Session... ", end="", flush=True)
    time.sleep(2)
    print("Session added.")
    time.sleep(2)

def view_sessions(SESSION_LIST):
    if not SESSION_LIST:
        print("No sessions currently available")
        return
    print(F"\n{BOLD}{RED}================= VIEW SESSION ================={RESET}")
    for sess_subject, data in SESSION_LIST.items():
        print(f"\n{BOLD}--- {sess_subject} ---{RESET}")
        for sdata in data:
            sess_length = sdata["sess_length"]
            sess_date = sdata["sess_date"]
            sess_date = sess_date.strftime("%m/%d/%Y")
            sess_note = sdata.get("sess_note", "")

            print(f"- {sess_subject} for {sess_length} min on {sess_date}")
            print(f"     Note: {sess_note}")

def edit_session(SESSION_LIST):
    print("\nThis feature is not yet implemented\n")
    pass

def session_stats():
    if not SESSION_LIST:
        print("\nNo sessions recorded")
        return

    most_studied_subject = None
    most_studied_minutes = 0
    least_studied_subject = None
    least_studied_minutes = float("inf")

    total_session_time = 0
    total_session_count = 0
    subject_report_lines = []
    last_session_subject = None
    last_session_date = None
    last_session_length = 0

    for sess_subject, data in SESSION_LIST.items():
        subject_session_count = 0
        subject_session_minutes = 0

        for sdata in data:
            subject_session_minutes += sdata["sess_length"]
            subject_session_count += 1
            total_session_time += sdata["sess_length"]
            total_session_count += 1

            # Track last session
            last_session_subject = sess_subject
            last_session_date = sdata["sess_date"]
            last_session_length = sdata["sess_length"]

        # Compute subject average safely
        subject_avg_sessions = (
            subject_session_minutes / subject_session_count
            if subject_session_count else 0
        )

        # Track most / least studied subjects
        if subject_session_minutes > most_studied_minutes:
            most_studied_minutes = subject_session_minutes
            most_studied_subject = sess_subject

        if subject_session_minutes < least_studied_minutes:
            least_studied_minutes = subject_session_minutes
            least_studied_subject = sess_subject

        # Add one line per subject
        subject_report_lines.append(
            f"{sess_subject:<10} | {subject_session_minutes:>4} min | "
            f"{subject_session_count:>2} sessions | avg {subject_avg_sessions:.1f} min"
        )

    # Total average
    total_session_avg = total_session_time / total_session_count if total_session_count else 0

    print(
        f"\n{BOLD}{RED}================= STUDY BOARD ================={RESET}\n\n"        
        f"TOTAL STUDY TIME: {total_session_time} minutes\n" 
        f"TOTAL SESSIONS: {total_session_count}\n"
        f"AVERAGE SESSION: {total_session_avg:.2f} min\n"
        f"MOST STUDIED SUBJECT: {most_studied_subject} ({most_studied_minutes} min)\n"
        f"LEAST STUDIED SUBJECT: {least_studied_subject} ({least_studied_minutes} min)\n\n"
        f"{BOLD}-------------- SUBJECT BREAKDOWN --------------{RESET}\n\n"
        f"{'\n'.join(subject_report_lines)}\n\n"
        f"Last session: {last_session_subject} on {last_session_date} ({last_session_length} min)\n"
    )
    time.sleep(3)

def save_file(filename, SESSION_LIST):
    try:
        with open(filename, "w") as f:
            for subject, data in SESSION_LIST.items():
                for data in data:
                    sess_length = data["sess_length"]
                    sess_date = data["sess_date"]
                    f.write(f"{subject},{sess_length},{sess_date}\n")
        print("Saving... ", end="", flush=True)
        time.sleep(2)
        print("Save successful.")
        time.sleep(1)
    except OSError as e:
        print(f"Unable to save file: {e}")

def load_file():
    pass

def quick_seed():
    SEED_LIST = SESSION_LIST

def quit():
    while True:
        confirm = input("Are you sure you want to quit? (Y/N) ").lower().strip()
        if confirm in ("y", "yes"):
            save_file(filename, SESSION_LIST)
            print("Goodbye!")
            return True

        elif confirm in ("n", "no"):
            return False

        else:
            print("Please enter yes (y) or no (n)")

NAV_MENU = {
    "1": {"nav_desc": "Add Session", "nav_action": add_session},
    "2": {"nav_desc": "Edit Session", "nav_action": lambda: edit_session(SESSION_LIST)},
    "3": {"nav_desc": "View Sessions", "nav_action": lambda: view_sessions(SESSION_LIST)},
    "4": {"nav_desc": "Session Stats", "nav_action": session_stats},
    "5": {"nav_desc": "Save File", "nav_action": lambda: save_file(filename, SESSION_LIST)},
    "6": {"nav_desc": "Quit", "nav_action": quit}
}

while True:
    if not SESSION_LIST:
        print("\nNo data yet, seeding.\n")
        SESSION_LIST = SEED_LIST
    
    show_menu()


    choice = input("Choice: ")
    handle_menu(choice)