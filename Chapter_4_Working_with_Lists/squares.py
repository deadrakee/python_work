# List comprehensions
squares = [val**2 for val in range(1,11)]
print(squares)

for idx in range(0, len(squares)):
    squares[idx]+=1
print(squares)