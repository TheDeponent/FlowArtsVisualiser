import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.lines import Line2D

# Parameters
num_frames = 360
armspan_inches = 5 * 12 + 9  # 5'9" in inches
armspan_meters = armspan_inches * 0.0254  # Convert to meters
radius = 0.45  # Poi tether length in meters
trail_length = num_frames  # Length of the trail in frames

# Calculate angles
theta = np.linspace(0, 2 * np.pi, num_frames)

# Calculate coordinates for extension
extension_x = (armspan_meters / 2) * np.cos(theta) + radius * np.cos(theta)
extension_y = (armspan_meters / 2) * np.sin(theta) + radius * np.sin(theta)

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-armspan_meters, armspan_meters)
ax.set_ylim(-armspan_meters, armspan_meters)
ax.set_aspect('equal', adjustable='box')
ax.set_title('12 Petal Antispin vs Extension - Same time Same direction')
ax.set_xlabel('Head leading vs Head leading')
ax.set_xticks([])
ax.set_yticks([])

# Poi elements
extension_head, = ax.plot([], [], 'go', markersize=10)
extension_trail, = ax.plot([], [], color='g', linewidth=1.5, alpha=0.5)
extension_tether = Line2D([], [], color='k', linewidth=0.5)

ax.add_line(extension_tether)

# Initialize trails
extension_trail_x = []
extension_trail_y = []

# Update function for the animation
def update(frame):
    extension_head.set_data(extension_x[frame], extension_y[frame])

    # Add extension head position to trail
    extension_trail_x.append(extension_x[frame])
    extension_trail_y.append(extension_y[frame])

    # Remove old trail points
    if len(extension_trail_x) > trail_length:
        extension_trail_x.pop(0)
        extension_trail_y.pop(0)

    extension_trail.set_data(extension_trail_x, extension_trail_y)

    extension_tether.set_data([(armspan_meters / 2) * np.cos(theta[frame]), extension_x[frame]],
                              [(armspan_meters / 2) * np.sin(theta[frame]), extension_y[frame]])

    return extension_head, extension_trail, extension_tether

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# Save the animation as a GIF
writer = PillowWriter(fps=15)
ani.save("Extension.gif", writer=writer)
