## **Pet Store Shopping System**

This Python program simulates a basic pet store shopping system. It is composed of two classes:

- **PetItem**: Represents a pet item with attributes such as title, cost, and count.
- **Basket**: Represents a basket that allows users to add, remove, and view pet items.

### **PetItem Class**

The `PetItem` class represents a pet item with the following attributes:
- `title`: The name of the pet item.
- `cost`: The cost of the pet item.
- `count`: The quantity of the pet item.

The `PetItem` class has the following methods:
- `__init__(self, title, cost)`: Initializes a new instance of the `PetItem` class.
- `__str__(self)`: Returns a string representation of the `PetItem` instance.

### **Basket Class**

The `Basket` class represents a shopping basket. It has the following attributes:
- `basket`: A list to store `PetItem` instances.
- `costs`: A list to store the costs for each `PetItem` in the basket.

The `Basket` class has the following methods:
- `__init__(self)`: Initializes a new instance of the `Basket` class.
- `add_to_basket(self, item, count)`: Adds a specified quantity of a `PetItem` to the basket or updates the quantity if the item is already present.
- `remove_from_basket(self, item_title, count_to_remove=None)`: Removes a specified quantity of a `PetItem` from the basket or removes the item entirely if no quantity is specified.
- `view_basket(self)`: Displays the contents of the basket and calculates the total cost.
- `display_available_items(self)`: Displays a list of available pet items for users to choose from.

### **Sample Usage**

The program provides a sample usage section where users can interact with the shopping basket through a menu:
1. Add item to basket
2. Remove an item from a basket
3. View basket
4. Checkout and exit

Users can select options, input item quantities, and manage their shopping basket until they choose to checkout and exit the program. The program handles invalid options and provides feedback to the user accordingly.

This program is designed to showcase a basic understanding of classes, methods, user input handling, and simple interaction with a shopping basket system.
