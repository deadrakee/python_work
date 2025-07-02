import os
from pathlib import Path

print("Current working directory:", os.getcwd())

# file in the same folder
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents, end="\n\n")

# file in a subfolder
nested_path = Path('text_files/nested_text.txt')
print(nested_path.read_text(), end="\n\n")

# file in a different branch
deep_path = Path('../../U2A6/U2A6_all/RH850.fcf')
print(deep_path.read_text(), end="\n\n")

# absolute path
absolute_path = Path('C:/Users/sab1sf/Desktop/GermanUmlaut.ahk')
print(absolute_path.read_text())