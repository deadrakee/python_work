### 3-8. Seeing the World:

places = ['iceland', 'peru', 'cuba', 'switzerland', 'germany']
# original order
print(f"\n{places}")

# temporary sort
print(sorted(places))

# original order
print(places)

# temporary reverse
print(sorted(places, reverse=True))

# original order
print(places)

# reverse permanent
places.reverse()
print(places)

# reverse to original
places.reverse()
print(places)

# sort alphabetical permanently
places.sort()
print(places)

# sort alphabetically descendent permanently
places.sort(reverse=True)
print(places)

# sort ascending with reverse
places.reverse()
print(places)