import os
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import colorchooser
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
from ThreePetalAnti import generate_ThreePetalAnti
from FivePetalAnti import generate_FivePetalAnti
from TenPetalAnti import generate_TenPetalAnti
from TwelvePetalAnti import generate_TwelvePetalAnti
from EightPetalInspin import generate_EightPetalIn
from FourPetalAnti import generate_FourPetalAnti
from TwoPetalInspin import generate_TwoPetalInspin
from FourPetalInspin import generate_FourPetalInspin
from CatEye import generate_Cateye
from Extension import generate_Extension
from TwoPetalInspinVertical import generate_TwoPetalInspinV
from StaticSpin import generate_StaticSpin
from StaticPendulum import generate_StaticPendulum
from Pendulum import generate_Pendulum
from ExtendedPendulum import generate_ExtendedPendulum

# List of available patterns
patterns = {
    "Extension": generate_Extension,
    "CatEye": generate_Cateye,
    "Static Spin": generate_StaticSpin,
    "Static Pendulum": generate_StaticPendulum,
    "Pendulum": generate_Pendulum,
    "Extended Pendulum": generate_ExtendedPendulum,
    "12 Petal Antispin (Gunslinger)": generate_TwelvePetalAnti,
    "10 Petal Antispin (Gunslinger)": generate_TenPetalAnti,
    "8 Petal Inspin (Gunslinger)": generate_EightPetalIn,
    "5 Petal Antispin": generate_FivePetalAnti,
    "4 Petal Antispin": generate_FourPetalAnti,
    "4 Petal Inspin": generate_FourPetalInspin,
    "3 Petal Antispin (Triquetra)": generate_ThreePetalAnti,
    "2 Petal Inspin (Horizontal)": generate_TwoPetalInspin,
    "2 Petal Inspin (Vertical)": generate_TwoPetalInspinV
}

ani = None  # Add this line
def choose_color(color_variable, color_display):
    color = colorchooser.askcolor(color_variable.get())[1]
    if color:
        color_variable.set(color)
        color_display.config(bg=color)

def combine_selected_patterns():
    global ani, title1, title2
    # Get the selected patterns
    pattern1_name = selected_pattern1.get()
    pattern2_name = selected_pattern2.get()
    pattern1 = patterns[pattern1_name]
    pattern2 = patterns[pattern2_name]

    # Get the selected colors
    head_color1 = poi_head_color1.get()
    handle_color1 = poi_handle_color1.get()
    head_color2 = poi_head_color2.get()
    handle_color2 = poi_handle_color2.get()

    # Get start side and rotation direction for both patterns
    start_side1 = start_side1_var.get()
    rotation_direction1 = rotation_direction1_var.get()
    start_side2 = start_side2_var.get()
    rotation_direction2 = rotation_direction2_var.get()

    # Generate the plots for the two patterns
    fig, ax = plt.subplots()
    ax1, update1, elements1, title1, xlabel1, _, _ = pattern1(fig, ax, head_color1, handle_color1, start_side1, rotation_direction1)
    ax2, update2, elements2, title2, xlabel2, _, _ = pattern2(fig, ax, head_color2, handle_color2, start_side2, rotation_direction2)

    # Define a combined update function for the animation
    def combined_update(frame):
        return update1(frame) + update2(frame)

    # Create the animation
    num_frames = 360
    ani = FuncAnimation(fig, combined_update, frames=num_frames, interval=20, blit=True)

    # Set the title of the combined graph
    fig.suptitle(f"{title1} vs {title2}")

    # Set the combined x-axis label
    conditions = (start_side1 == start_side2, rotation_direction1 == rotation_direction2)
    title_map = {
        (True, True): "Same Time Same Direction",
        (True, False): "Same Time Opposite Direction",
        (False, True): "Split Time Same Direction",
        (False, False): "Split Time Opposite Direction",
    }

    ax.set_xlabel(title_map[conditions])

    # Show the plot
    plt.show()

# Create the main window
root = tk.Tk()
root.title("Pattern Combiner")

poi_head_color1 = tk.StringVar(value='green')
poi_handle_color1 = tk.StringVar(value='purple')
poi_head_color2 = tk.StringVar(value='blue')
poi_handle_color2 = tk.StringVar(value='red')

# Create labels and dropdown menus for selecting patterns
tk.Label(root, text="Left Hand").grid(row=0, column=0)
selected_pattern1 = tk.StringVar()
pattern1_menu = ttk.Combobox(root, textvariable=selected_pattern1, values=list(patterns.keys()))
pattern1_menu.grid(row=0, column=1)
pattern1_menu.current(0)

