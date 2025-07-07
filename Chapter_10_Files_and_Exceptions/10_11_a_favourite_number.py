### 10-11-a. Favorite Number 

import json
from pathlib import Path

number = input("What is your favorite number: ")

path = Path("db_10_11.json")
path.write_text(json.dumps(number))

