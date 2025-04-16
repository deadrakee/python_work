### 7-10. Dream Vacation:

favorite_places = {}
active = True

while active:
    propmpt = input("\nEnter username or 'quit': ")

    if propmpt == 'quit':
        active = False
    else:
        user = propmpt
        place = input("Which is your dream destination: ")
        favorite_places[user] = place


print(f"\nPoll summary:")
if favorite_places:
    for user, place in favorite_places.items():
        print(f"{user.title()}'s favorite place is {place.title()}")

else:
    print("No entries..")