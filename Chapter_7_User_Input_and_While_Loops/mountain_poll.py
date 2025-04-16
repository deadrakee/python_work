polls = {}

polling_active = True

while polling_active:
    name = input("\nWho are you? ")
    mountain = input("Your mountain? ")

    polls[name] = mountain

    continue_polling = input("\nContinue polling?(yes/no) ")

    if continue_polling == 'no':
        polling_active = False

print("____________________\nPoll results:")
for name, mountain in polls.items():
    print(f"\n{name.title()} climbs {mountain.title()}")