"""
Pet Store Shopping System:

This Python program simulates a basic pet store shopping system. It is composed of two classes:

PetItem: Represents a pet item with attributes such as title, cost, and count.
Basket: Represents a basket that allows users to add, remove, and view pet items.
"""

# Define a class to represent a pet item
class PetItem:
    def __init__(self, title, cost):
        self.title = title
        self.cost = cost
        self.count = 1

    def __str__(self):
        return f"{self.title} (Count: {self.count}) - £{self.cost:.2f}"

# Define a class to represent a basket
class Basket:
    def __init__(self):
        self.basket = []    # List to store items in the basket
        self.costs = []  # List to store costs for each item in the basket

    def add_to_basket(self, item, count):
        # Check if the item is already in the basket
        basket_item = next((basket_item for basket_item in self.basket if basket_item.title == item.title), None)
        if basket_item:
            # If the item is in the basket, update the count
            basket_item.count += count
            print(f"Added {count} more '{item.title}' to your basket.")
        else:
            # If the item is not in the basket, add it
            item.count = count
            self.basket.append(item)
            print(f"Added {count} {item.title} to your basket.")
            self.costs.extend([item.cost] * count)

    def remove_from_basket(self, item_title, count_to_remove=None):
        # Find the item in the basket based on the item title
        item = next((basket_item for basket_item in self.basket if basket_item.title.lower() == item_title.lower()), None)
        if item:
            # If a specific count is provided, remove that count; otherwise, remove all
            if count_to_remove is None or count_to_remove >= item.count:
                self.basket.remove(item)
                self.costs.remove(item.cost * item.count)
                print(f"Removed all '{item.title}' from your basket.")
            else:
                item.count -= count_to_remove
                print(f"Removed {count_to_remove} '{item.title}' from your basket.")
        else:
            print(f"'{item_title}' not found in your basket.")

    def view_basket(self):
        if not self.basket:
            print("Your basket is empty.")
        else:
            print("\nYour Shopping Basket:")
            # Calculate the total cost and display each item in the basket
            total_cost = sum(item.cost * item.count for item in self.basket)
            for item in self.basket:
                print(item)
            print(f"\nTotal cost: £{total_cost:.2f}")

    def display_available_items(self):
        print("\nAvailable Items:")
        # Define available items using a dictionary
        items = {
            "1": PetItem("Dog Chow", 20.99),
            "2": PetItem("Kitty Toy", 8.50),
            "3": PetItem("Bird House", 35.75),
        }
        # Display available items with corresponding keys
        for key, item in items.items():
            print(f"{key}. {item.title} - £{item.cost:.2f}")
        return items

# Sample Usage
basket = Basket()

while True:
    print("\nOptions:")
    print("1. Add item to basket")
    print("2. Remove item from basket")
    print("3. View basket")
    print("4. Checkout and exit")

    option = input("Enter your option (1-4): ")

    if option == "1":
        # Allow the user to add items to the basket
        available_items = basket.display_available_items()
        item_option = input("Enter the number of the item you want to add to your basket: ")
        if item_option in {"1", "2", "3"}:
            quantity = input(f"Enter the count for {available_items[item_option].title}: ")
            if quantity.isdigit():
                basket.add_to_basket(available_items[item_option], int(quantity))
            else:
                print("Invalid quantity. Please enter a valid number.")
        else:
            print("Invalid item option. Please enter a number between 1 and 3.")

    elif option == "2":
        # Allow the user to remove items from the basket
        item_title = input("Enter the title of the item to remove: ").lower()
        item_in_basket = next((item for item in basket.basket if item.title.lower() == item_title.lower()), None)
        if item_in_basket:
            if item_in_basket.count > 1:
                print(f"There are {item_in_basket.count} '{item_in_basket.title}' in your basket.")
                try:
                    remove_option = input("Do you want to remove 1 (Enter '1'), all ("
                                          "Enter 'all'), or enter a specific number?: ")
                    if remove_option.lower() == "all":
                        basket.remove_from_basket(item_title)
                    elif remove_option.isdigit():
                        count_to_remove = int(remove_option)
                        basket.remove_from_basket(item_title, count_to_remove)
                    else:
                        print("Invalid input. No items removed.")
                except ValueError:
                    print("Invalid input. No items removed.")
            else:
                basket.remove_from_basket(item_title)
        else:
            print(f"'{item_title}' not found in your basket.")

    elif option == "3":
        # Display the contents of the basket
        basket.view_basket()

    elif option == "4":
        # Checkout and exit the program
        print(f"\nThank you for shopping with Pet Store!")
        break

    else:
        # Handle invalid options
        print("Invalid option.")
