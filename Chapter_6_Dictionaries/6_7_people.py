### 6-7. People

person_0 = {"name":"Gabriela", "surname":"Yordanova", "age":26, "hometown":"razgrad"}
person_1 = {"name":"Marshal", "surname":"Matters", "age":43, "hometown":"Detroit"}
person_2 = {"name":"Peter", "surname":"Park", "age":18, "hometown":"new york"}

people = [person_0, person_1, person_2]

for person in people:
    print(f"{person["name"].title()} {person["surname"].title()} is born in {person["hometown"].title()}"
          f" and is currently {person["age"]} years old.")