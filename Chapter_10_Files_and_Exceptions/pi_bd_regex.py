import re
import pathlib

# create a string of PI with 1M digits
path = pathlib.Path('text_files/pi_million_digits.txt')
pi_list = path.read_text().split()
pi_str = ''

for line in pi_list:
    pi_str+=line.lstrip()

# search for the birthday in the pi string with regex
birthday = "120394"
match = re.search(birthday, pi_str)

if match is not None:
    print(f"Found '{match.re.pattern}' in\n{match.string}")
    print(f"from {match.start()} to {match.end()}({pi_str[match.start():match.end()]})")
else:
    print("No match")