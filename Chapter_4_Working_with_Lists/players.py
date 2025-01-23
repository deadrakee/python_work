# slices

players = ["Gabi", "Ivaka", "Nikola", "Enkata", "Kalin", "Boji", "Golemiq"]
# print(players[-4::3])

indx = 1
print("First three players are:")
for player in players[:3]:
    print(f"Player {indx} - {player}")
    indx+=1

rev_idx = len(players)-2
print("\nLast three are:")
for player in players[-3:]:
    print(f"Player {rev_idx} - {player}")
    rev_idx+=1