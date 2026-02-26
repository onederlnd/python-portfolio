# Shopping List with Categories

A command-line shopping list manager that lets you organize grocery items by category and save/load them from a file.  
This tool is perfect for keeping your shopping organized and tracking items across different categories.

---

## Features

- add items with product name, category, and quantity  
- view your current shopping list grouped by category  
- remove items from the list  
- search for items by name  
- save and load shopping list to/from a file  
- clear all items for a fresh start  

---

## Getting Started

### Requirements

- python 3.8 or higher  
- works on windows, mac, and linux

### Installation

1. clone the repository:

git clone https://github.com/onederlnd/python-portfolio.git

2. navigate into the project folder:

cd shopping-list

3. run the main program:

python main.py

---

## Usage

When you run the program, you will see a menu:

choose an option:  
1 - view shopping list  
2 - add item  
3 - remove item  
4 - save list  
5 - load list  
6 - search list  
7 - clear list  
type exit to close the app

- **view shopping list** → see all items with quantity and category  
- **add item** → add a product name, category (dairy, produce, etc.), and quantity  
- **remove item** → delete a product from the list  
- **save list** → save all items to shopping_list.txt  
- **load list** → load items from shopping_list.txt  
- **search list** → search for a product by name  
- **clear list** → remove all items from the list  
- **exit** → exit the program

---

## File Structure

shopping-list/  
├─ main.py        # main program loop and menu  
├─ shopping_list.txt  # saved shopping list file (created automatically)  

---

## Contributing

This project is self-contained for personal use, but contributions are welcome:

- add categories management  
- improve search functionality (partial matches, case-insensitive)  
- enhance CLI experience with colors or menus  
- export list to csv for easy printing or sharing  

---

## License

MIT License