# Test dictionaries

alien_0 = { 'color':"red", "points":5 }

print(alien_0)

alien_0['x'] = 0
alien_0['y'] = 25

print(alien_0)

alien_0["color"] = "yellow"

print(alien_0)

alien_0 = {"speed":"slow"}

print(alien_0)

del alien_0["speed"]

print(alien_0)

alien_0 = {"color": ""}

print(alien_0)

print(alien_0.get("points"))