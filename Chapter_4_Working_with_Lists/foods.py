# list copy

my_foods = ["kinoa", "nahut", "fokacha", "oves", "zapekanka"]
g_foods = my_foods[::3]
print(g_foods)

copy_foods = my_foods
my_foods.append("noodles")
print(copy_foods)