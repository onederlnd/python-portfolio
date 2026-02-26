# sessions.py
from utils import get_positive_int, parse_date

# --- session management functions

def add_session(session_list):
    """add a new session"""
    subject = input("subject: ").strip().title()
    if subject not in session_list:
        session_list[subject] = []

    length = get_positive_int("how long was this session? (minutes): ")
    raw_date = input("when did this happen? (mm/dd/yyyy): ")
    date = parse_date(raw_date)
    note = input("note (optional): ").strip()

    session_list[subject].append({
        "sess_length": length,
        "sess_date": date,
        "sess_note": note
    })
    print("session added\n")

def view_sessions(session_list):
    """display all sessions"""
    if not session_list:
        print("no sessions currently available")
        return

    print("current sessions:")
    for subject, sessions in session_list.items():
        print(f"\n--- {subject} ---")
        for s in sessions:
            print(f"{s['sess_length']} min on {s['sess_date'].strftime('%m/%d/%Y')} - {s.get('sess_note','')}")