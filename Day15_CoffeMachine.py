from idlelib.mainmenu import menudefs

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

profit = 0
is_on = True

def process_coin():
    print("Please insert coins. ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def is_resources_enough(order_ingredients):
    for item in order_ingredients:
        order_ingredients[item] >= resources[item]
        print(f"Sorry there is not enough {item}.")
        return False
    return True

def make_coffe(drink_name, order_ingredients):
    print("true")
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}")


while is_on == True:
    user_request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_request == "off":
        is_on = False
    elif user_request == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_request]
        if is_resources_enough(drink["ingredient"]):
            payment = process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(user_request,drink["ingredients"])

