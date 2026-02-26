# persistence.py
import json

# --- save and load shopping list

def save_file(filename, data):
    """save shopping list as json"""
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("shopping list saved!")
    except Exception as e:
        print(f"[ERROR] unable to save file: {e}")

def load_file(filename):
    """load shopping list from json"""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"[ERROR] unable to load file: {e}")
        return {}