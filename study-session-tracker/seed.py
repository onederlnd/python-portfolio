# seed.py
import datetime

# --- seed data for initial sessions
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