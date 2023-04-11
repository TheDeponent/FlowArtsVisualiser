import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D


def generate_Cateye(fig, ax):
    # Parameters
    num_frames = 360
    armspan_inches = 5 * 12 + 9  # 5'9" in inches
    armspan_meters = armspan_inches * 0.0254  # Convert to meters
    radius = 0.45  # poi tether length in meters
    trail_length = num_frames  # Length of the trail in frames
    start_position = np.pi

    # Set start position
    start_position = {'right': 0, 'left': np.pi}
    start_theta = start_position[start_side]
    rotation_multiplier = {'anticlockwise': -1, 'clockwise': 1}
    rotation_direction_multiplier = rotation_multiplier[rotation_direction]

    # Calculate angles
    theta_1 = np.linspace(start_theta, start_theta -2 * (rotation_direction_multiplier * np.pi), num_frames)  # -np.pi to change SPIN DIRECTION, offset of np.pi, np.pi to change STARTING LOCATION
    theta_2 = theta_1 + np.pi

    # Calculate coordinates
    a = (armspan_meters / np.pi) * np.cos(np.pi / 3)
    b = (armspan_meters / np.pi) * np.sin(np.pi / 3)
    rotation_center_x = a * np.cos(theta_1)
    rotation_center_y = b * np.sin(theta_1)

    # Poi head clockwise ellipse motion
    poi_head_x = rotation_center_x + radius * np.cos(theta_2)
    poi_head_y = rotation_center_y - radius * np.sin(theta_2)

    # Poi handle counterclockwise circle
    poi_handle_x = poi_head_x - radius * np.cos(theta_1)
    poi_handle_y = poi_head_y - radius * np.sin(theta_1)

    # Set up the plot
    ax.set_xlim(-armspan_meters, armspan_meters)
    ax.set_ylim(-armspan_meters, armspan_meters)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('Cat Eye')
    ax.set_xlabel('Head Leading')
    ax.set_xticks([])
    ax.set_yticks([])

    # Poi elements
    poi_head, = ax.plot([], [], 'go', markersize=10)
    poi_head_trail, = ax.plot([], [], color='g', linewidth=1.5, alpha=0.5)
    poi_handle, = ax.plot([], [], 'yo', markersize=10, alpha=0.5)
    poi_handle_trail, = ax.plot([], [], color='y', linewidth=1.5, alpha=0.5)
    poi_tether = Line2D([], [], color='k', linewidth=0.5)

    ax.add_line(poi_tether)

    # Initialize trails
    poi_head_trail_x = []
    poi_head_trail_y = []
    poi_handle_trail_x = []
    poi_handle_trail_y = []

    # Update function for the animation
    def update(frame):
        poi_head.set_data((poi_head_x[frame], poi_head_y[frame]))
        poi_handle.set_data((poi_handle_x[frame], poi_handle_y[frame]))

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

    ani = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)
    return ax, update, (poi_head, poi_head_trail, poi_handle, poi_handle_trail, poi_tether), ani


if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax, update, elements, ani = generate_Cateye(fig, ax)
    fig.ani = ani  # Store the animation object as an attribute of the figure

    # Show the CatEye pattern
    plt.show()