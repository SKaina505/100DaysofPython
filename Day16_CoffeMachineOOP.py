from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

can_order = Menu()
give_coffe = CoffeeMaker()
money = MoneyMachine()


should_make_coffe = True

while should_make_coffe:
    choice = input(f"What would you like? ({can_order.get_items()}): ").lower()
    if choice == "off":
        should_make_coffe = False
    elif choice == "report":
        give_coffe.report()
        money.report()
    else:
        drink = can_order.find_drink(choice)
        if give_coffe.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                give_coffe.make_coffee(drink)
