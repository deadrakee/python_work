### 3-10. Every Function:
everything = ['rila', 'kirkjufell', 'yantra', 'iceland', 'peru', 'selfoss', 'zajo', 'maltese']

print(everything)

# sort temp
print(sorted(everything))
print(everything)

# sort reverse temp
print(sorted(everything, reverse=True))
print(everything)

# reverse
everything.reverse()
print(everything)

# sort permanent
everything.sort()
print(everything)

# length
print(len(everything))

# delete first
del everything[0]
print(everything)

# pop last
everything.pop()
print(everything)

# add in middle
everything.insert(2, "Gabi")
print(everything)

# add in the end
everything.append("Amarkata")
print(everything)

# remove specific
everything.remove('yantra')
print(everything)
