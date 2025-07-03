### 10-9. Silent Cats and Dogs

from pathlib import Path

cat_path = Path("text_files/cats.txt")
dog_path = Path("text_files/dogs.txt")

try:
    content_1 = cat_path.read_text()
except FileNotFoundError:
    pass
else:
    print(content_1)

try:
    content_2 = dog_path.read_text()
except FileNotFoundError:
    pass
else:
    print(content_2)
