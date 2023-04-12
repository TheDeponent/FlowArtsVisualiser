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

# Calculate coordinates for gunslinger antispin on both hands
rotation_center_x = (armspan_meters / 2) * np.cos(theta)
rotation_center_y = (armspan_meters / 2) * np.sin(theta)
right_antispin_head_x = rotation_center_x + (radius / 2) * np.cos(antispin_theta)
right_antispin_head_y = rotation_center_y + (radius / 2) * np.sin(antispin_theta)
right_antispin_handle_x = rotation_center_x - (radius / 2) * np.cos(antispin_theta)
right_antispin_handle_y = rotation_center_y - (radius / 2) * np.sin(antispin_theta)
left_antispin_head_x = rotation_center_x + (radius / 2) * np.cos(-antispin_theta)
left_antispin_head_y = rotation_center_y + (radius / 2) * np.sin(-antispin_theta)
left_antispin_handle_x = rotation_center_x - (radius / 2) * np.cos(-antispin_theta)
left_antispin_handle_y = rotation_center_y - (radius / 2) * np.sin(-antispin_theta)

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-armspan_meters, armspan_meters)
ax.set_ylim(-armspan_meters, armspan_meters)
ax.set_aspect('equal', adjustable='box')
ax.set_title('12 Petal Antispin vs 8 Petal Inspin - Same Time Same direction')
ax.set_xlabel('Head leading vs Handle leading')
ax.set_xticks([])
ax.set_yticks([])

# Poi elements
right_antispin_head, = ax.plot([], [], 'ro', markersize=10)
right_antispin_head_trail, = ax.plot([], [], color='r', linewidth=1.5, alpha=0.5)
right_antispin_handle, = ax.plot([], [], 'bo', markersize=10)
right_antispin_handle_trail, = ax.plot([], [], color='b', linewidth=1.5, alpha=0.5)
right_antispin_tether = Line2D([], [], color='k', linewidth=0.5)
left_antispin_head, = ax.plot([], [], 'go', markersize=10)
left_antispin_head_trail, = ax.plot([], [], color='g', linewidth=1.5, alpha=0.5)
left_antispin_handle, = ax.plot([], [], 'yo', markersize=10)
left_antispin_handle_trail, = ax.plot([], [], color='y', linewidth=1.5, alpha=0.5)
left_antispin_tether = Line2D([], [], color='k', linewidth=0.5)

ax.add_line(right_antispin_tether)
ax.add_line(left_antispin_tether)

# Initialize trails
right_antispin_head_trail_x = []
right_antispin_head_trail_y = []
right_antispin_handle_trail_x = []
right_antispin_handle_trail_y = []
left_antispin_head_trail_x = []
left_antispin_head_trail_y = []
left_antispin_handle_trail_x = []
left_antispin_handle_trail_y = []

# Update function for the animation
def update(frame):
    right_antispin_head.set_data(right_antispin_head_x[frame],
    right_antispin_head_y[frame])

    # Add right antispin head position to trail
    right_antispin_head_trail_x.append(right_antispin_head_x[frame])
    right_antispin_head_trail_y.append(right_antispin_head_y[frame])

    # Remove old trail points
    if len(right_antispin_head_trail_x) > trail_length:
        right_antispin_head_trail_x.pop(0)
        right_antispin_head_trail_y.pop(0)

    right_antispin_head_trail.set_data(right_antispin_head_trail_x, right_antispin_head_trail_y)

    right_antispin_handle.set_data(right_antispin_handle_x[frame], right_antispin_handle_y[frame])

    # Add right antispin handle position to trail
    right_antispin_handle_trail_x.append(right_antispin_handle_x[frame])
    right_antispin_handle_trail_y.append(right_antispin_handle_y[frame])

    # Remove old trail points
    if len(right_antispin_handle_trail_x) > trail_length:
        right_antispin_handle_trail_x.pop(0)
        right_antispin_handle_trail_y.pop(0)

    right_antispin_handle_trail.set_data(right_antispin_handle_trail_x, right_antispin_handle_trail_y)

    right_antispin_tether.set_data([right_antispin_head_x[frame], right_antispin_handle_x[frame]],
                                   [right_antispin_head_y[frame], right_antispin_handle_y[frame]])

    left_antispin_head.set_data(left_antispin_head_x[frame], left_antispin_head_y[frame])

    # Add left antispin head position to trail
    left_antispin_head_trail_x.append(left_antispin_head_x[frame])
    left_antispin_head_trail_y.append(left_antispin_head_y[frame])

    # Remove old trail points
    if len(left_antispin_head_trail_x) > trail_length:
        left_antispin_head_trail_x.pop(0)
        left_antispin_head_trail_y.pop(0)

    left_antispin_head_trail.set_data(left_antispin_head_trail_x, left_antispin_head_trail_y)

    left_antispin_handle.set_data(left_antispin_handle_x[frame], left_antispin_handle_y[frame])

    # Add left antispin handle position to trail
    left_antispin_handle_trail_x.append(left_antispin_handle_x[frame])
    left_antispin_handle_trail_y.append(left_antispin_handle_y[frame])

    # Remove old trail points
    if len(left_antispin_handle_trail_x) > trail_length:
        left_antispin_handle_trail_x.pop(0)
        left_antispin_handle_trail_y.pop(0)

    left_antispin_handle_trail.set_data(left_antispin_handle_trail_x, left_antispin_handle_trail_y)
    left_antispin_tether.set_data([left_antispin_head_x[frame], left_antispin_handle_x[frame]],
                                  [left_antispin_head_y[frame], left_antispin_handle_y[frame]])

    return (right_antispin_head, right_antispin_head_trail, right_antispin_handle, right_antispin_handle_trail,
            right_antispin_tether, left_antispin_head, left_antispin_head_trail, left_antispin_handle,
            left_antispin_handle_trail, left_antispin_tether)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# Save the animation as a GIF
writer = PillowWriter(fps=15)
ani.save("12PetalAntispinVs8PetalInspinSameSame.gif", writer=writer)
