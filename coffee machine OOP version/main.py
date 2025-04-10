from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    # Create an item list of items with sufficient resources, so user can know available items
    item_list = menu.get_items()
    items = []
    for item in item_list.split('/'):
        coffee = menu.find_drink(item)
        if coffee_maker.is_resource_sufficient(coffee):
            items.append(item)

    def pick_coffee():
        global is_on, coffee
        choice = input(f"What coffee  would you like? {'/'.join(items)}: ")
        coffee = menu.find_drink(choice)
        if choice == 'off':
            is_on = False
        elif choice == "report":
            print(coffee_maker.report())
            pick_coffee()
        elif choice not in items:
            print('wrong choice')
            pick_coffee()
        elif choice in items:
            def calculate_money():
                if coffee_maker.is_resource_sufficient(coffee):
                    coffee_cost = money_machine.make_payment(coffee.cost)
                    if coffee_cost == 'True':
                        coffee_maker.make_coffee(coffee)
                    elif coffee_cost == "add":
                        coffee_cost = money_machine.add_money(coffee.cost)
                        if coffee_cost == 'True':
                            coffee_maker.make_coffee(coffee)
                        else:
                            calculate_money()
                    elif coffee_cost == "refund":
                        money_machine.refund()
                    elif coffee_cost == "pick":
                        pick_coffee()

            calculate_money()

    # while there's still sufficient resources for at least one coffee, the machine keeps running
    if len(items) != 0:
        pick_coffee()

    else:
        print('We are out of stock')
        if money_machine.change == 0:
            exit()
        else:
            print(f'Collect your ${money_machine.change} balance.')
            exit()
