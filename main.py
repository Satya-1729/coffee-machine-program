from pickle import GLOBAL

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
Profit = 0

# report off, and it must pop up whenever the machine gets a coffee
def check_resources(coffee_type, water, milk, coffee):
    req_water = MENU[coffee_type]["ingredients"]["water"]
    req_milk = MENU[coffee_type]["ingredients"]["milk"]
    req_coffee = MENU[coffee_type]["ingredients"]["coffee"]

    # checking
    if water < req_water:

        return False,req_water, req_milk, req_coffee
    elif milk < req_milk:
        return False,req_water, req_milk, req_coffee
    elif coffee < req_coffee:
        return False,req_water, req_milk, req_coffee
    else:
        return True, req_water, req_milk, req_coffee


def coffee_machine(resources, MENU):


    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    global Profit


    while True:
        prompt = input("What would you like? (espresso/latte/cappuccino):\n").lower()

        if prompt == "report":
            # we have to give the current resources that we have
            print(f"the current resources is \nWater: {water} \nMilk: {milk} \nCoffee: {coffee} \nMoney: ${Profit}")
        elif prompt == "off":
            return "BBYE"

        else:
            print("Invalid choice. Please select espresso, latte, or cappuccino.")
            continue

        coffee_type = str(input("What would you like? (espresso/latte/cappuccino):\n"))

        # here checking if we have the required resources left
        flag, req_water, req_milk, req_coffee = check_resources(coffee_type, water, milk, coffee)
        cost = MENU[coffee_type]["cost"]

        if flag == True:
            # deducting the resources
            water -= req_water
            milk -= req_milk
            coffee -= req_coffee

            # if this is true then we will process the money
            print("Insert the money so we can make the drink")

            quarters = 0.25 * int(input("How many quarters? "))
            dimes = 0.10 * int(input("How many dimes? "))
            nickles = 0.05 * int(input("How many nickels? "))
            pennies = 0.01 * int(input("How many pennies? "))

            money = quarters + dimes + nickles + pennies

            if money < cost:
                print(f"Sorry that's not enough money. Money refunded. ${money:.2f}")
            elif money > cost:
                change = money - cost
                Profit += cost
                print(f"Here is your change ${change:.2f}.")
            else:
                Profit += cost

            print(f"the current resources is after purchasing coffee\nWater: {water} \nMilk: {milk} \nCoffee: {coffee} \nMoney: ${Profit}")
            print(f"Here is your {coffee_type}\n\n")

        else:
            print("Sorry, we don't have enough resources")
            break


print(coffee_machine(MENU=MENU, resources=resources))
