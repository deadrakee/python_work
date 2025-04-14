### 6-10. Favorite Numbers:

people_numbers = {
    "Boyan": [4, 2, 32, 1024, 3],
    "Gabi": [3, 5],
    "Nikola": [7, 9, 64, 4096],
    "Rozi": [9,],
    "Yana": [5, 1.2 ],
    }


for name, numbers in people_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")

    for number in numbers:
        print(f"\t{number}")