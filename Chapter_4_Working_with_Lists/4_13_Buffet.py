### 4-13. Buffet
menu = ("fokacha", "kiufte", "shopska", "kartofi", "bob")

print("The menu is:")
for food in menu:
    print(food)

# wont work
# menu[0] = "krehko bavno pecheno svinsko s triufel"

menu = ("fokacha", "kiufte", "shopska", "zamruznali kartofi", "krehko bavno pecheno svinsko s triufel")

print("\nOnly now! New menu is:")
for food in menu:
    print(food)