# Shopping List Program — Overview

A command-line Python application that lets users add, remove, search, display, and save shopping list items with quantity support using file storage.

# Functions Description-

## __init__(self)
Initializes the shopping list object, creates the list container, and loads saved items from file.

## start_menu(self)
Displays the command menu showing available actions the user can perform.

## add_to_list(self, item)
Adds a new item to the shopping list or updates the quantity if the item already exists.

## parse_store_quantity(self, item)
Parses item name and quantity from user input (e.g., Milk x2 → Milk, 2).

## remove_item(self, item)
Removes an item completely or reduces its quantity if multiple exist.

## show_shopping_list(self)
Displays the current shopping list in sorted order.

## save_items(self)
Saves all shopping list items to shopping_list.txt.

## load_items(self)
Loads previously saved shopping list items from shopping_list.txt.

## clear_list(self)
Deletes the entire shopping list after user confirmation.

## search_item(self, key)
Searches and displays items matching a given keyword or substring.

## main()
Controls the main program loop, handles user input, and routes commands to appropriate functions.

## -Vimoh Sharma
