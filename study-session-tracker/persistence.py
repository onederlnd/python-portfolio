# persistence.py
import json
import datetime

# --- save and load sessions

def save_file(filename, data):
    """save session data as json"""
    try:
        with open(filename, "w") as f:
            json.dump(data, f, default=str, indent=4)
        print("save successful")
    except Exception as e:
        print(f"[error] unable to save file: {e}")

def load_file(filename):
    """load session data from json"""
    try:
        with open(filename) as f:
            data = json.load(f)
            # convert date strings back to datetime.date
            for subject, sessions in data.items():
                for s in sessions:
                    s["sess_date"] = datetime.datetime.strptime(s["sess_date"], "%Y-%m-%d").date()
            return data
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"[error] unable to load file: {e}")
        return {}