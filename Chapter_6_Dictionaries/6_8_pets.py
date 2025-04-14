### 6-8. Pets

pet_0 = {"kind":"dog", "owner":"tonkata"}
pet_1 = {"kind":"cat", "owner":"snejana"}
pet_2 = {"kind":"fish", "owner":"mitko"}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"{pet["owner"].title()} has a {pet["kind"]}.")