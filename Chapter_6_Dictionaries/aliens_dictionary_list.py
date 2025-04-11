aliens = []

# Create 30 green aliens
for alien in range(30):
    alien_x = { 'id': alien, 'color': 'green', 'speed':'slow', 'points': 5 }
    aliens.append(alien_x)

# recolor first 5
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'

for alien in aliens[:10]:
    print(alien)
print("\n\n")


# recolor first 8
for alien in aliens[:8]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'

for alien in aliens[:10]:
    print(alien)
print("\n\n")


# recolor first 10
for alien in aliens[:10]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'

for alien in aliens[:10]:
    print(alien)
print("\n\n")