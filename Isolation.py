import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
def generate_Isolation(fig, ax, head_color, handle_color, start_side='left', rotation_direction='clockwise'):
    # Parameters
    num_frames = 360
    armspan_inches = 5 * 12 + 9  # 5'9" in inches
    armspan_meters = armspan_inches * 0.0254  # Convert to meters
    radius = 0.225  # poi tether length in meters
    trail_length = num_frames  # Length of the trail in frames

    # Set rotation direction
    rotation_multiplier = {'clockwise': -1, 'anticlockwise': 1}
    rotation_direction_multiplier = rotation_multiplier[rotation_direction]

    # Calculate angles
    theta_1 = np.linspace(0, 2 * np.pi, num_frames)

    # Calculate coordinates
    center_x = np.zeros(num_frames)  # Set center x-coordinate to 0
    center_y = np.zeros(num_frames)  # Set center y-coordinate to 0
    poi_head_x = radius * np.cos(theta_1)
    poi_head_y = radius * np.sin(theta_1)
    poi_handle_x = -radius * np.cos(theta_1)
    poi_handle_y = -radius * np.sin(theta_1)

    # Set up the plot
    ax.set_xlim(-armspan_meters, armspan_meters)
    ax.set_ylim(-armspan_meters, armspan_meters)
    ax.set_aspect('equal', adjustable='box')
    title = "Static Spin"
    xlabel= "Head Leading"
    ax.set_xticks([])
    ax.set_yticks([])

    # Poi elements
    poi_head, = ax.plot([], [], 'go', markersize=10, alpha=1, color=head_color)
    poi_head_trail, = ax.plot([], [], linewidth=1.5, alpha=0.5, color=head_color)
    poi_handle, = ax.plot([], [], 'yo', markersize=10, alpha=1, color=handle_color)
    poi_handle_trail, = ax.plot([], [], linewidth=1.5, alpha=0.5, color=handle_color)
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

    return ax, update, (
    poi_head, poi_head_trail, poi_handle, poi_handle_trail, poi_tether), title, xlabel, start_side, rotation_direction