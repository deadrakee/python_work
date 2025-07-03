### 10-8. Cats and Dogs:

from pathlib import Path

cat_path = Path("text_files/cats.txt")
dog_path = Path("text_files/dogs.txt")

try:
    print(cat_path.read_text()+'\n')
except FileNotFoundError:
    print("cats.txt not found!")

try:
    print(dog_path.read_text()+'\n')
except FileNotFoundError:
    print("dogs.txt not found!")