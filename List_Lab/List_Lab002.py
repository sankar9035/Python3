#A real-world shopping cart. Items are added/removed dynamically, and the cart computes the total price using list comprehension.
# Shopping cart using a list of tuples (item, price)

cart = []

def add_item(name, price):
    cart.append((name, price))
    print(f"Added: {name} — ₹{price}")

def remove_item(name):
    cart[:] = [(n, p) for n, p in cart if n != name]

def total():
    return sum(p for _, p in cart)

add_item("Laptop", 75000)
add_item("Mouse", 1200)
add_item("Keyboard", 3500)
remove_item("Mouse")

print(f"Cart: {cart}")
print(f"Total: ₹{total()}")
