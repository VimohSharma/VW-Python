#Vimoh Sharma
# A Command Line Shopping List Program with Add, Delete, Display functionalities.
class ShoppingList:
    def __init__(self):
        self.items = []
        self.load_items()

    def start_menu(self):
        print("\nWhat would you like to access today- ")
        print("Enter the item you would like to add: ")
        print("type 'SHOW' to show list of items")
        print("type 'HELP' for the help menu.")
        print("type 'CLEAR' to delete your entire shopping list.")
        print("type 'SEARCH' to search for items")
        print("type 'REMOVE' to remove items")
        print("type 'DONE' to save and exit!")

    def add_to_list(self, item):
        item=item.strip()
        if not item:
            print("Cannot add an empty item, try again.")
            return

        name,qty=self.parse_store_quantity(item)
        for item,existing in enumerate(self.items):
            existing_name, existing_qty = self.parse_store_quantity(existing)
            if existing_name==name:
                new_qty=existing_qty+qty
                self.items[item]=f"{name} x{new_qty}"
                print(f"{name} quantity updated to {new_qty}")
                return


        if qty>1:
            self.items.append(f"{name} x{qty}")
        else:
            self.items.append(name)

    def parse_store_quantity(self,item):
        item=item.strip()
        if "x" in item.lower():
            name,qty=item.lower().split("x")
            name=name.strip().capitalize()
            qty=int(qty.strip())
        else:
            name=item.capitalize()
            qty=1
        return name,qty

    def remove_item(self,item):
        item = item.strip()
        if not item:
            print("Enter a valid item, try again.")
            return

        name, qty = self.parse_store_quantity(item)
        for item, existing in enumerate(self.items):
            existing_name, existing_qty = self.parse_store_quantity(existing)
            if existing_name == name:
                if existing_qty>qty:
                    new_qty = existing_qty - qty
                    self.items[item] = f"{name} x{new_qty}"
                    print(f"{name} quantity reduced to {new_qty}")
                else:
                    self.items.pop(item)
                    print(f"{name} removed from the list.")
                return
        print(f"{name} not found in the list.")

    def show_shopping_list(self):
        print("\nyour current Shopping List looks like:")

        if not self.items:
            print([])
            print("First you have to add something to see your List!")
        else:
            for item in sorted(self.items):
                print(f"- {item}")

    def save_items(self):
        with open("shopping_list.txt","w") as file:
            for item in self.items:
                file.write(item + "\n")

    def load_items(self):
        try:
            with open("shopping_list.txt","r") as file:
                self.items = [line.strip() for line in file]
        except FileNotFoundError:
            self.items=[]

    def clear_list(self):
        confirmation=input("Are you sure you want to delete your list? (Y/N): ")

        if confirmation.upper() == "Y":
            self.items.clear()
            print("shopping list deleted.")
        else:
            print("deletion aborted.")

    def search_item(self,key):
        key=key.lower()

        found=[item for item in self.items if key in item.lower()]

        if found:
            print("Found items: ")
            for item in found:
                print(f"- {item}")
        else:
            print("No matching items found.")

def main():
    obj=ShoppingList()

    while True:
        obj.start_menu()
        try:
            wish=input("> ").strip()
            if not wish:
                print("Enter a Valid command or an item.")
                continue
            wish=wish.strip()
        except (EOFError,KeyboardInterrupt):
            obj.save_items()
            print("\nYour shopping list was preserved.")
            break

        if wish.upper() == "DONE":
            obj.save_items()
            print("Goodbye, Thanks for your time!")
            break

        elif wish.upper() == "REMOVE":
            obj.show_shopping_list()
            item=input("Enter the item you want to remove: ")
            obj.remove_item(item)

        elif wish.upper() == "SHOW":
            obj.show_shopping_list()

        elif wish.upper() =="HELP":
            obj.start_menu()

        elif wish.upper() =="CLEAR":
            obj.clear_list()

        elif wish.upper() =="SEARCH":
            key=input("Enter a substring, You want to search off of: ")
            obj.search_item(key)

        else:
            obj.add_to_list(wish)


if __name__=="__main__":
    main()