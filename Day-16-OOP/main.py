from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_payment = MoneyMachine()

choice = ""
while choice != "off":
    choice = input(f"What would you like to have ({menu.get_items()})?")
    if choice == 'report':
        coffee_maker.report()
        money_payment.report()
    else:
        menu_item = menu.find_drink(choice)
        if menu_item:
            if coffee_maker.is_resource_sufficient(menu_item):
                money_payment.make_payment(menu_item.cost)
                coffee_maker.make_coffee(menu_item)