tk.Label(root, text="Right Hand").grid(row=1, column=0)
selected_pattern2 = tk.StringVar()
pattern2_menu = ttk.Combobox(root, textvariable=selected_pattern2, values=list(patterns.keys()))
pattern2_menu.grid(row=1, column=1)
pattern2_menu.current(0)

# Color selection for poi head (Pattern 1)
tk.Label(root, text="Poi Head Color (Left Hand):").grid(row=2, column=0)
poi_head_color_display = tk.Label(root, bg=poi_head_color1.get(), width=10)
poi_head_color_display.grid(row=2, column=1)
poi_head_color_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(poi_head_color1, poi_head_color_display))
poi_head_color_button.grid(row=2, column=2)

# Color selection for poi handle (Pattern 1)
tk.Label(root, text="Poi Handle Color (Left Hand):").grid(row=3, column=0)
poi_handle_color_display = tk.Label(root, bg=poi_handle_color1.get(), width=10)
poi_handle_color_display.grid(row=3, column=1)
poi_handle_color_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(poi_handle_color1, poi_handle_color_display))
poi_handle_color_button.grid(row=3, column=2)

# Color selection for poi head (Pattern 2)
tk.Label(root, text="Poi Head Color (Right Hand):").grid(row=4, column=0)
poi_head_color_display2 = tk.Label(root, bg=poi_head_color2.get(), width=10)
poi_head_color_display2.grid(row=4, column=1)
poi_head_color_button2 = tk.Button(root, text="Choose Color", command=lambda: choose_color(poi_head_color2, poi_head_color_display2))
poi_head_color_button2.grid(row=4, column=2)

# Color selection for poi handle (Pattern 2)
tk.Label(root, text="Poi Handle Color (Right Hand):").grid(row=5, column=0)
poi_handle_color_display2 = tk.Label(root, bg=poi_handle_color2.get(), width=10)
poi_handle_color_display2.grid(row=5, column=1)
poi_handle_color_button2 = tk.Button(root, text="Choose Color", command=lambda: choose_color(poi_handle_color2, poi_handle_color_display2))
poi_handle_color_button2.grid(row=5, column=2)

# Start side and rotation direction selection (Pattern 1)
tk.Label(root, text="Start Side (Left Hand):").grid(row=6, column=0)
start_side1_var = tk.StringVar(value='left')
start_side1_menu = ttk.Combobox(root, textvariable=start_side1_var, values=['left', 'right'])
start_side1_menu.grid(row=6, column=1)
start_side1_menu.current(0)

tk.Label(root, text="Rotation Direction (Left Hand):").grid(row=7, column=0)
rotation_direction1_var = tk.StringVar(value='clockwise')
rotation_direction1_menu = ttk.Combobox(root, textvariable=rotation_direction1_var, values=['clockwise', 'anticlockwise'])
rotation_direction1_menu.grid(row=7, column=1)
rotation_direction1_menu.current(0)

# Start side and rotation direction selection (Pattern 2)
tk.Label(root, text="Start Side (Right Hand):").grid(row=8, column=0)
start_side2_var = tk.StringVar(value='right')
start_side2_menu = ttk.Combobox(root, textvariable=start_side2_var, values=['left', 'right'])
start_side2_menu.grid(row=8, column=1)
start_side2_menu.current(1)

tk.Label(root, text="Rotation Direction (Right Hand:").grid(row=9, column=0)
rotation_direction2_var = tk.StringVar(value='clockwise')
rotation_direction2_menu = ttk.Combobox(root, textvariable=rotation_direction2_var, values=['clockwise', 'anticlockwise'])
rotation_direction2_menu.grid(row=9, column=1)
rotation_direction2_menu.current(1)

# Create a button to combine the selected patterns
combine_button = tk.Button(root, text="Combine Patterns", command=combine_selected_patterns)
combine_button.grid(row=12, column=0, columnspan=1)

# Save GIF button
def save_gif():
    writer = PillowWriter(fps=60)
    title = f"{title1}_vs_{title2}.gif"
    filepath = os.path.join("GIFs", title)
    ani.save(filepath, writer=writer)

save_gif_button = tk.Button(root, text="Save as GIF (GENERATE PATTERN FIRST)", command=save_gif)
save_gif_button.grid(row=12, column=1, columnspan=1)

# Run the main event loop
root.mainloop()