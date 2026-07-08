inventory = [("Pen",5,100) , ("Bag",300,20), ("Book",80,50)]

print("===== INVENTORY =====")

def stock_value():
     total = 0
     for item,price,quantity in inventory:
        total += price * quantity
     return total

    
def expensive_item():
    name = ""
    expensive_price = 0
    for item, price , quantity in inventory:
        if price > expensive_price:
            name = item
            expensive_price = price
    print(f"{name} : {expensive_price}")

def print_items():
    sorted_inventory = sorted(inventory,key=lambda x:x[1])
    for item, price, quantity in sorted_inventory:
        print(f"{item} {price} {quantity} ")

