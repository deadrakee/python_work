import pathlib

pi_file = pathlib.Path('text_files/pi_million_digits.txt')
pi_list = pi_file.read_text().splitlines()
pi_str = ''

for pi_line in pi_list:
    pi_str+=pi_line.lstrip()

print(f"Beginning of PI: {pi_str[:12]}")
print(f"End of PI: {pi_str[-10:]}")