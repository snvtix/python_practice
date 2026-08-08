costs = {
    "americano" : 10, # pln
    "cappucino" : 15, # pln
    "latte" : 17 # pln
}

resources = {
    "water" : 3000, # ml
    "milk" : 2000, # ml
    "coffee" : 1500 # grams
}

requirements = {
    "americano": {"water": 300, "milk": 0,   "coffee": 75},
    "cappucino": {"water": 100, "milk": 200, "coffee": 50},
    "latte":     {"water": 100, "milk": 300, "coffee": 50}
}

money = 50.0

def make_coffee(coffee_type):

    coffee = coffee_type.lower()

    if coffee in requirements and check_resources_coffee(coffee) == True:
        resources["water"] = resources["water"] - requirements[coffee]["water"]
        resources["milk"] = resources["milk"] - requirements[coffee]["water"]
        resources["coffee"] = resources["coffee"] - requirements[coffee]["water"]
        print(f"One {coffee} ready!")
    else:
        print(f"{coffee.title()} not avaible.")

def check_resources_coffee(coffe_type):

    coffee = coffee_type.lower()

    if resources["water"] >= requirements[coffee]["water"] and resources["milk"] >= requirements[coffee]["water"] and resources["coffee"] >= requirements[coffee]["water"]:
        return True
    else:
        return False

def insert_money(coffe_type):
    coin_list = [0.1, 0.2, 0.5, 1, 2, 5]
    coin_number = []
    coins_value = 0

    print("Insert coins.")
    for coin in range(6):
        print(f"Number of {coin_list[coin]} pln coins: ")
        coin_number.append(input())
        coins_value += int(coin_number[coin])*coin_list[coin]

    if coins_value >= costs[coffee_type]:
        if coins_value == costs[coffee_type]:
            make_coffee(coffee_type)
        else:
            print(f"Return of {str(round(coins_value-costs[coffee_type], 2))} pln.")
            make_coffee(coffee_type)
    else:
        print("Please try again.")
        print(f"Return of {str(coins_value)} pln.")

print("Hi, would you want to order a coffee?")
print("There are avaible: americano (10 pln), cappucino (15 pln) and latte (17 pln)")

while True:
    print("Choose your coffee: ")
    coffee_type = input()
    insert_money(coffee_type)
    print("\n")

    
