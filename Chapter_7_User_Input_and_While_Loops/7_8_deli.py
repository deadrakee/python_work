### 7-8. Deli:

sandwich_orders = ['ham', 'cheese','veggie', 'salami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Preparing {current_sandwich} sandwich..")

    finished_sandwiches.append(current_sandwich)

print()
for sandwich in finished_sandwiches:
    print(f"Sandwiches finished - {sandwich}")