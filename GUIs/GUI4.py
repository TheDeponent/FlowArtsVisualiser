import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

# Constants
num_frames = 360
armspan_inches = 5 * 12 + 9  # 5'9" in inches
armspan_meters = armspan_inches * 0.0254  # Convert to meters
radius = 0.45  # Poi tether length in meters
trail_length = num_frames  # Length of the trail in frames
poi_tether = 0.45, np.linspace(0, 2 * np.pi, num_frames)  # Poi tether length in meters and angles

# Define your pattern functions here
def pattern1(poi_color, trail_color):
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
    extension_head, = ax.plot([], [], 'o', markersize=10, color=poi_color)
    extension_trail, = ax.plot([], [], color=trail_color, linewidth=1.5, alpha=0.5)
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
    anim = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

    return {
        'num_frames': num_frames,
        'poi_trail': (extension_trail_x, extension_trail_y),
        'poi_head': (extension_x, extension_y),
        'armspan_meters': armspan_meters,
        'poi_color': poi_color,
        'trail_color': trail_color,
        'trail_length': trail_length,
        'animation': anim,  # add animation object to return values
        'poi_tether': (armspan_meters / 2, theta),
    }

def pattern2(poi_color, trail_color):

    # Calculate angles
    theta_clockwise = np.linspace(0, -2 * np.pi, num_frames)  # Clockwise circle for green and yellow poi
    antispin_theta = np.linspace(0, -10 * np.pi, num_frames)  # Anticlockwise rotation for antispin

    # Calculate coordinates for gunslinger antispin (green and yellow poi)
    rotation_center_x2 = (armspan_meters / 2) * np.cos(theta_clockwise)  # Use theta_clockwise here
    rotation_center_y2 = (armspan_meters / 2) * np.sin(theta_clockwise)  # Use theta_clockwise here
    antispin_head_x2 = rotation_center_x2 + (radius / 2) * np.cos(antispin_theta)
    antispin_head_y2 = rotation_center_y2 + (radius / 2) * np.sin(antispin_theta)
    antispin_handle_x2 = rotation_center_x2 - (radius / 2) * np.cos(antispin_theta)
    antispin_handle_y2 = rotation_center_y2 - (radius / 2) * np.sin(antispin_theta)

    # Return the data
    return {
        "poi_color": poi_color,
        "trail_color": trail_color,
        "rotation_center_x2": rotation_center_x2,
        "rotation_center_y2": rotation_center_y2,
        "antispin_head_x2": antispin_head_x2,
        "antispin_head_y2": antispin_head_y2,
        "antispin_handle_x2": antispin_handle_x2,
        "antispin_handle_y2": antispin_handle_y2,
        "theta_clockwise": theta_clockwise,
        "antispin_theta": antispin_theta,
        "armspan_inches": armspan_inches,
        "armspan_meters": armspan_meters,
        "radius": radius,
        "num_frames": num_frames,
        "trail_length": trail_length,
        'poi_head': (antispin_head_x2, antispin_head_y2, antispin_handle_x2, antispin_handle_y2),
        'poi_tether': (poi_tether, theta_clockwise),
    }


def pattern3(poi_color, trail_color):

    # Calculate angles
    theta = np.linspace(0, 2 * np.pi, num_frames)
    antispin_theta = np.linspace(0, -10 * np.pi, num_frames)  # Clockwise rotation for antispin

    # Calculate coordinates for gunslinger antispin
    rotation_center_x = (armspan_meters / 2) * np.cos(theta)
    rotation_center_y = (armspan_meters / 2) * np.sin(theta)
    antispin_head_x = rotation_center_x + (radius / 2) * np.cos(antispin_theta)
    antispin_head_y = rotation_center_y + (radius / 2) * np.sin(antispin_theta)
    antispin_handle_x = rotation_center_x - (radius / 2) * np.cos(antispin_theta)
    antispin_handle_y = rotation_center_y - (radius / 2) * np.sin(antispin_theta)

    # Return the data
    return {
        "poi_color": poi_color,  # change here
        "trail_color": trail_color,
        "rotation_center_x": rotation_center_x,
        "rotation_center_y": rotation_center_y,
        "antispin_head_x": antispin_head_x,
        "antispin_head_y": antispin_head_y,
        "antispin_handle_x": antispin_handle_x,
        "antispin_handle_y": antispin_handle_y,
        "theta": theta,
        "antispin_theta": antispin_theta,
        "armspan_inches": armspan_inches,
        "armspan_meters": armspan_meters,
        "radius": radius,
        "num_frames": num_frames,
        "trail_length": trail_length,
        'poi_head': (antispin_head_x, antispin_head_y, antispin_handle_x, antispin_handle_y),
        'poi_tether': (poi_tether, theta),
    }

