prompt = "\nSay something new or enter 'quit' to stop the program:\n"

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f"Re: {message}")