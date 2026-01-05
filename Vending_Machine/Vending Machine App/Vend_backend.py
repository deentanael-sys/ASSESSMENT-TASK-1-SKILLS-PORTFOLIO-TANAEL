import time


#shows the list of products with prodcut title code and price(DONE)
# asks the user for the product code(DONE)
# User enters product code it automatically goes to the cart and adds the item price to the balance(DONE)
# asks if the user wants to purchase another item and adds another (DONE)
# and if user types exit, it ends the transaction and returns the balance (DONE)
# if the item is out of stock, it notifies the user and asks for another selection ()
# returns change if there is any left after the transaction ()
#add menu at start with options to vend item, restock items, exit program ()
# then you can insert money

items = {
        'A1': {'name': "Fred's Eyeball", 'price': 5.50, 'stock': 2},
        'A2': {'name': "Quandale's Dingle", 'price': 10.00, 'stock': 1},
        'A3': {'name': "Legendary Hero", 'price': 2.75, 'stock': 8},
        'A4': {'name': "Diamond Pickaxe", 'price': 7.00, 'stock': 3},
        'B1': {'name': "Zenyatta's Orb", 'price': 1.50, 'stock': 10},
        'B2': {'name': "Spiky Blue Shell", 'price': 2.25, 'stock': 6},
        'B3': {'name': "Companion Cube", 'price': 2.50, 'stock': 4},
        'B4': {'name': "Pokeballs", 'price': 4.00, 'stock': 24},
        'C1': {'name': "Crowbar", 'price': 1.75, 'stock': 3},
        'C2': {'name': "Web Shooters", 'price': 6.25, 'stock': 4},
        'C3': {'name': "A Frying Pan", 'price': 3.50, 'stock': 1},
        'C4': {'name': "Holy Hand Grenades", 'price': 4.00, 'stock': 5},
    }
total_price = 0.0

def transaction(x=float(input('How much do you have?'))):
    change = x-total_price 
    if change >= 0:
        print(f"items dispensed, your change is {change}")
    else:
        print('you dont have enough money, items returned')

def restock():
    items = {
        'A1': {'name': "Fred's Eyeball", 'price': 5.50, 'stock': 2},
        'A2': {'name': "Quandale's Dingle", 'price': 10.00, 'stock': 1},
        'A3': {'name': "Legendary Hero", 'price': 2.75, 'stock': 8},
        'A4': {'name': "Diamond Pickaxe", 'price': 7.00, 'stock': 3},
        'B1': {'name': "Zenyatta's Orb", 'price': 1.50, 'stock': 10},
        'B2': {'name': "Spiky Blue Shell", 'price': 2.25, 'stock': 6},
        'B3': {'name': "Companion Cube", 'price': 2.50, 'stock': 4},
        'B4': {'name': "Pokeballs", 'price': 4.00, 'stock': 24},
        'C1': {'name': "Crowbar", 'price': 1.75, 'stock': 3},
        'C2': {'name': "Web Shooters", 'price': 6.25, 'stock': 4},
        'C3': {'name': "A Frying Pan", 'price': 3.50, 'stock': 1},
        'C4': {'name': "Holy Hand Grenades", 'price': 4.00, 'stock': 5},
    }    
    return items

def vend_item():
    global total_price
    print ("Available items:")
    time.sleep(1)
    for name, item in items.items():
        print(f"{name}: {item['name']} - ${item['price']} (Stock: {item['stock']})")
    
    print("\n")
    cart = input("Enter the product code of the item you want to purchase: \nType 'exit' to exit'").upper()

    if cart == 'A1' in items:
        items['A1'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item()
    
    elif cart == 'A2' in items:
        items['A2'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item()  
    
    elif cart == 'A3' in items:
        items['A3'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item()
    
    elif cart == 'A4' in items:
        items['A4'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item()
    
    
    elif cart == 'B1' in items:
        items['B1'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item(), total_price
    
    elif cart == 'B2' in items:
        items['B2'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item()
    
    elif cart == 'B3' in items:
        items['B3'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item()
    
    elif cart == 'B4' in items:
        items['B4'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item()
    
    elif cart == 'C1' in items:
        items['C1'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item()
    
    elif cart == 'C2' in items:
        items['C2'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item()
    
    elif cart == 'C3' in items:
        items['C3'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item()
    
    elif cart == 'C4' in items:
        items['C4'] ['stock'] -=1
        total_price += items[cart]['price']
        time.sleep(1)
        print(f"You selected {items[cart]['name']} for ${total_price:.2f}.")
        return vend_item()
    
    elif cart == 'EXIT':
        time.sleep(1)
        print(f"Transaction ended. Your total balance is ${total_price:.2f}")
        time.sleep(.5)
        print(f"Checking...")
        time.sleep(1.5)
        transaction()
    
    elif cart == 'RESTOCK':
        time.sleep(1)
        print(f"Restocking Items")
        time.sleep(2)
        restock()
        print(f"Items Restocked")

    else:
        print("Invalid product code. Please try again.")
        time.sleep(1)
        return vend_item()
    

          
vend_item()