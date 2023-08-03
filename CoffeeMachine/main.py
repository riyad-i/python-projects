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

resources["money"] = 0
MENU["espresso"]['ingredients']['milk']=0

def print_report(resources):
    report = resources.copy()
    for key in report:
        if key == 'water' or key == 'milk':
            report[key] = str(report[key]) + 'ml'
        elif key == 'coffee':
            report[key] = str(report[key]) + 'g'
        elif key == 'money':
            report[key] = '$' + str(report[key])
        print(key.capitalize()+":", report[key])

def change(want):
    #todo can call makedrink function at end of this one if customer had enough money
    #todo or return true if change went through and then call makedrink function in main loop
    price=MENU[want]['cost']
    print(f"That would be ${price} please.")
    print('Please insert coins.')
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickels = int(input('how many nickels?: '))
    pennies = int(input('how many pennies?: '))
    total=  .25 * quarters + .1* dimes + .05 * nickels + .01 * pennies
    #print(total)
    if total > price:
        print(f"Here is ${round(total - price,2)} in change.\nHere is your {want}. Enjoy!")
        return True
    elif total == price:
        print(f"Here is your {want}. Enjoy!")
        return True
    elif total < price:
        print("Sorry that's not enough money. Money refunded.")
        return False



        #todo def check ingredients first, return true, than later attempt drink, might be same with payment ie. check change first than remove currency
def check_ingredients(want):
        #todo returns Sorry there is not enough water. depending on what ingredient isn't enough
        #todo subtracts ingredients if successful and gives drink
        #todo compare tuple values
    if (resources["water"],resources["milk"],resources["coffee"]) >= (MENU[want]['ingredients']['water'],MENU[want]['ingredients']['milk'],MENU[want]['ingredients']['coffee']) :
        #todo need this body for attempt drink function
        # resources['water'] = resources['water'] - MENU[want]['ingredients']['water']
        # resources['milk'] = resources['milk'] - MENU[want]['ingredients']['milk']
        # resources['coffee'] = resources['coffee'] - MENU[want]['ingredients']['coffee']
        return True
    else:
        print(f"Sorry there aren't enough ingredients")
        return False

def remove_ingredients(want):
   resources['water'] = resources['water'] - MENU[want]['ingredients']['water']
   resources['milk'] = resources['milk'] - MENU[want]['ingredients']['milk']
   resources['coffee'] = resources['coffee'] - MENU[want]['ingredients']['coffee']
   resources['money'] = resources['money'] + MENU[want]['cost']




while True:
    try:
        print(resources.values())
        want = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if want == 'off':
            exit()
        elif want == 'report':
            print_report(resources)
            continue
        else:#todo check drink ingredients before payment, return true or false whether enough ingreidents, than continue to payment accordinhly
            if check_ingredients(want) is False:
                continue
            #todo then change then attempt drink
            if change(want) is False:
                continue
            remove_ingredients(want)#aka attempt_drink
            print(resources)
    except KeyError:
        print('type valid input')











