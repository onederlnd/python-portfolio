# shopping.py
from utils import get_nonempty_string, get_positive_int

# --- shopping list functions

def add_item(shopping_list):
    """add an item to the shopping list"""
    product = get_nonempty_string("product name: ")
    category = get_nonempty_string("category (dairy, produce, etc): ")
    quantity = get_positive_int("how many? ")

    shopping_list[product] = {"category": category, "quantity": quantity}
    print(f"{product} added to shopping list")

def remove_item(shopping_list):
    """remove an item from the shopping list"""
    product = get_nonempty_string("which item do you want to delete? ")
    if product in shopping_list:
        shopping_list.pop(product)
        print(f"{product} has been deleted!")
    else:
        print(f"{product} not found in shopping list")

def view_list(shopping_list):
    """display the current shopping list"""
    if not shopping_list:
        print("your shopping list is empty!")
        return

    print("current shopping list:")
    for product, data in shopping_list.items():
        print(f"{data['quantity']} - {product} ({data['category']})")

def search_item(shopping_list):
    """search for an item in the shopping list"""
    query = get_nonempty_string("search for: ")
    found = [p for p in shopping_list if query.lower() in p.lower()]
    if found:
        print("search results:")
        for p in found:
            data = shopping_list[p]
            print(f"{data['quantity']} - {p} ({data['category']})")
    else:
        print("no items found")

def clear_list(shopping_list):
    """clear all items from the shopping list"""
    shopping_list.clear()
    print("shopping list cleared")