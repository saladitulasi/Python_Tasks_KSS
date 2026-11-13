
# Small Shop Purchase Management System

# Dictionary to store product names and prices
products = {
    "Pen": 10,
    "Book": 50,
    "Pencil": 5,
    "Bag": 500,
    "Bottle": 100
}

# List to store cart items
cart = []

# Set to store product categories
categories = {"Stationery", "Accessories", "School Supplies"}

# Tuples to store product details (name, price, category)
product_details = (
    ("Pen", 10, "Stationery"),
    ("Book", 50, "Stationery"),
    ("Pencil", 5, "Stationery"),
    ("Bag", 500, "Accessories"),
    ("Bottle", 100, "School Supplies")
)


# Function to display available products
def display_products():
    print("\n----- AVAILABLE PRODUCTS -----")

    for name, price, category in product_details:
        print("Product:", name)
        print("Price: Rs.", price)
        print("Category:", category)
        print("------------------------")


# Function to add items to cart
def add_to_cart():
    try:
        name = input("Enter product name: ")

        if name not in products:
            raise NameError("Product does not exist!")

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        # Store product name, price and quantity in cart
        cart.append((name, products[name], quantity))

        print(name, "added to cart successfully!")

    except ValueError:
        print("Error: Please enter a valid positive quantity.")

    except NameError as e:
        print("Error:", e)


# Recursive function to calculate total price
def calculate_total(items):
    if not isinstance(items, list):
        raise TypeError("Cart must be a list.")

    if len(items) == 0:
        return 0

    item = items[0]

    if not isinstance(item, tuple):
        raise TypeError("Cart items must be tuples.")

    name, price, quantity = item

    if not isinstance(price, (int, float)) or not isinstance(quantity, int):
        raise TypeError("Invalid data type in cart.")

    return (price * quantity) + calculate_total(items[1:])


# Function to display cart and calculate bill
def calculate_bill():
    try:
        if len(cart) == 0:
            print("Your cart is empty!")
            return

        print("\n--------- CUSTOMER BILL ---------")

        for name, price, quantity in cart:
            print(name, "x", quantity, "=", price * quantity)

        total = calculate_total(cart)

        print("---------------------------------")
        print("Total Bill: Rs.", total)

    except TypeError as e:
        print("Error:", e)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


# Main menu
while True:
    print("\n===== SMALL SHOP MANAGEMENT =====")
    print("1. Display Products")
    print("2. Add Item to Cart")
    print("3. Calculate Total Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            calculate_bill()

        elif choice == 4:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")

    except ValueError:
        print("Error: Please enter a valid menu choice.")

    except ZeroDivisionError:
        print("Error: Calculation error.")

    except TypeError:
        print("Error: Incorrect data type.")

