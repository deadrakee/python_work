current_num = 0

## Better implementation
# while current_num < 10:
#     if current_num % 2:
#         print(f"{current_num} is odd")

#     current_num += 1

while current_num < 10:
    current_num += 1
    if current_num % 2 == 0:
        continue
    print(f"{current_num} is odd")
