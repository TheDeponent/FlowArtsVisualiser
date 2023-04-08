import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def angel_roll(t, shoulder_width, staff_length):
    x_movement = shoulder_width * (1 - 2 * t)
    angle = -np.pi * t
    return x_movement, angle

fig, ax = plt.subplots()
performer_height_inches = 69
performer_height_cm = performer_height_inches * 2.54
armspan = performer_height_cm
shoulder_width = armspan / 2
staff_length = 85

x_data, y_data = [], []
ln_blue, = plt.plot([], [], 'bo', markersize=8)
ln_green, = plt.plot([], [], 'go', markersize=8)
ln_staff, = plt.plot([], [], 'r-', linewidth=2)

def init():
    ax.set_xlim(-armspan, armspan)
    ax.set_ylim(-armspan, armspan)
    ax.set_aspect('equal')
    ax.set_title("Angel Roll")  # Add title
    ax.set_xticks([])  # Remove x-axis number tags
    ax.set_yticks([])  # Remove y-axis number tags
    ax.set_xlabel("Armspan 5'9, Staff 85cm")  # Label x-axis
    ax.plot([-shoulder_width, shoulder_width], [0, 0], 'k-', linewidth=2)
    return ln_blue, ln_green, ln_staff

def update(frame):
    x, angle = angel_roll(frame, shoulder_width, staff_length)
    x_blue = x - staff_length / 2 * np.cos(angle)
    y_blue = -staff_length / 2 * np.sin(angle)
    x_green = x + staff_length / 2 * np.cos(angle)
    y_green = staff_length / 2 * np.sin(angle)
    ln_blue.set_data(x_blue, y_blue)
    ln_green.set_data(x_green, y_green)
    ln_staff.set_data([x_blue, x_green], [y_blue, y_green])
    return ln_blue, ln_green, ln_staff

ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 100),
                    init_func=init, blit=True, interval=100)

# Save the animation as a GIF
writer = PillowWriter(fps=24)
ani.save("angel_roll.gif", writer=writer)
