### 15-1. Cubes:
import matplotlib.pyplot as plt

# Cubes of 1-5
x_val_five = range(1,6)
y_val_five = [x**3 for x in x_val_five]

# Cubes until 5k
x_val_five_k = range(1,5_001)
y_val_five_k = [x**3 for x in x_val_five_k]

# Create the graphs
fig, ax = plt.subplots()
fig2, bx = plt.subplots()

# Label ax graph (until 5)
ax.set_title("Cube numbers")
ax.set_xlabel("Value")
ax.set_ylabel("Cubes")
# Set and offset on top and right big 1/3 of the largest value
ax.axis([0,
         x_val_five[-1] + x_val_five[-1]//3,
         0,
         y_val_five[-1] + y_val_five[-1]//3
         ])

# Label bx graph (until 5000)
bx.set_title("Cube numbers")
bx.set_xlabel("Value")
bx.set_ylabel("Cubes")
# Set and offset on top and right big 1/3 of the largest value
bx.axis([0,
         x_val_five_k[-1] + x_val_five_k[-1]//3,
         0,
         y_val_five_k[-1] + y_val_five_k[-1]//3
         ])

# Place the two lines on the plot
ax.scatter(x_val_five, y_val_five, color='red', s=10)
bx.scatter(x_val_five_k, y_val_five_k, color='green', s=10)

plt.show()
