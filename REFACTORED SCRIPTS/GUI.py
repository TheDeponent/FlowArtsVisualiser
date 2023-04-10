import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from ThreePetalAnti import generate_FivePetalAnti
from FivePetalAnti import generate_FivePetalAnti
from TenPetalAnti import generate_TenPetalAnti
from Extension import generate_Extension
from TwelvePetalAnti import generate_TwelvePetalAnti
from EightPetalIn import generate_EightPetalIn
from FourPetalAnti import generate_FourPetalAnti

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
    fig, ax = plt.subplots()
    combine_patterns(fig, ax, generate_EightPetalIn, generate_Extension)
