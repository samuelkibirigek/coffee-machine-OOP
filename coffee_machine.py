class Machine:
    def __init__(self):
        self.MENU = {
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

        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

        self.profit = 0
        self.choice = input("What coffee would you like please: \n").lower()

    def turn_off_machine(self):
        quit()

    def report(self):
            print(f'Water: {self.resources["water"]}\n'
                  f'Milk: {self.resources["milk"]}\n'
                  f'Coffee: {self.resources["coffee"]}\n'
                  f'Profit:{self.profit}')

    def sufficient(self):
        for coffee in self.MENU:
            if self.choice == coffee:
                for ing in self.MENU[self.choice]["ingredients"]:
                    if ing in self.resources:
                        try:
                            assert self.MENU[self.choice]["ingredients"][ing] <= self.resources[ing]
                        except AssertionError:
                            print("Sorry,Ingredients not enough.")
                            break


