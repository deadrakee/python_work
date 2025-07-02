### 10-4. Guest:

from pathlib import Path

name = input("Tell me your name: ")
path = Path("guest.txt")
path.write_text(name)