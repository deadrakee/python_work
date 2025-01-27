#3-4. Guest List
guests = ["Tysoncheto", "Carlos", "Will"]

print(f"Ela si govorim za fizika {guests[0].title()}, shte ima kurvi.")
print(f"{guests[1].title()} sushto e pokanen.")
print(f"And welcome to the dinner Mr. {guests[2].title()}.")

#3-5. Changing Guest List
absent  = "Carlos"
print(f"\n{absent.title()} izpederasti, kolata mu ne zapalila...")
guests[1] = "hamilton"
print(f"Ela si govorim za fizika {guests[0].title()}, shte ima kurvi.")
print(f"{guests[1].title()} sushto e pokanen.")
print(f"And welcome to the dinner Mr. {guests[2].title()}.")

#3-6. More Guests
print(f"\nHey {guests}, new info. Here come new challengers!")
guests.insert(0, "Ekko")
guests.insert(2, "Hailee")
guests.append("yukimura_sanada_san")
stringy_guests = f"{guests}"
print(f"All invited: {stringy_guests.title()}.")

#3-7. Shrinking Guest List
print("\nFree cash flow, only two will eat!")
banished = guests.pop()
print(f"{banished.title()} - sedi si u doma")
banished = guests.pop()
print(f"{banished.title()} - sedi si u doma")
banished = guests.pop()
print(f"{banished.title()} - sedi si u doma")
banished = guests.pop()
print(f"{banished.title()} - sedi si u doma")
print(f"The real motherfucking Gs are {guests[0].title()} and {guests[1].title()}")
del guests[0]
del guests[0]
print(guests)