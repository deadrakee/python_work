from pathlib import Path
import json

list = [1,2,3,4,5]
path = Path('text_files/list_as_json.json')

#convert to json string
json_list = json.dumps(list)
print(f"json string {json_list}")
path.write_text(json_list)
