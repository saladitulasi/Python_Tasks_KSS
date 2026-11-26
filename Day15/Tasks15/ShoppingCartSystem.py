# Shopping cart
cart = []

# Item prices
prices = {
    "apple": 20,
    "banana": 10,
    "milk": 30,
    "bread": 25
}

try:
    n = int(input("Enter number of items: "))

    for i in range(n):
        item = input("Enter item name: ").lower()
        cart.append(item)

    # Remove duplicate items
    unique_cart = set(cart)

    print("\nShopping Cart:", unique_cart)

    total = 0

    # Calculate total cost
    for item in unique_cart:
        if item in prices:
            total += prices[item]
        else:
            print(item, "is not available")

    print("\nTotal Cost: Rs.", total)

except ValueError:
    print("Invalid input! Please enter a valid number.")

except Exception as e:
    print("Error:", e)