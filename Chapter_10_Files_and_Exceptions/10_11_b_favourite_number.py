### 10-11-b. Favorite Number 

import json
from pathlib import Path

path = Path("db_10_11.json")

if path.exists():
    content = path.read_text()
    number = json.loads(content)
    print(f"I know your favorite number! It’s {number}.")
else:
    print("File does not exist..")
