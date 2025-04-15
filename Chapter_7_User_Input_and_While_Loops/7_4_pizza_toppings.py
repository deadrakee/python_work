### 7-4. Pizza Toppings:

prompt = "\nAdd a new pizza topping or enter 'stop': "
topping = ""

while topping != 'stop':
    topping = input(prompt)
    
    if topping != 'stop':
        print(f"Adding {topping} to the pizza!")