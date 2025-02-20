### 5-2. More Conditional Tests:
real_g = "Gengsta"
you = "gengsta"

# case sensitive strings
print("Are you a real Gengsta?")
print(you == real_g)

print("So you are fake ass gengsta?")
print(you != real_g)

print("shame...")

# lower comparison
print("Only when real Gengstas are demoted you can qualify?")
print(you == real_g.lower())

# my number range
my_num = 4
print("\nMy num is less than 5")
print(my_num < 5)
print("My num is more than 1")
print(my_num > 1)
print("My num is more than or equal to 3")
print(my_num >= 3)
print("My num is not equal to 3")
print(my_num != 3)
print("My num is equal to 4")
print(my_num == 4)

# list presence
components = ["CAN", "LIN", "ECUM", "BSWM", "DCM", "DEM"]
print(f"\nCAN and LIN are in the list:")
print("CAN" in components and "LIN" in components)

print("DCM and DEM are in the list:")
print(("DCM" and "DEM") in components)

print("ECUM and ECUC are in the list:")
print(("ECUM" and "ECUC") in components)

print("BSWM or ASWM in the list:")
print(("BSWM" or "ASWM") in components)

print("GTM is not in the list:")
print("GTM" not in components)