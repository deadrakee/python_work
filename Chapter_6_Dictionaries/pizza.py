pizza = {
    'crust': 'italian',
    'toppings': ['mushrooms', 'cheese', 'salami'],
}

print(f"Order is '{pizza['crust']}' pizza with")

for topping in pizza['toppings']:
    print(topping)