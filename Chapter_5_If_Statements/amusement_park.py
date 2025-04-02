age = 75 

if age <= 4:
    price = 0

elif age <= 18:
    price = 25

elif age <= 74:
    price = 40

elif age >= 75:
    price = 20

else:
    print("Unreachable statement error")

print(f"You pay {price}$")