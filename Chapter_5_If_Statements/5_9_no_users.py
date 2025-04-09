### 5-9. No Users:

usernames = []

if usernames:
    for name in usernames:
        if(name == "admin"):
            print("Full permissions granted admin!")
        else:
            print(f"Hello {name}, no usb for you.")
else:
    print("We need to find some users!")