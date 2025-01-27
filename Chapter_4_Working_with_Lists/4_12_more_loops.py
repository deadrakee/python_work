### 4-12. More Loops
my_foods = ["kinoa", "nahut", "fokacha", "oves", "zapekanka"]
g_foods = my_foods[::3]

print("My foods are:")
for food in my_foods:
    print(f"\t{food}")

print("\nGabi's foods are:")
for food in g_foods:
    print(f"\t{food}")