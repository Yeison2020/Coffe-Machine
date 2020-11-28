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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}






def is_rosource_sufficient(order_ingredients):
    is_enough = True
    for item in  order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough water{item}")
            is_enough = False
    return is_enough

def is_transaction_succeful(money_receive, drink_cost):
    # Note: I was not getting it hightlight, because they were not define
    """ This will return Ture when the payment is accepted, ,or False when if money is not sufficient."""
    if money_receive >= drink_cost:
        # To reache the profit from a global scope
        change = round(money_receive - drink_cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process_coin():

    """
    Return True when the order can be make or False when not ingredient no suffiecient
    """

    print("Insert coins")
    total = int(input("How many quarters\n")) * 0.25
    total += int(input("How many dimes\n")) * 0.10
    total += int(input("How many  nickles\n")) * 0.05
    total += int(input("How many pennies\n")) * 0.01
    return total


def make_coffe(drink_name, order_ingredients):
    """ Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")



run_machine = True

while run_machine:

    """Return the total calculated from coins inserted"""

    choice = input("What would you like? (espresso/latte/cappuccino)").lower()

    if choice == "off":
        run_machine = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']}50ml")
        print(f"Coffee:{resources['coffee']}76g")
        print(f"Money:{profit}")
    else:
        drink = MENU[choice]
        #print(drink)
        if is_rosource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_succeful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])












