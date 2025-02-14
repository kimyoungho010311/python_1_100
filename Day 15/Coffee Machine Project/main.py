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
    'money' : 100,
}


# TODO: 사용자 입력 처리 함수
def get_user_choice():
    pass

# TODO: 자원 충분 확인 함수
def check_resources(choice):
    ingredients = MENU[choice]['ingredients']
    for item, required in ingredients.items():
        if resources.get(item,0) < required:
            print(f"Sorry, there is not enough {item}.\n")
            return False
    print("Resources are sufficient.\n")
    return True

# TODO: 동전 입력 및 처리 함수
def process_coins(drink):
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }
    total = 0
    print("Please insert coins.\n")
    for coin, value in coins.items():
        count = int(input(f"How many {coin}? : "))
        total += count * value
    print(f"Total inserted: ${total:.2f}")
    if MENU[drink]["cost"] > total:
        print("Not enough money. Money refunded.")
        total = 0
    elif MENU[drink]['cost'] == total:
        make_coffee(drink)
        resources['money'] += total
    elif MENU[drink]['cost'] < total:
        change = total - MENU[drink]['cost']
        print(f'Here is ${change:.2f} dollars in change')
        resources['money'] += MENU[drink]['cost']
        make_coffee(drink)


# TODO: 음료 제조 함수
def make_coffee(drink):
    ingredients = MENU[drink]['ingredients']
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink}. Enjoy!\n")


# TODO: 보고서 출력 함수
def print_report():
    print('\n')
    for key, value in resources.items():
        if key == 'money':
            print(f"{key.capitalize()}: ${value:.2f}")
        else:
            unit = 'ml' if key in ['water', 'milk'] else 'g'
            print(f"{key.capitalize()}: {value} {unit}")
    print('\n')
# TODO: 메인 루프 구현
def coffee_machine():
    # repeat program
    program = True

    while True:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink in ['espresso', 'latte', 'cappuccino']:
            if check_resources(drink):
                process_coins(drink)
            else:
                print("Cannot proceed due to insufficient resources.\n")
        elif drink == 'off':
            print("\nCoffee machine off. Goodbye!")
            break
        elif drink == 'report':
            print_report()
        else:
            print("Invalid input. Please try again.\n")


coffee_machine()
