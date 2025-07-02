### 10-3. Simpler Code:

from pathlib import Path

path = Path('pi_digits.txt')
index = 1

for line in path.read_text().splitlines():
    print(f"{index}: {line}")
    index+=1
