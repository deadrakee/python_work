### 7-2. Restaurant Seating:

table_limit = 8
people_count = int(input("How many people? "))

if people_count > table_limit:
    print("Wait for a table!")

else:
    print("Table is ready!")