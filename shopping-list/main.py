# main.py
from shopping import add_item, remove_item, view_list, search_item, clear_list
from persistence import save_file, load_file

FILENAME = "shopping_list.json"
shopping_list = load_file(FILENAME)

# --- menu options mapping
MENU_LIST = {
    "1": lambda: view_list(shopping_list),
    "2": lambda: add_item(shopping_list),
    "3": lambda: remove_item(shopping_list),
    "4": lambda: save_file(FILENAME, shopping_list),
    "5": lambda: shopping_list.update(load_file(FILENAME)),
    "6": lambda: search_item(shopping_list),
    "7": lambda: clear_list(shopping_list),
}

# --- main menu display
def show_menu():
    print(
        "\nwhat would you like to do? (choose a number)\n"
        "1 - view shopping list\n"
        "2 - add item\n"
        "3 - remove item\n"
        "4 - save list\n"
        "5 - load list\n"
        "6 - search list\n"
        "7 - clear list\n"
        "type exit to close the app\n"
    )

# --- main program loop
def main():
    while True:
        show_menu()
        command = input("> ").strip().lower()
        if command == "exit":
            save_file(FILENAME, shopping_list)
            print("goodbye!")
            break
        elif command in MENU_LIST:
            MENU_LIST[command]()
        else:
            print("invalid command")

if __name__ == "__main__":
    main()