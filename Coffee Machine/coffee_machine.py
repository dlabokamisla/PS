from types_of_coffee import MENU, resources

money_value = 0
list_resources = []
list_costs = []
for key in resources.keys():
    list_resources.append(key)
water = list_resources[0].title()
milk = list_resources[1].title()
coffee = list_resources[2].title()
money = "Money"

for value in resources.values():
    list_costs.append(value)
water_value = list_costs[0]
milk_value = list_costs[1]
coffee_value = list_costs[2]


def check_resources_sufficient():
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if water_value < espresso_water or water_value < latte_water or water_value < cappuccino_water:
            print("Sorry, there's not enough water.")
            return False
        elif coffee_value < espresso_coffee or coffee_value < latte_coffee or coffee_value < cappuccino_coffee:
            print("Sorry, there's not enough coffee.")
            return False
        elif milk_value < latte_milk or milk_value < cappuccino_milk:
            print("Sorry, there's not enough milk.")
            return False
        else:
            return True
    else:
        return True


def process_coins():
    print("Please insert coins.\n")
    user_quarters = int(input("how many quarters? "))
    quarters = user_quarters * 0.25
    user_dimes = int(input("how many dimes? "))
    dimes = user_dimes * 0.10
    user_nickels = int(input("how many nickels? "))
    nickels = user_nickels * 0.05
    user_pennies = int(input("how many pennies? "))
    pennies = user_pennies * 0.01
    user_money = quarters + dimes + nickels + pennies
    return round(user_money, 2)


def check_transaction(sum_money):
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if sum_money < espresso_cost or sum_money < latte_cost or sum_money < cappuccino_cost:
            return "Sorry, that's not enough money. Money refunded."
        elif sum_money > espresso_cost or sum_money > latte_cost or sum_money > cappuccino_cost:
            if user_choice == "espresso":
                print(f"Here is ${round(sum_money - espresso_cost, 2)} dollars in change.")
            elif user_choice == "latte":
                print(f"Here is {round(sum_money - latte_cost, 2)} dollars in change.")
            elif user_choice == "cappuccino":
                print(f"Here is {round(sum_money - cappuccino_cost, 2)} dollars in change.")
            print(f"Here is your {user_choice}. Enjoy!")
        else:
            print(f"Here is your {user_choice}. Enjoy!")


def make_coffee():
    sum_money = process_coins()
    check_transaction(sum_money)


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        print("")

    # keys and values
    espresso = MENU['espresso']['ingredients']
    espresso_water = espresso['water']
    espresso_coffee = espresso['coffee']
    espresso_cost = MENU['espresso']['cost']

    latte = MENU['latte']['ingredients']
    latte_water = latte['water']
    latte_milk = latte['milk']
    latte_coffee = latte['coffee']
    latte_cost = MENU['latte']['cost']

    cappuccino = MENU['cappuccino']['ingredients']
    cappuccino_water = cappuccino['water']
    cappuccino_milk = cappuccino['milk']
    cappuccino_coffee = cappuccino['coffee']
    cappuccino_cost = MENU['cappuccino']['cost']

    if user_choice == "report":
        print(f"{water}: {water_value}ml\n{milk}: {milk_value}ml\n{coffee}: {coffee_value}g\n{money}: ${money_value}\n")
    elif user_choice == "espresso":
        if not check_resources_sufficient():
            continue
        make_coffee()
        water_value -= espresso_water
        coffee_value -= espresso_coffee
        money_value += espresso_cost
    elif user_choice == "latte":
        if not check_resources_sufficient():
            continue
        make_coffee()
        water_value -= latte_water
        coffee_value -= latte_coffee
        milk_value -= latte_milk
        money_value += latte_cost
    elif user_choice == "cappuccino":
        if not check_resources_sufficient():
            continue
        make_coffee()
        water_value -= cappuccino_water
        coffee_value -= cappuccino_coffee
        milk_value -= cappuccino_milk
        money_value += cappuccino_cost
    else:
        break
