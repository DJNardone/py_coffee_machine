from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

bev_menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()
machine_on = True
while machine_on:
    items = bev_menu.get_items()
    choice = input(f"What would you like? ({items}): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        maker.report()
        money.report()
    else:
        beverage = bev_menu.find_drink(choice)
        if maker.is_resource_sufficient(beverage):
            if money.make_payment(beverage.cost):
                maker.make_coffee(beverage)