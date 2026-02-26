# Shopping List with Categories
# 
# A command-line shopping list manager that allows users to organize grocery items
# by category and save/load them from a file.
# 
# ---
# 
import os
import sys

filename = "shopping_list.txt"
shopping_list = {}

def handle_command(menu_list):
    for option in menu_list:
        option
def clear():
    """ clear all items"""
    shopping_list.clear()
def add_item():
    product = input("Product name: ")
    category = input("Category (dairy, produce, etc): ")
    quantity = input("How many? ")

    shopping_list[product] = {"category": category, "quantity": quantity}
    return shopping_list
    
def remove_item():
    """ remove item """
    product = input("Which item do you want to delete? ")
    shopping_list.pop(product)
    print(f"{product} has been deleted!")
def search():
    """ search and find items"""
    search_item = input("Search for: ")
    print("YOU'RE SEARCHING FOR: ", search_item)
    if search_item in shopping_list:
        print(f"search found! {search_item}")
    else:
        print("no item found")
def view_list(shopping_list):
    """ show current shopping list """

    print("Current shopping list:")

    for product, data in shopping_list.items():
        quantity = data["quantity"]
        category = data["category"]
        print(f"{quantity} - {product} ({category})")

    if not shopping_list:
        print("Your shopping list is empty!")

def save_file(filename):
    """ saves a shopping list """
    try:
        with open(filename, "w") as f:
            f.write(str(shopping_list))
            print("Shopping list saved!")
    except Exception as e:
        print(f"[ERROR] Unable to save file: {e} ")

# - Load list from file
def load_file(filename):
    """ load a shopping list file """
    try:
        with open(filename, "r") as f:
            shopping_list = f.readlines()
            return shopping_list
    except Exception as e:
            print(f"[ERROR] Unable to save file: {e} ")

def main():
    print("What would you like to do? (Choose a number)\n" \
    "1 - View shopping list\n" \
    "2 - Add item\n" \
    "3 - Remove item\n" \
    "4 - Save list\n" \
    "5 - Load list\n" \
    "6 - Search list\n" \
    "7 - Clear list\n" \
    "Type exit to close the app"
    )

menu_list = {
    "1": lambda: view_list(shopping_list),
    "2": lambda: add_item(),
    "3": lambda: remove_item(),
    "4": lambda: save_file(filename),
    "5": lambda: load_file(filename),
    "6": lambda: search(),
    "7": lambda: clear(),
}
while True:
    """"""
    main()
    command = input("> ")
    if command == "exit":
        print("Goodbye!")
        exit()
    if command in menu_list:
        menu_list[command]()
    else:
        print("Invalid command")
