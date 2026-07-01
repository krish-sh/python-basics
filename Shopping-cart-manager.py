cart = []
prices = {}

print("===== ENTER CART ITEMS =====")
user = input("For adding items to cart, enter Add: ")

def add_item(item, price):
    cart.append(item)
    prices[item] = price

def show_Cart():
    print('\n ===== CART =====')
    for i, item in enumerate(cart, 1):
        print(f'{i} {item}: Rs{prices[item]}') 
    total = sum(prices[i] for i in cart)
    print("Total: ", total)
    print("After adding GST:", total + (total * 0.18))  

if user.lower() == "add":
    print("Enter item name (or type 'done' to finish):")
    while True:
        item = input("Enter item name: for addding or type 'done' to finish: ")
        if item.lower() == 'done':
            show_Cart()
            break
        price = float(input("Enter item price: "))
        add_item(item, price )
else:
    print("Enter valid input")