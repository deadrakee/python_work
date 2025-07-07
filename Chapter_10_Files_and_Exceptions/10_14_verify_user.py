### 10-14. Verify User:

from pathlib import Path
import json

def get_stored_username():
    """Get stored username if available."""
    path = Path('db_10_14.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
         return None

def save_new_username():
    """Prompt for a new username."""
    path = Path('db_10_14.json')
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def is_existing_user():
    """Verify whether the active username is matching file username """
    stored_username = get_stored_username()

    if stored_username:
        is_name_matching = "None"

        # loop until yes or no is entered by user
        while is_name_matching != "yes" and is_name_matching != "no":
            is_name_matching = input(f"Are you {stored_username}? ").lower()

        if is_name_matching == "yes":
            return True
        else:
            return False
    else:
        return False

def greet_user():
    """Greet the user by name."""
    user_existing = is_existing_user()

    if user_existing:
        stored_username = get_stored_username()
        print(f"Welcome back, {stored_username}!")
    else:
        username = save_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
