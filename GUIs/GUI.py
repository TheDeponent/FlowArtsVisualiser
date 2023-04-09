import tkinter as tk
from tkinter import ttk

# Import necessary libraries from your existing scripts
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
import math

# Define your pattern functions here
def pattern1(poi_color, trail_color, hand):
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
    ani = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

    # Display the animation
    plt.show()

def pattern2(poi_color, trail_color, hand):
    # Parameters
    num_frames = 360
    armspan_inches = 5 * 12 + 9  # 5'9" in inches
    armspan_meters = armspan_inches * 0.0254  # Convert to meters
    radius = 0.45  # Poi tether length in meters
    trail_length = num_frames  # Length of the trail in frames

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

    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_xlim(-armspan_meters, armspan_meters)
    ax.set_ylim(-armspan_meters, armspan_meters)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('8 Petal Inspin')
    ax.set_xlabel('Head Leading')
    ax.set_xticks([])
    ax.set_yticks([])

    # Poi elements
    antispin_head2, = ax.plot([], [], 'o', markersize=10, color=poi_color)
    antispin_head_trail2, = ax.plot([], [], color=trail_color, linewidth=1.5, alpha=0.5)
    antispin_handle2, = ax.plot([], [], 'o', markersize=10, color=poi_color)
    antispin_handle_trail2, = ax.plot([], [], color=trail_color, linewidth=1.5, alpha=0.5)
    antispin_tether2 = Line2D([], [], color='k', linewidth=0.5)

    ax.add_line(antispin_tether2)

    # Initialize trails
    antispin_head_trail_x2 = []
    antispin_head_trail_y2 = []
    antispin_handle_trail_x2 = []
    antispin_handle_trail_y2 = []

    # Update function for the animation
    def update(frame):
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

        return (antispin_head2, antispin_head_trail2, antispin_handle2, antispin_handle_trail2, antispin_tether2)

    # Create the animation
    ani2 = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

    # Display the animation
    plt.show()


def pattern3(poi_color, trail_color, hand):
    # Add the code for pattern 3 here, with the necessary modifications
    # Replace hardcoded colors with poi_color and trail_color
    # Adjust the code for the selected hand if necessary
    # Parameters
    num_frames = 360
    armspan_inches = 5 * 12 + 9  # 5'9" in inches
    armspan_meters = armspan_inches * 0.0254  # Convert to meters
    radius = 0.45  # Poi tether length in meters
    trail_length = num_frames  # Length of the trail in frames

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

    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_xlim(-armspan_meters, armspan_meters)
    ax.set_ylim(-armspan_meters, armspan_meters)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('12 Petal Antispin Flower')
    ax.set_xlabel('Head leading')
    ax.set_xticks([])
    ax.set_yticks([])

    # Poi elements
    antispin_head, = ax.plot([], [], 'o', markersize=10, color=poi_color)
    antispin_head_trail, = ax.plot([], [], color=trail_color, linewidth=1.5, alpha=0.5)
    antispin_handle, = ax.plot([], [], 'o', markersize=10, color=poi_color)
    antispin_handle_trail, = ax.plot([], [], color=trail_color, linewidth=1.5, alpha=0.5)
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

        return antispin_head, antispin_head_trail, antispin_handle, antispin_handle_trail, antispin_tether

    # Create the animation
    ani3 = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

    # Display the animation
    plt.show()

def pattern4(poi_color, trail_color, hand):
    # Parameters
    num_frames = 360
    armspan_inches = 5 * 12 + 9  # 5'9" in inches
    armspan_meters = armspan_inches * 0.0254  # Convert to meters
    radius = 0.45  # Poi tether length in meters
    trail_length = num_frames  # Length of the trail in frames

    # Calculate angles
    theta = np.linspace(0, -2 * np.pi, num_frames)
    antispin_theta = np.linspace(0, -6 * np.pi, num_frames)

    # Calculate coordinates for antispin
    arm_x = (armspan_meters / 2) * np.cos(theta)
    arm_y = (armspan_meters / 2) * np.sin(theta)
    poi_x = arm_x + radius * np.cos(antispin_theta)
    poi_y = arm_y + radius * np.sin(antispin_theta)

    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_xlim(-armspan_meters, armspan_meters)
    ax.set_ylim(-armspan_meters, armspan_meters)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('2 Petal Inspin')
    ax.set_xlabel('Head Leading')
    ax.set_xticks([])
    ax.set_yticks([])

    # Poi elements
    poi_head, = ax.plot([], [], 'o', markersize=10, color=poi_color)
    poi_trail, = ax.plot([], [], color=trail_color, linewidth=1.5, alpha=0.5)
    poi_tether = Line2D([], [], color='k', linewidth=0.5)

    ax.add_line(poi_tether)

    # Initialize trails
    poi_trail_x = []
    poi_trail_y = []

    # Update function for the animation
    def update(frame):
        poi_head.set_data(poi_x[frame], poi_y[frame])

        # Add poi head position to trail
        poi_trail_x.append(poi_x[frame])
        poi_trail_y.append(poi_y[frame])

        # Remove old trail points
        if len(poi_trail_x) > trail_length:
            poi_trail_x.pop(0)
            poi_trail_y.pop(0)

        poi_trail.set_data(poi_trail_x, poi_trail_y)

        poi_tether.set_data([arm_x[frame], poi_x[frame]], [arm_y[frame], poi_y[frame]])

        return poi_head, poi_trail, poi_tether

    # Create the animation
    ani4 = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

    # Display the animation
    plt.show()


def submit():
    # Map pattern names to pattern functions
    patterns = {
        "Pattern 1": pattern1,
        "Pattern 2": pattern2,
        "Pattern 3": pattern3,
        "Pattern 4": pattern4
    }

    poi_color = poi_color_var.get()
    trail_color = trail_color_var.get()
    hand = hand_var.get()
    selected_pattern = pattern_var.get()

    # Call the selected pattern function with the chosen options
    patterns[selected_pattern](poi_color, trail_color, hand)


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
hand_var = tk.StringVar(root)
hand_var.set("Both")  # Set default hand

ttk.Label(root, text="Pattern:").grid(column=0, row=0)
ttk.OptionMenu(root, pattern_var, *["Pattern 1", "Pattern 2", "Pattern 3", "Pattern 4"]).grid(column=1, row=0)
ttk.Label(root, text="Poi Color:").grid(column=0, row=1)
ttk.Entry(root, textvariable=poi_color_var).grid(column=1, row=1)
ttk.Label(root, text="Trail Color:").grid(column=0, row=2)
ttk.Entry(root, textvariable=trail_color_var).grid(column=1, row=2)
ttk.Label(root, text="Hand:").grid(column=0, row=3)
ttk.OptionMenu(root, hand_var, "Both", "Left", "Right").grid(column=1, row=3)

ttk.Button(root, text="Visualize", command=submit).grid(column=0, row=4, columnspan=2)

root.mainloop()
