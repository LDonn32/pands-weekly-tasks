# Weekly task 8 
# Write a program called plottask.py that displays:
# a histogram of a normal distrubtion of a 1000 value with a mean of 5 and standard deviation of 2,
# and a plot of the function h(x)=x3 in the range 0-10
# on the set of axes

# include legends if possible

# copy the .png file into the repository


import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
data = np.random.normal(loc=5, scale=2, size=1000)

# Create an array of x values for the function h(x) = x^3
x_values = np.linspace(0, 10, 400)

# Compute the y values for h(x) = x^3
y_values = x_values ** 3

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))  # Set the size of the figure

# Plot the histogram of the normal distribution
ax.hist(data, bins=30, density=True, alpha=0.6, color='skyblue', label='Normal Distribution')

# Plot the function h(x) = x^3
ax.plot(x_values, y_values, color='darkred', lw=2, label=r'$h(x) = x^3$', linestyle='-', linewidth=2)

# Add a grid for better visibility
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Set the title and labels with enhanced styling
ax.set_title('Histogram of Normal Distribution and $h(x) = x^3$', fontsize=16, fontweight='bold')
ax.set_xlabel('X', fontsize=14)
ax.set_ylabel('Density / Value', fontsize=14)

# Customize the legend
ax.legend(loc='upper left', fontsize=12, frameon=False)

# Save the plot as a .png file in a repository or directory
plt.savefig('plot_image.png', format='png', dpi=300)  # Save with high resolution (300 DPI)

# Show the plot
plt.show()


# updated code - getting TYPE ERROR 


























