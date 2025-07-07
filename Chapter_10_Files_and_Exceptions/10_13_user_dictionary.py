### 10-13. User Dictionary:

import json
from pathlib import Path

path = Path("db_10_13.json")

if path.exists():
    user_data = json.loads(path.read_text())
    print(user_data)
else:
    user_data = {}
    user_data["name"] = input("Enter name: ")
    user_data["age"] = input("Enter age: ")
    user_data["rank"] = input("Enter rank: ")
    user_data["champion"] = input("Enter favourite champion: ")
    path.write_text(json.dumps(user_data))
    print("Stored in file!")