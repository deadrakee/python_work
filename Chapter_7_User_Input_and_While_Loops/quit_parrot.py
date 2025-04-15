prompt = "\nSay something new or enter 'quit' to stop the program:\n"

message = ""

while message != 'quit':
    message = input(prompt)
    print(f"Repeat: {message}")