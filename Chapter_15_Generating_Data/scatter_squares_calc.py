from turtle import color
import matplotlib.pyplot as plt

x_val = range(1, 1001)
y_val = [x**2 for x in x_val]

plt.style.use('ggplot')

fig, ax = plt.subplots()

# Draw a blue line
# ax.scatter(x_val, y_val, color='blue', s=10)

# Draw a custom green line
# ax.scatter(x_val, y_val, color=(0, 0.5, 0), s=10)

# Draw a gradient blue by a colormap
ax.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Blues, s=10)

ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares", fontsize=14)
ax.tick_params(labelsize=14)

# Don't use scientific notation
# ax.ticklabel_format(style="plain")

# Set range for each axis
ax.axis([0,1100,0,1_100_000])

# Show on screen
plt.show()

# Save in file
# plt.savefig('plot.png', bbox_inches='tight')