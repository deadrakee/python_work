### 10-6. Addition:

first_num = input("Enter number: ")
second_num = input("Enter second number: ")

try:
    result = int(first_num) + int(second_num)
except ValueError:
    print("Can't sum letters...")
else:
    print(f"result = {result}")