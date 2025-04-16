unconfirmed_users = ['Alice', 'Bob', 'Eve']
confirmed_users = []

## reverse order
# while unconfirmed_users:
#     current = unconfirmed_users.pop()
#     confirmed_users.append(current)

# straight order
while unconfirmed_users:
    current = unconfirmed_users.pop(0)
    confirmed_users.append(current)

for confirmed_user in confirmed_users:
    print(f"Confirmed - {confirmed_user.title()}") 