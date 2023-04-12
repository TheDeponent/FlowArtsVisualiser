import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from ThreePetalAnti import generate_ThreePetalAnti
from FivePetalAnti import generate_FivePetalAnti
from TenPetalAnti import generate_TenPetalAnti
from Extension import generate_Extension
from TwelvePetalAnti import generate_TwelvePetalAnti
from EightPetalInspin import generate_EightPetalIn
from FourPetalAnti import generate_FourPetalAnti
from TwoPetalInspin import generate_TwoPetalInspin
from FourPetalInspin import generate_FourPetalInspin
from CatEye import generate_Cateye

# List of available patterns
patterns = {
    "Extension": generate_Extension,
    "CatEye": generate_Cateye,
    "12 Petal Antispin (Gunslinger)": generate_TwelvePetalAnti,
    "10 Petal Antispin (Gunslinger)": generate_TenPetalAnti,
    "8 Petal Inspin (Gunslinger)": generate_EightPetalIn,
    "5 Petal Antispin": generate_FivePetalAnti,
    "4 Petal Antispin": generate_FourPetalAnti,
    "4 Petal Inspin": generate_FourPetalInspin,
    "3 Petal Antispin": generate_ThreePetalAnti,
    "2 Petal Inspin": generate_TwoPetalInspin,
}
def choose_color(color_variable, color_display):
    color = colorchooser.askcolor(color_variable.get())[1]
    if color:
        color_variable.set(color)
        color_display.config(bg=color)

def combine_selected_patterns():
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

    # Generate the plots for the two patterns
    fig, ax = plt.subplots()
    ax1, update1, elements1, title1, xlabel1 = pattern1(fig, ax, head_color1, handle_color1)
    ax2, update2, elements2, title2, xlabel2 = pattern2(fig, ax, head_color2, handle_color2)

    # Define a combined update function for the animation
    def combined_update(frame):
        return update1(frame) + update2(frame)

    # Create the animation
    num_frames = 360
    ani = FuncAnimation(fig, combined_update, frames=num_frames, interval=20, blit=True)

    # Set the title of the combined graph
    fig.suptitle(f"{title1} vs {title2}")

    # Set the combined x-axis label
    ax.set_xlabel(f"{xlabel1} vs {xlabel2}")

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
pattern2_menu.current(1)

# Color selection for poi head (Pattern 1)
tk.Label(root, text="Poi Head Color (Pattern 1):").grid(row=2, column=0)
poi_head_color_display = tk.Label(root, bg=poi_head_color1.get(), width=10)
poi_head_color_display.grid(row=2, column=1)
poi_head_color_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(poi_head_color1, poi_head_color_display))
poi_head_color_button.grid(row=2, column=2)

# Color selection for poi handle (Pattern 1)
tk.Label(root, text="Poi Handle Color (Pattern 1):").grid(row=3, column=0)
poi_handle_color_display = tk.Label(root, bg=poi_handle_color1.get(), width=10)
poi_handle_color_display.grid(row=3, column=1)
poi_handle_color_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(poi_handle_color1, poi_handle_color_display))
poi_handle_color_button.grid(row=3, column=2)

# Color selection for poi head (Pattern 2)
tk.Label(root, text="Poi Head Color (Pattern 2):").grid(row=4, column=0)
poi_head_color_display2 = tk.Label(root, bg=poi_head_color2.get(), width=10)
poi_head_color_display2.grid(row=4, column=1)
poi_head_color_button2 = tk.Button(root, text="Choose Color", command=lambda: choose_color(poi_head_color2, poi_head_color_display2))
poi_head_color_button2.grid(row=4, column=2)

# Color selection for poi handle (Pattern 2)
tk.Label(root, text="Poi Handle Color (Pattern 2):").grid(row=5, column=0)
poi_handle_color_display2 = tk.Label(root, bg=poi_handle_color2.get(), width=10)
poi_handle_color_display2.grid(row=5, column=1)
poi_handle_color_button2 = tk.Button(root, text="Choose Color", command=lambda: choose_color(poi_handle_color2, poi_handle_color_display2))
poi_handle_color_button2.grid(row=5, column=2)

# Create a button to combine the selected patterns
combine_button = tk.Button(root, text="Combine Patterns", command=combine_selected_patterns)
combine_button.grid(row=7, column=0, columnspan=5)

# Run the main event loop
root.mainloop()
