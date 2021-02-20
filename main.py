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


def check_resources(requested_resources, available_resources):
    for ingredient in requested_resources:
        if requested_resources[ingredient] > available_resources[ingredient]:
            print(f"Sorry not enough {ingredient} available")
            return False
    return True


def calculate_change(drink_cost, entered_amount):
    if drink_cost > entered_amount:
        print(f"Sorry that's not enough money. Money refunded")
        return False
    else:
        change = round(entered_amount - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit_amount
        profit_amount += drink_cost
        return True


def process_coin():
    print("Please insert coin")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return round(amount, 2)


def process_drink(drink_name, request_ingredients):
    for ingredient in request_ingredients:
        resources[ingredient] -= request_ingredients[ingredient]
    print(f"Here is your {drink_name}. Enjoy!!")


profit_amount = 0
coffee_machine_is_on = True
while coffee_machine_is_on:
    user_input = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        for resource in resources:
            if resource != "coffee":
                print(f"{resource.title()}: {resources[resource]}ml")
            else:
                print(f"{resource.title()}: {resources[resource]}g")
        print(f"Money: {profit_amount}")
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        drink = MENU[user_input]
        if check_resources(drink["ingredients"], resources):
            total_amount = process_coin()
            if calculate_change(drink["cost"], total_amount):
                process_drink(user_input, drink["ingredients"])

    elif user_input == "off":
        coffee_machine_is_on = False
    else:
        print("Incorrect drink requested")