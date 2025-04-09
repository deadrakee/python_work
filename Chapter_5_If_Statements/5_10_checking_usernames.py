### 5-10. Checking Usernames

current_users_all_case = ["JACK", "John", "amy", "MICHAEL", "Viktor"]
current_users = []
new_users = ["Adam", "Betty", "jack", "Amy", "Stef"]

for current_user in current_users_all_case:
    current_users.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Username '{new_user.lower()}' is already taken. Enter new username.")
    else:
        print("username available")