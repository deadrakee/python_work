### 7-9. No Pastrami

sandwich_orders = ['ham', 'pastrami', 'pastrami', 'cheese', 'pastrami', 'veggie', 'salami']
finished_sandwiches = []
pastrami_orders_count = 0

print("The Deli ran out of pastrami!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    pastrami_orders_count+=1

print(f"Pastrami orders cancelled: {pastrami_orders_count}.\n")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Preparing {current_sandwich} sandwich..")

    finished_sandwiches.append(current_sandwich)

print()
for sandwich in finished_sandwiches:
    print(f"Sandwiches finished - {sandwich}")