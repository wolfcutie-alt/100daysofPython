import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def getOrder():
    order = input("What would you like? Espresso, Latte or Cappuccino? ").lower()
    
    return order

def report(resources):
    print(f"""
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${round(resources["money"], 2)}
""")
    
def checkValidOrder(water, milk, coffee, amount, price, order):
    if water > resources["water"] or milk > resources["milk"] or coffee > resources["coffee"]:
        print("Sorry there is not enough resource")
    elif amount < price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = price - amount
        
        if change > 0:
            print(f"Order successed. Here is ${change} in change.")
        else:
            print("Order successed!!!")
        
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        resources["money"] += amount
         
                
        print(f"Here is your {order}. Enjoy!")
            
def insertCoin():
    quarter = int(input("Quater: "))
    dime = int(input("Dime: "))
    nickle = int(input("Nickle: "))
    penny = int(input("Penny: "))
    return quarter * 0.25 + dime * 0.1 + nickle * 0.05 + penny * 0.01

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
resources.update({"money": 0})
    
while True:
    request = input("""
******** Start App ********

1. Type 'order' to place order
2. Type 'report' to get report
3. Type 'off' to turn off

***************************
""").lower()
    
    if request == "order":
        order = getOrder()
        coin = insertCoin()
        espressoDetail = MENU["espresso"]
        latteDetail = MENU["latte"]
        cappuccinoDetail = MENU["cappuccino"]
        espressoDetail["ingredients"].update({"milk": 0})
        
        if order == "espresso":
            checkValidOrder(espressoDetail["ingredients"]["water"], espressoDetail["ingredients"]["milk"], espressoDetail["ingredients"]["coffee"], coin, espressoDetail["cost"], order)
        elif order == "latte":
            checkValidOrder(latteDetail["ingredients"]["water"], latteDetail["ingredients"]["milk"], latteDetail["ingredients"]["coffee"], coin, latteDetail["cost"], order)
        elif order == "cappuccino":
            checkValidOrder(cappuccinoDetail["ingredients"]["water"], cappuccinoDetail["ingredients"]["milk"], cappuccinoDetail["ingredients"]["coffee"], coin, cappuccinoDetail["cost"], order)
        
        continue_order = input("Anything else: ").lower()
        
        if continue_order == "yes":
            clear()
        else:
            continue
        
    elif request == "report":
        report(resources)
        continue
    
    elif request == "off":
        break
