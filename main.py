from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

while machine_is_on:
    choice = input(f"What would you like? ({menu.get_items()}):\n").lower()

    for item in menu.menu:
        if choice == item.name:
            drink = menu.find_drink(choice)
            if money.make_payment(drink.cost):
                if coffee.is_resource_sufficient(drink):
                    coffee.make_coffee(drink)

    if choice == "report":
        coffee.report()

    elif choice == "off":
        machine_is_on = False

    elif choice == "profit":
        money.report()

    else:
        print("Please order for one of the available coffee types!")
        continue
