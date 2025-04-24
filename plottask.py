# plottask.py 
# Weekly Task 08 

# Author: Laura Donnelly


# Import packages.
import numpy as np
import matplotlib.pyplot as plt

# Create a normal distribution.
mean = 5
std_dev = 2
num_samples = 1000

# Generate the random data.
data = np.random.normal(mean, std_dev, num_samples)

# Plot the histogram.
# 1 row, 2 columns, first subplot.
plt.subplot(1, 2, 1)  

plt.hist(data, bins=30, color='pink', edgecolor='purple', label='Normal Distribution')
plt.title('Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Add a legend to the histogram.

plt.legend(loc='upper left')

# Plot the function h(x) = x^3 using np.arange().
# Create x values from 0 to 10 with a step of 0.1.
x_values = np.arange(0, 10, 0.1)  

# Calculate y = x^3.
y_value = x_values**3  

# Create the function plot.
# 1 row, 2 columns, second subplot.
plt.subplot(1, 2, 2)  

plt.plot(x_values, y_value, color='purple', label='h(x) = x^3')
plt.title('Plot of h(x) = x^3')
plt.xlabel('x')
plt.ylabel('h(x)')

# Add a legend to the function plot.
plt.legend(loc='upper left' )

# Save the histogram and plot.
plt.savefig('plottask.png')

# Adjust layout to avoid any overlap of the histogram or plot.
plt.tight_layout()

# Display the plots.
plt.show()
















