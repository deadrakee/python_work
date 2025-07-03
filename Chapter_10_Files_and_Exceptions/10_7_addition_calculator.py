### 10-7. Addition Calculator

while True:
    try:
        first_num = int(input("Enter first number: "))
    except ValueError:
        print("Can't sum letters..")
    else:
        break

while True:
    try:
        second_num = int(input("Enter second number: "))
    except ValueError:
        print("Can't sum letters..")
    else:
        break
    
result = first_num + second_num
print(f"result = {result}")