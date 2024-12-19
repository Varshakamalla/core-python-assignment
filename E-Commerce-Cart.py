def calculate_total_price(cart_items):
    if not cart_items:
        return "The cart is Empty"
    total_price=sum(cart_items.values())
    if len(cart_items)>5:
        discount=total_price*(10/100)
        total_price-=discount
    return total_price
def get_cart_items():
    cart_items={}
    n=int(input("Enter the Number of items in the cart : "))
    for _ in range(n):
        item_name=input("Enter item name : ")
        item_price = float(input(f"Enter price for {item_name}: "))
        cart_items[item_name] = item_price
        return cart_items

cart_items = get_cart_items()
total_price = calculate_total_price(cart_items)
print(f"Total Price: {total_price}")