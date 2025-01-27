# extract middle of a list
import math

size = 8
list = list(range(1,size+1))
print(list)

chunk = math.ceil(len(list)/3 )
print(f"\nchunk = {chunk}")

if len(list)%3:
    # since chunk is not a whole number, the starting point is 
    # somewhere between tho values. Decision is to start from the left index
    start_idx = chunk
    print(f"\nstart_idx drob = {start_idx}")
else:
    # chunk is a whole number, start from idx above
    start_idx = chunk+1
    print(f"\nstart_idx whole = {start_idx}")

end_idx = start_idx+chunk
print(f"\nend_idx = {end_idx}")

print(f"\n{list[start_idx-1:end_idx-1]}")



# Statistical report from testing

# >>> 3/3   1.0  = 1
# start 2

# >>> 4/3  upp 1.3333333333333333 = 2
# start 2

# >>> 5/3 1.6666666666666667 up = 2
# start 2

# >>> 6/3  2.0 = 2
# start 3

# 13 / 3 - zagruglqsh nagore 4.333 = 5
# pochvame ot 5


# >>> 14/3  nagore 4.666666666666667 = 5
# pochvame ot 6

# >>> 15/3   5.0 = 5
# pochvame ot 6