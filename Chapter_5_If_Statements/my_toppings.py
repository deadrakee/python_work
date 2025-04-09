toppings_available = ['pepe', 'cheese', 'ham,' 'mushroom', 'tomato', 'yellow_cheese']
toppings_requested = ['tomato', 'yellow_cheese', 'peperoni']
pizza_possible = True

for current_topping in toppings_requested:
    if current_topping not in toppings_available:
        print(f"{current_topping} is missing")
        pizza_possible = False

if pizza_possible == True:
    print("Pizza is done!")