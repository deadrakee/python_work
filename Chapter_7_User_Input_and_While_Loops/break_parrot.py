prompt = "\nSay something new or enter 'quit' to stop the program:\n"

while True:
    message = input(prompt)

    if message != 'quit':
        print(f"Re:{message}")
    else:
        break