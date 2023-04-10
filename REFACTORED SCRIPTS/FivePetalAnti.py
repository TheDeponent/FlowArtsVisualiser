import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

def generate_FivePetalAnti(fig, ax):
    # Parameters
    num_frames = 360
    armspan_inches = 5 * 12 + 9  # 5'9" in inches
    armspan_meters = armspan_inches * 0.0254  # Convert to meters
    radius = 0.45  # poi tether length in meters
    trail_length = num_frames  # Length of the trail in frames

    # Calculate angles
    theta_1 = np.linspace(0, -2 * np.pi, num_frames)
    theta_2 = -4 * theta_1 + (np.pi / 2)

    # Calculate coordinates
    rotation_center_x = (armspan_meters / 2) * np.cos(theta_1)
    rotation_center_y = (armspan_meters / 2) * np.sin(theta_1)
    poi_head_x = rotation_center_x + radius * np.cos(theta_2)
    poi_head_y = rotation_center_y + radius * np.sin(theta_2)
    poi_handle_x = poi_head_x + radius * np.cos(theta_2 + np.pi)
    poi_handle_y = poi_head_y + radius * np.sin(theta_2 + np.pi)

    # Set up the plot
    ax.set_xlim(-armspan_meters, armspan_meters)
    ax.set_ylim(-armspan_meters, armspan_meters)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('5 Petal Antispin')
    ax.set_xlabel('Head Leading')
    ax.set_xticks([])
    ax.set_yticks([])

    # Poi elements
    poi_head, = ax.plot([], [], 'ro', markersize=10)
    poi_head_trail, = ax.plot([], [], color='r', linewidth=1.5, alpha=0.5)
    poi_handle, = ax.plot([], [], 'bo', markersize=10)
    poi_handle_trail, = ax.plot([], [], color='g', linewidth=1.5, alpha=0, visible=False)
    poi_tether = Line2D([], [], color='k', linewidth=0.5)

    ax.add_line(poi_tether)

    # Initialize trails
    poi_head_trail_x = []
    poi_head_trail_y = []
    poi_handle_trail_x = []
    poi_handle_trail_y = []

    # Update function for the animation
    def update(frame):
        poi_head.set_data(poi_head_x[frame], poi_head_y[frame])
        poi_handle.set_data(poi_handle_x[frame], poi_handle_y[frame])

        poi_head_trail_x.append(poi_head_x[frame])
        poi_head_trail_y.append(poi_head_y[frame])
        poi_handle_trail_x.append(poi_handle_x[frame])
        poi_handle_trail_y.append(poi_handle_y[frame])

        if frame == 0:
            poi_head_trail_x.clear()
            poi_head_trail_y.clear()
            poi_handle_trail_x.clear()
            poi_handle_trail_y.clear()

        poi_head_trail.set_data(poi_head_trail_x[-trail_length:], poi_head_trail_y[-trail_length:])
        poi_handle_trail.set_data(poi_handle_trail_x[-trail_length:], poi_handle_trail_y[-trail_length:])

        poi_tether.set_data([poi_head_x[frame], poi_handle_x[frame]],
                            [poi_head_y[frame], poi_handle_y[frame]])

        return (poi_head, poi_head_trail, poi_handle, poi_handle_trail, poi_tether)

    # Create the animation
    ani = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

    return ax, update, (poi_head, poi_head_trail, poi_handle, poi_handle_trail, poi_tether)