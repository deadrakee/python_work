### 10-1. Learning Python:

from pathlib import Path

my_path = Path("learning_python.txt")
print(f"Print directly:\n{my_path.read_text()}")

list = my_path.read_text().splitlines()

index = 1
print("Print line by line:")
for line in list:
    print(f"{index} {line}")
    index+=1