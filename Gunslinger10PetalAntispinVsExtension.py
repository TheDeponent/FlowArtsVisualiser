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
antispin_theta = np.linspace(0, -10 * np.pi, num_frames)  # Clockwise rotation for antispin

# Calculate coordinates for extension
extension_x = (armspan_meters / 2) * np.cos(theta) + radius * np.cos(theta)
extension_y = (armspan_meters / 2) * np.sin(theta) + radius * np.sin(theta)

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
ax.set_title('Gunslinger 10 Petal Antispin vs Extension')
ax.set_xlabel('Poi = 45cm, Performer Armspan 5\'9"')
ax.set_xticks([])
ax.set_yticks([])


# Poi elements
extension_head, = ax.plot([], [], 'go', markersize=10)
extension_trail, = ax.plot([], [], color='g', linewidth=1.5, alpha=0.5)
extension_tether = Line2D([], [], color='k', linewidth=0.5)
antispin_head, = ax.plot([], [], 'ro', markersize=10)
antispin_head_trail, = ax.plot([], [], color='r', linewidth=1.5, alpha=0.5)
antispin_handle, = ax.plot([], [], 'bo', markersize=10)
antispin_handle_trail, = ax.plot([], [], color='b', linewidth=1.5, alpha=0.5)
antispin_tether = Line2D([], [], color='k', linewidth=0.5)

ax.add_line(extension_tether)
ax.add_line(antispin_tether)

# Initialize trails
extension_trail_x = []
extension_trail_y = []
antispin_head_trail_x = []
antispin_head_trail_y = []
antispin_handle_trail_x = []
antispin_handle_trail_y = []

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

    antispin_head.set_data(antispin_head_x[frame], antispin_head_y[frame])

    # Add antispin head position to trail
    antispin_head_trail_x.append(antispin_head_x[frame])
    antispin_head_trail_y.append(antispin_head_y[frame])

    # Remove old trail points
    if len(antispin_head_trail_x) > trail_length:
        antispin_head_trail_x.pop(0)
        antispin_head_trail_y.pop(0)

    antispin_head_trail.set_data(antispin_head_trail_x, antispin_head_trail_y)

    antispin_handle.set_data(antispin_handle_x[frame], antispin_handle_y[frame])

    # Add antispin handle position to trail
    antispin_handle_trail_x.append(antispin_handle_x[frame])
    antispin_handle_trail_y.append(antispin_handle_y[frame])

    # Remove old trail points
    if len(antispin_handle_trail_x) > trail_length:
        antispin_handle_trail_x.pop(0)
        antispin_handle_trail_y.pop(0)

    antispin_handle_trail.set_data(antispin_handle_trail_x, antispin_handle_trail_y)

    antispin_tether.set_data([antispin_head_x[frame], antispin_handle_x[frame]],
                             [antispin_head_y[frame], antispin_handle_y[frame]])

    return extension_head, extension_trail, extension_tether, antispin_head, antispin_head_trail, antispin_handle, antispin_handle_trail, antispin_tether


# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# Save the animation as a GIF
writer = PillowWriter(fps=15)
ani.save("Gunslinger10PetalAntispinVsExtension.gif", writer=writer)
