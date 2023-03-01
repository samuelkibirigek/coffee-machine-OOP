class Money:
    def __init__(self):
        self.money = 0
        self.quater = int(input("How many quaters:"))
        self.dimes = int(input("How many dimes:"))
        self.nickel = int(input("How many nickels:"))
        self.pennies = int(input("How many pennies:"))

    def coins(self):
        self.money = ((self.quater * 0.25) + (self.dimes * 0.10) + (self.nickel * 0.05) + (self.pennies * 0.01))


