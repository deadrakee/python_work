### 10-12. Favorite Number Remembered:

import json
import pathlib as pl

path = pl.Path("db_10_12.json")

if path.exists():
    number = json.loads(path.read_text())
    print(f"Your number was {number}")
else:
    number = input("Enter number: ")
    path.write_text(json.dumps(number))