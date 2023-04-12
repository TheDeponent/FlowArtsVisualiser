import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters of the ellipse
a = 1
b = 2
omega = 2 * np.pi / 5

# Define the initial position of the circle
x0 = a
y0 = 0

# Create a figure and axis for the animation
fig, ax = plt.subplots(figsize=(10, 6))
plt.axis('equal')

# Define the circle and trail objects
circle, = ax.plot([], [], 'o', color='red')
trail, = ax.plot([], [], '-', color='red', alpha=0.5)

# Set the x and y axis limits
xlim = (-5, 5)
ylim = (-5, 5)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

# Define the initialization function for the animation
def init():
    circle.set_data([], [])
    trail.set_data([], [])
    return circle, trail

# Define the update function for the animation
x_trail, y_trail = [], []
def update(frame):
    t = frame / 100
    x = a * np.cos(omega * t)
    y = b * np.sin(omega * t)
    circle.set_data(x, y)
    x_trail.append(x)
    y_trail.append(y)
    trail.set_data(x_trail, y_trail)
    return circle, trail

# Create and run the animation
ani = FuncAnimation(fig, update, frames=1000, init_func=init, blit=True, interval=10)
plt.show()
