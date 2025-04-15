### 7-5. Movie Tickets

prompt = "\nHow old are you: "

age = 0
price = 0

while True:
    age = int(input(prompt))

    if age < 1:
        price = -1

    elif age < 3:
        price = 0
    
    elif age < 13:
        price = 10
    
    elif age < 100:
        price = 15

    else:
        price = -1
    
    if price == -1:
        print("Do not lie to me...")
    else:
        print(f"Your ticket costs {price}$.")