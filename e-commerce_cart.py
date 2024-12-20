def calculate_total(cart_items):
    if len(cart_items) == 0:
        return "Your cart is empty"
    total = 0
    for price in cart_items.values():
        total += price
    if len(cart_items) > 5:
        total = total * 0.9
    return f"Total Price: {total}"
cart_items = {
               'Laptop': 50000,
               'Headphones': 2000,
               'Mouse': 500, 
               'Keyboard': 1500
             }
print(calculate_total(cart_items))
