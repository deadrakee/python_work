import json
from pathlib import Path

path = Path('text_files/list_as_json.json')

try:
    json_str = path.read_text()
except FileNotFoundError:
    print("File not found")
else:
    # convert json string to python object
    list = json.loads(json_str)

print("List:")
for element in list:
    print(element)