def pattern4(poi_color, trail_color):
    # Calculate angles
    theta = np.linspace(0, -2 * np.pi, num_frames)
    antispin_theta = np.linspace(0, -6 * np.pi, num_frames)

    # Calculate coordinates for antispin
    arm_x = (armspan_meters / 2) * np.cos(theta)
    arm_y = (armspan_meters / 2) * np.sin(theta)
    poi_x = arm_x + radius * np.cos(antispin_theta)
    poi_y = arm_y + radius * np.sin(antispin_theta)

    # Return the data
    return {
        "poi_color": poi_color,
        "trail_color": trail_color,
        "theta": theta,
        "antispin_theta": antispin_theta,
        "arm_x": arm_x,
        "arm_y": arm_y,
        "poi_x": poi_x,
        "poi_y": poi_y,
        "armspan_inches": armspan_inches,
        "armspan_meters": armspan_meters,
        "radius": radius,
        "num_frames": num_frames,
        "trail_length": trail_length,
        'poi_head': (poi_y, poi_x),
        'poi_tether': (poi_tether, theta),
    }


def submit():
    # Map pattern names to pattern functions
    patterns = {
        "Pattern 1": pattern1,
        "Pattern 2": pattern2,
        "Pattern 3": pattern3,
        "Pattern 4": pattern4
    }

    poi_color1 = poi_color_var1.get()
    trail_color1 = trail_color_var1.get()
    selected_pattern1 = pattern_var1.get()

    poi_color2 = poi_color_var2.get()
    trail_color2 = trail_color_var2.get()
    selected_pattern2 = pattern_var2.get()

    # Call the selected pattern functions with the chosen options
    pattern_data1 = patterns[selected_pattern1](poi_color1, trail_color1)
    pattern_data2 = patterns[selected_pattern2](poi_color2, trail_color2)

    # Overlay the patterns
    overlay_patterns(pattern_data1, pattern_data2)


def overlay_patterns(pattern_data1, pattern_data2):
    fig, ax = plt.subplots()
    poi1_head, = ax.plot([], [], 'o', markersize=10)
    poi2_head, = ax.plot([], [], 'o', markersize=10)
    poi1_handle, = ax.plot([], [], 'o', markersize=10)
    poi2_handle, = ax.plot([], [], 'o', markersize=10)
    if 'poi_color' in pattern_data1:
        poi1_head.set_color(pattern_data1['poi_color'])
    if 'poi_color' in pattern_data2:
        poi2_head.set_color(pattern_data2['poi_color'])

    num_frames = pattern_data1['num_frames']

    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_xlim(-pattern_data1['armspan_meters'], pattern_data1['armspan_meters'])
    ax.set_ylim(-pattern_data1['armspan_meters'], pattern_data1['armspan_meters'])
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('Pattern Overlay')
    ax.set_xticks([])
    ax.set_yticks([])

    # Poi elements for pattern 1
    poi1_head, = ax.plot([], [], 'o', markersize=10, color=pattern_data1['poi_color'])
    poi1_handle, = ax.plot([], [], 'o', markersize=10, color=pattern_data1['poi_color'])
    poi1_trail, = ax.plot([], [], color=pattern_data1['trail_color'], linewidth=1.5, alpha=0.5)
    poi1_tether = Line2D([], [], color='k', linewidth=0.5)
    ax.add_line(poi1_tether)

    # Poi elements for pattern 2
    poi2_head, = ax.plot([], [], 'o', markersize=10, color=pattern_data2['poi_color'])
    poi2_handle, = ax.plot([], [], 'o', markersize=10, color=pattern_data2['poi_color'])
    poi2_trail, = ax.plot([], [], color=pattern_data2['trail_color'], linewidth=1.5, alpha=0.5)
    poi2_tether = Line2D([], [], color='k', linewidth=0.5)
    ax.add_line(poi2_tether)

    # Initialize trails
    poi1_trail_x = []
    poi1_trail_y = []
    poi2_trail_x = []
    poi2_trail_y = []

    # Update function for the animation
    def update(frame):
        # Update pattern 1
        poi1_head.set_data(pattern_data1['poi_head'][0][frame], pattern_data1['poi_head'][1][frame])

        if len(pattern_data1['poi_head']) == 4:
            poi1_handle.set_data(pattern_data1['poi_head'][2][frame], pattern_data1['poi_head'][3][frame])

        # Add poi1 head position to trail
        poi1_trail_x.append(pattern_data1['poi_head'][0][frame])
        poi1_trail_y.append(pattern_data1['poi_head'][1][frame])

        # Remove old trail points for poi1
        if len(poi1_trail_x) > pattern_data1['trail_length']:
            poi1_trail_x.pop(0)
            poi1_trail_y.pop(0)

        poi1_trail.set_data(poi1_trail_x, poi1_trail_y)

        # Update tether for poi1
        poi1_tether.set_data([0, pattern_data1['poi_tether'][0] * np.cos(pattern_data1['poi_tether'][1][frame])],
                             [0, pattern_data1['poi_tether'][0] * np.sin(pattern_data1['poi_tether'][1][frame])])

        # Update pattern 2
        poi2_head.set_data(pattern_data2['poi_head'][0][frame], pattern_data2['poi_head'][1][frame])

        if len(pattern_data2['poi_head']) == 4:
            poi2_handle.set_data(pattern_data2['poi_head'][2][frame], pattern_data2['poi_head'][3][frame])

        # Add poi2 head position to trail
        poi2_trail_x.append(pattern_data2['poi_head'][0][frame])
        poi2_trail_y.append(pattern_data2['poi_head'][1][frame])

        # Remove old trail points for poi2
        if len(poi2_trail_x) > pattern_data2['trail_length']:
            poi2_trail_x.pop(0)
            poi2_trail_y.pop(0)

        poi2_trail.set_data(poi2_trail_x, poi2_trail_y)

        # Update tether for poi2
        poi2_tether.set_data([0, pattern_data2['poi_tether'][0] * np.cos(pattern_data2['poi_tether'][1][frame])],
                             [0, pattern_data2['poi_tether'][0] * np.sin(pattern_data2['poi_tether'][1][frame])])

        return poi1_head, poi1_trail, poi1_tether, poi2_head, poi2_trail, poi2_tether, poi1_handle, poi2_handle

    # Create the animation
    FuncAnimation(fig, update, frames=num_frames, blit=True, interval=50)

    # Display the animation
    plt.show()


