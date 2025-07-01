### 9-15. Lottery analysis

import random

lotto_stack = []
my_balls = []
current_balls = []

# Add 10 random numbers in the list. Every execution will have different results
for _ in range(10):
    lotto_stack.append(random.randint(0, 100))

# Add five random lowercase letters
for _ in range(5):
    lotto_stack.append(chr(random.randint(97, 122)))

# Select 4 random elements from the previous list
for _ in range(4):
    my_balls.append(random.choice(lotto_stack))

indx = 1

# Make a new list of 4 items in each iteration. End cycle when
# the current 4 item list matches the my_balls 4 items list
while True:
    current_balls = []
    for _ in range(4):
        current_balls.append(random.choice(lotto_stack))

    if current_balls == my_balls:
        print(f"No of runs: {indx}")
        print(lotto_stack)
        print(current_balls)
        print(my_balls)
        break
    else:
        print(f"Current balls: {current_balls}")
    indx+=1
