### 10-2. Learning C:

import pathlib as pl

my_path = pl.Path("learning_python.txt")
my_str = my_path.read_text()
print(my_str)

my_str = my_str.replace('Python', 'C')
my_str = my_str.replace("can", "can't")
print(my_str)