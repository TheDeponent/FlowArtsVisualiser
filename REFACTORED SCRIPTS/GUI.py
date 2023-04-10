import tkinter as tk
from tkinter import ttk
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

def combine_patterns(fig, ax, pattern1, pattern2):
    # Add elements from both patterns to the same plot and store their update functions
    ax, update1, elements1 = pattern1(fig, ax)
    ax, update2, elements2 = pattern2(fig, ax)

    # Combined update function that handles both patterns
    def combined_update(frame):
        return update1(frame) + update2(frame)

    # Create a single animation for both patterns
    num_frames = 360
    ani = FuncAnimation(fig, combined_update, frames=num_frames, interval=20, blit=True)

    # Display the combined plot
    plt.show()

if __name__ == "__main__":
    #fig, ax = plt.subplots()
    #combine_patterns(fig, ax, generate_EightPetalIn, generate_Extension)
    pass

# List of available patterns
patterns = {
    "Extension": generate_Extension,
    "CatEye": generate_Cateye,
    "3 Petal Antispin": generate_ThreePetalAnti,
    "5 Petal Antispin": generate_FivePetalAnti,
    "10 Petal Antispin (Gunslinger)": generate_TenPetalAnti,
    "12 Petal Antispin (Gunslinger)": generate_TwelvePetalAnti,
    "8 Petal Inspin (Gunslinger)": generate_EightPetalIn,
    "4 Petal Antispin": generate_FourPetalAnti,
    "2 Petal Inspin": generate_TwoPetalInspin,
    "4 Petal Inspin": generate_FourPetalInspin,
}

def combine_selected_patterns():
    pattern1_name = selected_pattern1.get()
    pattern2_name = selected_pattern2.get()
    pattern1 = patterns[pattern1_name]
    pattern2 = patterns[pattern2_name]

    fig, ax = plt.subplots()
    combine_patterns(fig, ax, pattern1, pattern2)

# Create the main window
root = tk.Tk()
root.title("Pattern Combiner")

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

# Create a button to combine the selected patterns
combine_button = tk.Button(root, text="Combine Patterns", command=combine_selected_patterns)
combine_button.grid(row=2, column=0, columnspan=2)

# Run the main event loop
root.mainloop()
