def user_greeter(users):
    """prints list"""
    indx = 1
    for user in users:
        print(f"Name {indx} - {user}")
        indx += 1

all_users = ['alice', 'bob', 'eve']
user_greeter(all_users)