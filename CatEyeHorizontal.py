import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

#FUCK THIS PATTERN IN PARTICULAR.

def generate_CateyeH(fig, ax, head_color, handle_color, start_side='left', rotation_direction='clockwise'):
    # Parameters
    num_frames = 360
    armspan_inches = 5 * 12 + 9  # 5'9" in inches
    armspan_meters = armspan_inches * 0.0254  # Convert to meters
    radius = 0.45  # poi tether length in meters
    trail_length = num_frames  # Length of the trail in frames

    # Set start position
    rotation_multiplier = {'clockwise': -1, 'anticlockwise': 1}
    rotation_direction_multiplier = rotation_multiplier[rotation_direction]
    start_position = {'left': 0, 'right': np.pi}
    start_theta = start_position[start_side] + rotation_direction_multiplier * (0.25 * 2 * np.pi)  # Added a 1/4 of the total rotation

    # Calculate angles
    theta_1 = np.linspace(start_theta, start_theta -2 * (rotation_direction_multiplier * np.pi), num_frames)  # -np.pi to change SPIN DIRECTION, offset of np.pi, np.pi to change STARTING LOCATION
    theta_2 = theta_1 + np.pi

    # Calculate coordinates
    a = (armspan_meters / np.pi) * np.cos(np.pi / 3)
    b = (armspan_meters / np.pi) * np.sin(np.pi / 3)
    rotation_center_y = a * np.cos(theta_1)
    rotation_center_x = b * np.sin(theta_1)

    # Poi head clockwise ellipse motion
    poi_head_y = rotation_center_y + radius * np.cos(theta_2)
    poi_head_x = rotation_center_x - radius * np.sin(theta_2)

    # Poi handle counterclockwise circle
    poi_handle_y = poi_head_y - radius * np.cos(theta_1)
    poi_handle_x = poi_head_x - radius * np.sin(theta_1)

    # Set up the plot
    ax.set_xlim(-armspan_meters, armspan_meters)
    ax.set_ylim(-armspan_meters, armspan_meters)
    ax.set_aspect('equal', adjustable='box')
    title = "Horizontal Catseye"
    xlabel = "Head Leading"
    ax.set_xticks([])
    ax.set_yticks([])

    # Poi elements
    poi_head, = ax.plot([], [], 'go', markersize=10, alpha=1, color=head_color)
    poi_head_trail, = ax.plot([], [], linewidth=1.5, alpha=0.5, color=head_color)
    poi_handle, = ax.plot([], [], 'yo', markersize=10, alpha=1, color=handle_color)
    poi_handle_trail, = ax.plot([], [], linewidth=1.5, alpha=0.0, color=handle_color)
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

    return ax, update, (poi_head, poi_head_trail, poi_handle, poi_handle_trail, poi_tether), title, xlabel, start_side, rotation_direction
