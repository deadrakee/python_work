### 5-1. Conditional Tests
# Generate a random number and try to match it with 3 or 8
import random

num = random.randint(1,10)

print("Is num < 10? I predict True.")
print(num < 10)

print("Is num > 1? I predict True.")
print(num > 1)

print("Is num > 5? I predict True.")
print(num > 5)

print("Is num == 8? I predict True.")
print(num == 8)

print("Is num < 5? I predict False.")
print(num < 5)

print("Is num == 3? I predict True.")
print(num == 3)