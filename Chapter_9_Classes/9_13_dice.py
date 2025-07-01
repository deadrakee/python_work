### 9-13. Dice:

import random

class Die:
    """Represent a virtual die"""

    def __init__(self, sides = 6):
        """Construct a die with x sides"""
        self.sides = sides

    def roll_die(self):
        """get from 1 to sides randomly"""
        print(f"Rolling d{self.sides}: {random.randint(1, self.sides)}")


indx = 0
my_dice = Die()

while(indx <= 10):
    my_dice.roll_die()
    indx+=1

indx = 0
my_dice = Die(10)

while(indx <= 10):
    my_dice.roll_die()
    indx+=1

my_dice = Die(20)
for _ in range(10):
    my_dice.roll_die()