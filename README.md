# pands-weekly-tasks

Author: Laura Donnelly


# Weekly Task 02
Write a program called bank.py 

The program should:

- Prompt the user and read in two money amounts (in cent)
- Add the two amounts
- Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 



## Resources:
Documentation for inputting the euro sign using f -strings

https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/




# Weekly Task 03

Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890
Extra:
Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

## Resources:

https://docs.python.org/3/library/string.html
https://docs.python.org/3/tutorial/introduction.html#strings
https://www.w3schools.com/python/python_strings.asp

Extra
Assumptions:


# Weekly Task 4
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).

Example of it running:

$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1


## Resources:

Information on the Collatz Problem

https://www.askpython.com/python/examples/collatz-conjecture

Python input() Function:

This function allows the programme to take input from the user, which is used to ask the user for a positive integer.

https://docs.python.org/3/library/functions.html#input

Used in this part of code:

   Prompt the user to input a positive integer
  number = int(input("Please enter a positive integer: "))

Python Lists
Lists are used to store multiple items in a single variable. Need this in the program to store the sequence of numbers
https://www.w3schools.com/python/python_lists.asp

Python List append() Method
The append() method adds a single element to the end of a list. It modifies the original list in place and does not return a new list.
https://www.w3schools.com/python/ref_list_append.asp

The while Loop
With the while loop the program can execute a set of statements as long as a condition is true.

https://www.w3schools.com/python/python_while_loops.asp
https://www.youtube.com/watch?time_continue=175&v=ECduJk00mUU&embeds_referring_euri=https%3A%2F%2Fwww.bing.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.bing.com&source_ve_path=Mjg2NjY

Used in this part of code:

  while number != 1:
        # Add the current number to the sequence
        sequence.append(number)

Python Conditional Statements:

This resource explains how if, else, and elif statements work in Python to handle different conditions like checking if a number is even or odd.
https://www.w3schools.com/python/python_conditions.asp

Used in this part of code:

  if number % 2 == 0:
            number = number // 2  # If even, divide by 2
        else:
            number = 3 * number + 1  # If odd, multiply by 3 and add 1

Python String Methods and join():

The join() method is used to convert a list of numbers into a string with spaces between them.

https://docs.python.org/3/library/stdtypes.html#str.join
https://www.w3schools.com/python/ref_string_join.asp

Looked at examples others did
https://codereview.stackexchange.com/questions/285429/automate-the-boring-stuff-with-python-the-collatz-sequence


Error on code -  IndentationError: expected an indented block after function definition

Below resources helped to fix, I wasn't spacing/tabing code correctly first time.
https://www.youtube.com/watch?v=w5styN3Vaqw
https://stackoverflow.com/questions/4446366/why-am-i-getting-indentationerror-expected-an-indented-block


## Weekly Task 05
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

You will need to search the web to find how you work out what day it is.

An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.


An example of running it on a Saturday is as follows:

$ python weekday.py
It is the weekend, yay!

There is no user input.

Modifed the program to include a third option for Friday. 
An example of running it on a Friday is as follows:

$ python weekday.py
Tgif!!! It's Friday woohoo!!


## Rescourses: 

Documentation on how to import datetime and use weekday() method

https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

Documentation on elif, if and else methods used in the code 

https://www.w3schools.com/python/python_conditions.asp

## Weekly task 6
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 

This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.




## Weekly Task 7 




## Weekly Task 8 





Sample code so far with refs and notes - need to update


import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
data = np.random.normal(loc=5, scale=2, size=1000)

# Create an array of x values for the function h(x) = x^3
x_values = np.linspace(0, 10, 400)

# Compute the y values for h(x) = x^3
y_values = x_values ** 3  # Correct variable name from 'y_value' to 'y_values'

# Create the plot
fig, ax = plt.subplots()

# Plot the histogram of the normal distribution
ax.hist(data, bins=30, density=True, alpha=0.6, color='b', label='Normal Distribution')

# Plot the function h(x) = x^3
ax.plot(x_values, y_values, color='r', label=r'$h(x) = x^3$')

# Set the title and labels
ax.set_title('Histogram of Normal Distribution and $h(x) = x^3$')
ax.set_xlabel('X')
ax.set_ylabel('Density / Value')

# Show the plot
plt.show()
