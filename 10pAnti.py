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
antispin_theta_right = np.linspace(0, -8 * np.pi, num_frames)  # Anticlockwise rotation for right poi antispin

# Calculate coordinates for gunslinger antispin (first poi)
rotation_center_x = (armspan_meters / 2) * np.cos(theta)
rotation_center_y = (armspan_meters / 2) * np.sin(theta)
antispin_head_x = rotation_center_x + (radius / 2) * np.cos(antispin_theta_right)
antispin_head_y = rotation_center_y + (radius / 2) * np.sin(antispin_theta_right)
antispin_handle_x = rotation_center_x - (radius / 2) * np.cos(antispin_theta_right)
antispin_handle_y = rotation_center_y - (radius / 2) * np.sin(antispin_theta_right)

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-armspan_meters, armspan_meters)
ax.set_ylim(-armspan_meters, armspan_meters)
ax.set_aspect('equal', adjustable='box')
ax.set_title('10 Petal Antispin')
ax.set_xlabel('Head Leading')
ax.set_xticks([])
ax.set_yticks([])

# Poi elements
antispin_head, = ax.plot([], [], 'ro', markersize=10)
antispin_head_trail, = ax.plot([], [], color='r', linewidth=1.5, alpha=0.5)
antispin_handle, = ax.plot([], [], 'bo', markersize=10)
antispin_handle_trail, = ax.plot([], [], color='b', linewidth=1.5, alpha=0.5)
antispin_tether = Line2D([], [], color='k', linewidth=0.5)

ax.add_line(antispin_tether)

# Initialize trails
antispin_head_trail_x = []
antispin_head_trail_y = []
antispin_handle_trail_x = []
antispin_handle_trail_y = []

# Update function for the animation
def update(frame):
    antispin_head.set_data(antispin_head_x[frame], antispin_head_y[frame])
    antispin_handle.set_data(antispin_handle_x[frame], antispin_handle_y[frame])

    antispin_head_trail_x.append(antispin_head_x[frame])
    antispin_head_trail_y.append(antispin_head_y[frame])
    antispin_handle_trail_x.append(antispin_handle_x[frame])
    antispin_handle_trail_y.append(antispin_handle_y[frame])

    antispin_head_trail.set_data(antispin_head_trail_x, antispin_head_trail_y)
    antispin_handle_trail.set_data(antispin_handle_trail_x, antispin_handle_trail_y)

    antispin_tether.set_data([antispin_head_x[frame], antispin_handle_x[frame]],
    [antispin_head_y[frame], antispin_handle_y[frame]])

    return (antispin_head, antispin_head_trail, antispin_handle, antispin_handle_trail, antispin_tether)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# Save the animation as a GIF
writer = PillowWriter(fps=15)
ani.save("10pAntispin.gif", writer=writer)
