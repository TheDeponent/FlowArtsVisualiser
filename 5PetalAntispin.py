import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Circle
from matplotlib.lines import Line2D
import math

# Constants
armspan = 5 * 12 * 2.54  # 5'9" in centimeters
arm_length = armspan / 2
tether_length = 45
poi_radius = 5
title = "5 Petal Antispin"
xlabel = "Poi = 45cm, Performer Armspan 5'9"

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-armspan / 2 - tether_length, armspan / 2 + tether_length)
ax.set_ylim(-armspan / 2 - tether_length, armspan / 2 + tether_length)
ax.set_title(title)
ax.set_xlabel(xlabel)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal', adjustable='box')

# Initialize elements
tether_line = Line2D([], [], color="black", linewidth=1)
poi_circle = Circle((0, 0), poi_radius, color="red", fill=True)
poi_trail, = plt.plot([], [], color="red", linewidth=1)

def init():
    ax.add_patch(poi_circle)
    ax.add_line(tether_line)
    ax.add_line(poi_trail)
    return tether_line, poi_circle, poi_trail

def update(frame):
    # Arm and poi positions
    arm_angle = -2 * np.pi * frame / 360
    poi_angle = -4 * arm_angle + (np.pi / 2)  # (np.pi / -) For top centred, positive for bottom centred
    arm_x = arm_length * math.cos(arm_angle)
    arm_y = arm_length * math.sin(arm_angle)
    poi_x = arm_x + tether_length * math.cos(poi_angle)
    poi_y = arm_y + tether_length * math.sin(poi_angle)

    # Update elements
    tether_line.set_data([arm_x, poi_x], [arm_y, poi_y])
    poi_circle.set_center((poi_x, poi_y))
    poi_trail.set_data(np.append(poi_trail.get_xdata(), poi_x), np.append(poi_trail.get_ydata(), poi_y))
    return tether_line, poi_circle, poi_trail

ani = FuncAnimation(fig, update, frames=360, init_func=init, blit=True)

# Save as GIF using PillowWriter
writer = PillowWriter(fps=24)
ani.save("5_petal_antispin.gif", writer=writer)
