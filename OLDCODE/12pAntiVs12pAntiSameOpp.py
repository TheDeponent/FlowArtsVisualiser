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
theta_clockwise = np.linspace(np.pi, -1 * np.pi, num_frames)  # Clockwise circle with a shift for green and yellow poi
antispin_theta = np.linspace(0, -10 * np.pi, num_frames)  # Anticlockwise rotation for antispin
antispin_theta2 = np.linspace(0, 10 * np.pi, num_frames)  # Clockwise rotation with a phase shift for Head leading on both sides

# Calculate coordinates for gunslinger antispin (first poi)
rotation_center_x = (armspan_meters / 2) * np.cos(theta)
rotation_center_y = (armspan_meters / 2) * np.sin(theta)
antispin_head_x = rotation_center_x + (radius / 2) * np.cos(antispin_theta)
antispin_head_y = rotation_center_y + (radius / 2) * np.sin(antispin_theta)
antispin_handle_x = rotation_center_x - (radius / 2) * np.cos(antispin_theta)
antispin_handle_y = rotation_center_y - (radius / 2) * np.sin(antispin_theta)

# Calculate coordinates for gunslinger antispin (green and yellow poi)
rotation_center_x2 = (armspan_meters / 2) * np.cos(theta_clockwise)  # Use theta_clockwise here
rotation_center_y2 = (armspan_meters / 2) * np.sin(theta_clockwise)  # Use theta_clockwise here
antispin_head_x2 = rotation_center_x2 + (radius / 2) * np.cos(antispin_theta2)  # Use antispin_theta2 here
antispin_head_y2 = rotation_center_y2 + (radius / 2) * np.sin(antispin_theta2)  # Use antispin_theta2 here
antispin_handle_x2 = rotation_center_x2 - (radius / 2) * np.cos(antispin_theta2)  # Use antispin_theta2 here
antispin_handle_y2 = rotation_center_y2 - (radius / 2) * np.sin(antispin_theta2)  # Use antispin_theta2 here

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-armspan_meters, armspan_meters)
ax.set_ylim(-armspan_meters, armspan_meters)
ax.set_aspect('equal', adjustable='box')
ax.set_title('12 Petal Antispin vs 12 Petal Antispin - Same Time Opposite Direction')
ax.set_xlabel('Head Leading v Head Leading')
ax.set_xticks([])
ax.set_yticks([])

# Poi elements
antispin_head, = ax.plot([], [], 'ro', markersize=10)
antispin_head_trail, = ax.plot([], [], color='r', linewidth=1.5, alpha=0.5)
antispin_handle, = ax.plot([], [], 'bo', markersize=10)
antispin_handle_trail, = ax.plot([], [], color='b', linewidth=1.5, alpha=0.5)
antispin_tether = Line2D([], [], color='k', linewidth=0.5)

antispin_head2, = ax.plot([], [], 'go', markersize=10)
antispin_head_trail2, = ax.plot([], [], color='g', linewidth=1.5, alpha=0.5)
antispin_handle2, = ax.plot([], [], 'yo', markersize=10)
antispin_handle_trail2, = ax.plot([], [], color='y', linewidth=1.5, alpha=0.5)
antispin_tether2 = Line2D([], [], color='k', linewidth=0.5)

ax.add_line(antispin_tether)
ax.add_line(antispin_tether2)

# Initialize trails
antispin_head_trail_x = []
antispin_head_trail_y = []
antispin_handle_trail_x = []
antispin_handle_trail_y = []
antispin_head_trail_x2 = []
antispin_head_trail_y2 = []
antispin_handle_trail_x2 = []
antispin_handle_trail_y2 = []

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

    antispin_head2.set_data(antispin_head_x2[frame], antispin_head_y2[frame])
    antispin_handle2.set_data(antispin_handle_x2[frame], antispin_handle_y2[frame])

    antispin_head_trail_x2.append(antispin_head_x2[frame])
    antispin_head_trail_y2.append(antispin_head_y2[frame])
    antispin_handle_trail_x2.append(antispin_handle_x2[frame])
    antispin_handle_trail_y2.append(antispin_handle_y2[frame])

    antispin_head_trail2.set_data(antispin_head_trail_x2, antispin_head_trail_y2)
    antispin_handle_trail2.set_data(antispin_handle_trail_x2, antispin_handle_trail_y2)

    antispin_tether2.set_data([antispin_head_x2[frame], antispin_handle_x2[frame]],
                              [antispin_head_y2[frame], antispin_handle_y2[frame]])

    return (antispin_head, antispin_head_trail, antispin_handle, antispin_handle_trail, antispin_tether,
            antispin_head2, antispin_head_trail2, antispin_handle2, antispin_handle_trail2, antispin_tether2)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# Save the animation as a GIF
writer = PillowWriter(fps=15)
ani.save("12pAntispinVs12pAntiSpinSameOpp.gif", writer=writer)
