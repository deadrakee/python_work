### Polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

new_participants = ['john', 'adam', 'jen', 'thomas', 'bill', 'sarah', 'matthew', 'phil']

for participant in new_participants:
    if participant in favorite_languages:
        print(f"Thanks for your time {participant.title()}. {favorite_languages[participant].title()} is cool!")
    else:
        print(f"{participant.title()}, please take the poll.")