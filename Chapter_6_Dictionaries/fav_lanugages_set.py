set_example = {'a', 'b', 'a', 'a', 'c', 'd', 'b','d'}

print(f"Set_example(unique values) - {set_example}\n")

dict_example = {'a': 'b', 'a': 'a', 'c': 'd', 'b':'d', 'a':'overwrite'}

# print both key and value
print("Print both key and value:")
for key, value in dict_example.items():
    print(f"key - {key}\nvalue - {value}\n")

# only keys
print("\n\nKeys only:")
for key in dict_example:
    print(f"key - {key}\n")

# only values
print("\n\nValues only:")
for val in dict_example.values():
    print(f"val - {val}\n")

# unique values only
print("\n\nUnique values only:")
for val in set(dict_example.values()):
    print(f"unique val - {val}\n")