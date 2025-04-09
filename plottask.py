# Weekly Task 8 
# Author: Laura Donnelly

# Write a program called plottask.py that displays:
# a histogram of a normal distrubtion of a 1000 value with a mean of 5 and standard deviation of 2,
# and a plot of the function h(x)=x3 in the range 0-10
# on the set of axes
# include legends if possible
# copy the .png file into the repository.


# Rescoures:
# [Link] https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# [Link] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# [Link] https://numpy.org/doc/stable/reference/generated/numpy.arange.html
# [Link] https://www.geeksforgeeks.org/numpy-arrange-in-python/
# [Link] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# [Link] https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
# [Link] https://www.geeksforgeeks.org/matplotlib-pyplot-tight_layout-in-python/

# Import packages.

import numpy as np
import matplotlib.pyplot as plt

# Create a normal distribution with the information given in the task: 
# 1000 values, mean=5, std=2.

mean = 5
std_dev = 2
num_samples = 1000

# Generate the random data.
# [Link] https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html

data = np.random.normal(mean, std_dev, num_samples)

# Plot the histogram.
# [Link] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

# 1 row, 2 columns, first subplot.
plt.subplot(1, 2, 1)  
plt.hist(data, bins=30, color='pink', edgecolor='purple', label='Normal Distribution')
plt.title('Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Add a legend to the histogram.
# [Link] https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/

plt.legend(loc='upper left')

# Plot the function h(x) = x^3 using np.arange().
# [Link] https://numpy.org/doc/stable/reference/generated/numpy.arange.html
# [Link] https://www.geeksforgeeks.org/numpy-arrange-in-python/

# Create x values from 0 to 10 with a step of 0.1.
x_values = np.arange(0, 10, 0.1)  

# Calculate y = x^3.
y_value = x_values**3  

# Create the function plot.
# [Link] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# 1 row, 2 columns, second subplot.
plt.subplot(1, 2, 2)  

plt.plot(x_values, y_value, color='purple', label='h(x) = x^3')
plt.title('Plot of h(x) = x^3')
plt.xlabel('x')
plt.ylabel('h(x)')

# Add a legend to the function plot.
plt.legend(loc='upper left' )


# Save the histogram and plot.
# Note: I had to change the flow of plt.show() and plt.savefig()
# If I ran show first, the saved file would come up blank
# They were interferring with each other
plt.savefig('plottask.png')


# Adjust layout to avoid any overlap of the histogram or plot.
# [Link] https://www.geeksforgeeks.org/matplotlib-pyplot-tight_layout-in-python/
plt.tight_layout()

# Display the plots.
plt.show()
