# Create the tkinter GUI
root = tk.Tk()
root.title("Poi Pattern Visualizer")

# Create and grid the labels, entries, and buttons
pattern_var = tk.StringVar(root)
pattern_var.set("Pattern 1")  # Set default pattern
poi_color_var = tk.StringVar(root)
poi_color_var.set("#00FF00")  # Set default poi color
trail_color_var = tk.StringVar(root)
trail_color_var.set("#FF00FF")  # Set default trail color

ttk.Label(root, text="Pattern 1").grid(row=0, column=0, sticky=tk.W)
pattern_var1 = tk.StringVar(root)
pattern_var1.set("Pattern 1")  # Set default pattern
ttk.Combobox(root, textvariable=pattern_var1, values=("Pattern 1", "Pattern 2", "Pattern 3", "Pattern 4")).grid(row=0,
                                                                                                                column=1)

ttk.Label(root, text="Poi Color 1").grid(row=1, column=0, sticky=tk.W)
poi_color_var1 = tk.StringVar(root)
poi_color_var1.set("#00FF00")  # Set default poi color
ttk.Entry(root, textvariable=poi_color_var1).grid(row=1, column=1)

ttk.Label(root, text="Trail Color 1").grid(row=2, column=0, sticky=tk.W)
trail_color_var1 = tk.StringVar(root)
trail_color_var1.set("#FF00FF")  # Set default trail color
ttk.Entry(root, textvariable=trail_color_var1).grid(row=2, column=1)

ttk.Label(root, text="Pattern 2").grid(row=4, column=0, sticky=tk.W)
pattern_var2 = tk.StringVar(root)
pattern_var2.set("Pattern 1")  # Set default pattern
ttk.Combobox(root, textvariable=pattern_var2, values=("Pattern 1", "Pattern 2", "Pattern 3", "Pattern 4")).grid(row=4,
                                                                                                                column=1)

ttk.Label(root, text="Poi Color 2").grid(row=5, column=0, sticky=tk.W)
poi_color_var2 = tk.StringVar(root)
poi_color_var2.set("#00FF00")  # Set default poi color
ttk.Entry(root, textvariable=poi_color_var2).grid(row=5, column=1)

ttk.Label(root, text="Trail Color 2").grid(row=6, column=0, sticky=tk.W)
trail_color_var2 = tk.StringVar(root)
trail_color_var2.set("#FF00FF")  # Set default trail color
ttk.Entry(root, textvariable=trail_color_var2).grid(row=6, column=1)

ttk.Button(root, text="Submit", command=submit).grid(row=8, columnspan=2)

root.mainloop()
