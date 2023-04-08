import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

# Parameters
num_frames = 360
armspan_inches = 5 * 12 + 9  # 5'9" in inches
armspan_meters = armspan_inches * 0.0254  # Convert to meters
radius = 0.45  # Poi tether length in meters

# Calculate angles for extension
theta = np.linspace(0, 2 * np.pi, num_frames)

# Calculate coordinates for extension
extension_x = (armspan_meters / 2) * np.cos(theta) + radius * np.cos(theta)
extension_y = (armspan_meters / 2) * np.sin(theta) + radius * np.sin(theta)

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-armspan_meters, armspan_meters)
ax.set_ylim(-armspan_meters, armspan_meters)
ax.set_aspect('equal', adjustable='box')

# Poi elements
extension_head, = ax.plot([], [], 'go', markersize=10)
extension_tether = Line2D([], [], color='k', linewidth=0.5)
ax.add_line(extension_tether)

# Update function for the animation
def update(frame):
    extension_head.set_data(extension_x[frame], extension_y[frame])
    extension_tether.set_data([(armspan_meters / 2) * np.cos(theta[frame]), extension_x[frame]],
                              [(armspan_meters / 2) * np.sin(theta[frame]), extension_y[frame]])

    return extension_head, extension_tether

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

plt.show()
