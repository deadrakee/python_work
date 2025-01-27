### 4-11. My Pizzas, Your Pizzas
pizzas = ["pepperoni", "hawai", "formagi"]
friend_pizzas = pizzas[:]

pizzas.insert(1, "proshuto")
friend_pizzas.append("diavola")

# show elements of the first list
print("My pizzas:")
for pizza in pizzas:
    print(f"\t{pizza}")

# show elements from the second list
print(f"\nKrasi's pizzas:")
for pizza in friend_pizzas:
    print(f"\t{pizza}")
