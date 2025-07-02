import pathlib

path = pathlib.Path('text_files/pi_million_digits.txt')

pi_list = path.read_text().split()

pi_str = ''

for line in pi_list:
    pi_str+=line.lstrip()

print('080399' in pi_str)