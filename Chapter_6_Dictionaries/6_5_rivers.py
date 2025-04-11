### 6-5. Rivers:

rivers = {
    'nile': 'egypt',
    'danube': 'austria',
    'danube': 'bulgaria',
    'iskar': 'bulgaria',
    }

for river_name, river_country in rivers.items():
    print(f"{river_name.title()} flows through {river_country.title()}.")

# Danube key for Austria is not printed, because it is overwritten by Bulgaria

print("\nAll rivers are:")
for river_name in rivers:
    print(river_name.title())

print("\nAll countries are:")
for river_country in set(rivers.values()):
    print(river_country.title())