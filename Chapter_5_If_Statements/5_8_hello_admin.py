### 5-8. Hello Admin:

usernames = ["alice", "bob", "admin", "eve", "nakov"]

for name in usernames:
    if(name == "admin"):
        print("Full permissions granted admin!")
    else:
        print(f"Hello {name}, no usb for you.")