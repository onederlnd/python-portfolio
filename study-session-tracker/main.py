# main.py
from seed import SEED_LIST
from persistence import save_file, load_file
from sessions import add_session, view_sessions
from stats import session_stats

FILENAME = "sessions.json"
SESSION_LIST = load_file(FILENAME) or SEED_LIST.copy()

# --- menu mapping
MENU_LIST = {
    "1": lambda: add_session(SESSION_LIST),
    "2": lambda: view_sessions(SESSION_LIST),
    "3": lambda: session_stats(SESSION_LIST),
    "4": lambda: save_file(FILENAME, SESSION_LIST),
    "5": "quit"
}

# --- menu display
def show_menu():
    print(
        "\nchoose an option:\n"
        "1 - add session\n"
        "2 - view sessions\n"
        "3 - session stats\n"
        "4 - save sessions\n"
        "5 - quit"
    )

# --- main loop
def main():
    while True:
        show_menu()
        choice = input("> ").strip()
        if choice not in MENU_LIST:
            print("invalid option")
            continue
        if choice == "5":
            save_file(FILENAME, SESSION_LIST)
            print("goodbye!")
            break
        MENU_LIST[choice]()

if __name__ == "__main__":
    main()