### 10-5. Guest Book:

from pathlib import Path

users = ""
input_name = ""

while input_name != 'finished':
    users+=input_name+'\n'
    input_name = input("\nEnter new name or 'finished': ")

path = Path("guest_book.txt")
path.write_text(users.lstrip())