import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

# Parameters
num_frames = 360
armspan_inches = 5 * 12 + 9  # 5'9" in inches
armspan_meters = armspan_inches * 0.0254  # Convert to meters
radius = 0.45  # Poi tether length in meters

# Calculate angles for antispin
theta = np.linspace(0, 2 * np.pi, num_frames)
antispin_theta = np.linspace(0, -10 * np.pi, num_frames)  # Change to negative for clockwise rotation

# Calculate coordinates for gunslinger antispin
rotation_center_x = (armspan_meters / 2) * np.cos(theta)
rotation_center_y = (armspan_meters / 2) * np.sin(theta)
antispin_head_x = rotation_center_x + (radius / 2) * np.cos(antispin_theta)
antispin_head_y = rotation_center_y + (radius / 2) * np.sin(antispin_theta)
antispin_handle_x = rotation_center_x - (radius / 2) * np.cos(antispin_theta)
antispin_handle_y = rotation_center_y - (radius / 2) * np.sin(antispin_theta)

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-armspan_meters, armspan_meters)
ax.set_ylim(-armspan_meters, armspan_meters)
ax.set_aspect('equal', adjustable='box')

# Poi elements
antispin_head, = ax.plot([], [], 'ro', markersize=10)
antispin_handle, = ax.plot([], [], 'bo', markersize=10)
antispin_tether = Line2D([], [], color='k', linewidth=0.5)
ax.add_line(antispin_tether)

# Update function for the animation
def update(frame):
    antispin_head.set_data(antispin_head_x[frame], antispin_head_y[frame])
    antispin_handle.set_data(antispin_handle_x[frame], antispin_handle_y[frame])
    antispin_tether.set_data([antispin_head_x[frame], antispin_handle_x[frame]],
                             [antispin_head_y[frame], antispin_handle_y[frame]])

    return antispin_head, antispin_handle, antispin_tether

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

plt.show()
