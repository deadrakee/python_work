### 8-10. Sending Messages:

def empty_messages(messages, sent_messages):
    """pass to func"""
    while messages:
        message = messages.pop(0)
        sent_messages.append(message)
        print(message)

def show_messages(type, messages):
    """just print"""
    print("------------")
    print(f"{type}: {messages}")

messages = ["Hallo mein Freund", "Was is deine Lieblingshobby?", "Passt dir?", "Wir machen das"]
sent_messages = []

empty_messages(messages, sent_messages)
show_messages("messages", messages)
show_messages("sent", sent_messages)