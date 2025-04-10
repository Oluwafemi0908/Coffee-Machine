class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0
        self.options = ''
        self.change = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.options = ''
        if self.money_received == 0:
            self.process_coins()
            self.make_payment(cost)
        elif self.money_received < cost:
            self.options = ''
            self.options = input("Sorry that's not enough money. Do you want to add more money, pick another coffee "
                                 "or be refunded?: ").lower()
            return self.options
        elif self.money_received >= cost:
            self.options = ''
            self.change = round(self.money_received - cost, 2)
            print(f"You have {self.CURRENCY}{self.change} in change.")
            self.profit += cost
            self.money_received = self.change
            self.options = 'True'
            return self.options
        print(self.options)
        return self.options

    def add_money(self, cost):
        self.process_coins()
        self.make_payment(cost)
        return self.options

    def refund(self):
        print(f"You have been refunded ${self.money_received}.")
        self.money_received = 0
