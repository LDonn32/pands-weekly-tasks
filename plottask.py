# Weekly task 8 
# Write a program called plottask.py that displays:
# a histogram of a normal distrubtion of a 1000 value with a mean of 5 and standard deviation of 2,
# and a plot of the function h(x)=x3 in the range 0-10
# on the set of axes

# include legends if possible

# copy the .png file into the repository



# import packages needed

import numpy as np
# numpy is used for numerical operations and arrays. I have sho
# [link] https://numpy.org/doc/2.2/user/absolute_beginners.html

import matplotlib.pyplot as plt
# matplotlib.plyplot is used for plotting data. I have shortened it t
# [link] https://matplotlib.org/stable/users/explain/quick_start.html

# create 1000 random values from a normal distribution with mean set at 5 and standard deviation set at 2

data = np.random.normal(loc=5, scale=2, size = 1000)
# This will create an array of 1000 random values to be sampled.
# # loc is the mean which is set at 5
# # scale is for the standard deviation set at 2
# # size is the shape of the array (it is the number of values to create set at 1000)
#[link] https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
#[link] https://www.w3schools.com/python/numpy/numpy_random_normal.asp

# create an array of x values for the function h(x) = x^3

x_values = np.linspace(0, 10, 400)
# linspace will create, between 0 and 10, 400 evenly spaced values
#[link] https://pytutorial.com/understanding-python-numpylinspace/

y_value = x_values ** 3
# This runs the math function of h(x) = x^3
# setting y_values as a variable for x_values means that it will run the function for each x value in the array (I think???) - triple check this after running complete code
# going off week 6 function lecture - research some resources and link here



# create the plot

fig, ax = plt.subplots()
# subplots will populate a fig and set of axs 
# looking at returns section of documentation
#[Link] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

#plot the histogram of the normal distrubition

ax.hist(data, bins=30, density=True, alpha=0.6, colour='b', label='Normal Distribution')
# this function populates our histogram on the ax
# inputing data to plot our values from the normal distribution
# bins is used to divide the data ive set to 30 for now but can change this once we see the histogram, may need to scale up or down
# density is a bool that sets the area under the histogram is equal to 1
# alpha looks after the transparency of the bars. I have set it to 0.6 as 0 is fully transparent and 1 is saturdated. Can update simialr to bins
# colour looks after the colour of the bars. Set to blue but can play around 
# label sets the label for the histogram
# [Link] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html


# plot the function h(x) = x^3

ax.plot(x_values, y_values, color='r', label=r'$h(x) = x^3&')
# plotting the function. I used x values and y values to mark x and y on the histogram
# colour set to r for a red line, can update
# adding a lable for the function used 
# $$ and x^3 is used in the latex style code shown in Ians lecture - might not run just going of lecture walkthrough. Get documentation on this
#[Link] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# add the labels and the title
ax.set_title('Histogram of Normal Distribution and $h(x) = x^3$')
ax.set_xlabel('X')
ax.set_ylabel('Density / Value')
#[Link] https://datagy.io/matplotlib-title/ 


#show
plt.show()

# getting error ln 47 saying y values is not defined however i have coded y_values = x_values ** 3 
# need to trouble shoot this