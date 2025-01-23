# Exercise divided in four sections:
# 1. Shows usage of f-strings
# 2. Use of quotes and apostrophes in a single expression
# 3. Whitespace stripping
# 4. Suffix removal

print("\n")

#2-3,4
name = "Boyan"
print(f"Hello {name.upper()}, would you like to learn some Python today?")

#2-5,6
famous_person = "albert einstein"
print(f'{famous_person.title()} once said, "A person who never made a mistake never tried anything new."')

#2-7
stripping = "\tsab1sf\n"
print(f"{stripping.strip()}.")

#2-8
filename = 'name_cases.py'
print(filename.removesuffix('.py'))