import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

# Sample data
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441,
            56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43, 80.653,
            44.741, 50.651, 78.553, 72.961, 72.889, 65.152, 46.462, 55.322, 78.782, 48.328, 75.748,
            78.273, 76.486, 78.332, 54.791, 72.235, 74.994, 71.338, 71.878, 51.579, 58.04, 52.947,
            79.313, 80.657, 56.735, 59.448, 79.406, 60.022, 79.483, 70.259, 56.007, 46.388, 60.916,
            70.198, 82.208, 73.338, 81.757, 64.698, 70.65, 70.964, 59.545, 78.885, 80.745, 80.546,
            72.567, 82.603, 72.535, 54.11, 67.297, 78.623, 77.588, 71.993, 42.592, 45.678, 73.952,
            59.443, 48.303, 74.241, 54.467, 64.164, 72.801, 76.195, 66.803, 74.543, 71.164, 42.082,
            62.069, 52.906, 63.785, 79.762, 80.204, 72.899, 56.867, 46.859, 80.196, 75.64, 65.483,
            75.537, 71.752, 71.421, 71.688, 75.563, 78.098, 78.746, 76.442, 72.476, 46.242, 65.528,
            72.777, 63.062, 74.002, 42.568, 79.972, 74.663, 77.926, 48.159, 49.339, 80.941, 72.396,
            58.556, 39.613, 80.884, 81.701, 74.143, 78.4, 52.517, 70.616, 58.42, 69.819, 73.923,
            71.777, 51.542, 79.425, 78.242, 76.384, 73.747, 74.249, 73.422, 62.698, 42.384, 43.487]

# Split the data into different segments (e.g., different bin sizes or ranges)
# In this case, I’ll divide it into 5 different bin sizes for illustration
bin_sizes = [5, 10, 15, 20, 25]

# Set up the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # Make room for buttons

# Initial plot
current_bin_size = 5
ax.hist(life_exp, bins=current_bin_size)
ax.set_title(f'Histogram with {current_bin_size} bins')
ax.set_xlabel('Life Expectancy')
ax.set_ylabel('Frequency')

# Button click handler to update the plot
def update_plot(event):
    global current_bin_size
    if event.inaxes == axprev:
        current_bin_size = bin_sizes[(bin_sizes.index(current_bin_size) - 1) % len(bin_sizes)]
    else:
        current_bin_size = bin_sizes[(bin_sizes.index(current_bin_size) + 1) % len(bin_sizes)]

    ax.clear()  # Clear the current plot
    ax.hist(life_exp, bins=current_bin_size)  # Plot with new bin size
    ax.set_title(f'Histogram with {current_bin_size} bins')
    ax.set_xlabel('Life Expectancy')
    ax.set_ylabel('Frequency')
    plt.draw()  # Redraw the figure

# Create "Previous" and "Next" buttons
axprev = plt.axes([0.1, 0.05, 0.1, 0.075])  # [left, bottom, width, height]
axnext = plt.axes([0.8, 0.05, 0.1, 0.075])

button_prev = Button(axprev, 'Previous')
button_next = Button(axnext, 'Next')

button_prev.on_clicked(update_plot)
button_next.on_clicked(update_plot)

# Show the plot
plt.show()
