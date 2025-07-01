### 9-14. Lottery:

import random

lotto_stack = []
lotto_balls = []

# Add 10 random numbers in the list. Every execution will have different results
for _ in range(10):
    lotto_stack.append(random.randint(0, 100))

# Add five random lowercase letters
for _ in range(5):
    lotto_stack.append(chr(random.randint(97, 122)))

# Select 4 random elements from the previous list
for _ in range(4):
    lotto_balls.append(random.choice(lotto_stack))

print(lotto_stack)
print(lotto_balls)