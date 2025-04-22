# weekday.py 

# Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
# You will need to search the web to find how you work out what day it is.

# An example of running this program on a Thursday is given below.
# $ python weekday.py Yes, unfortunately today is a weekday.

# An example of running it on a Saturday is as follows:
# $ python weekday.py It is the weekend, yay!

# There is no user input.

# EXTRA: I modified the program to include
# a third output for Friday.

# Author: Laura Donnelly


# Import datetime module. 
import datetime

# Using the .weekday() method of a datetime.date object, get the current date ( 0 = Monday - 6 = Sunday).
weekno = datetime.date.today().weekday()

# Using if, else and elif statements, set conditions to print for certain days of the week.
if weekno == 4: # 4 is friday
    print("Tgif!!! It's Friday woohoo!!")
elif weekno < 5:  # less than 0 - 5 inlcuded (except 4 as defined in if)
    print("Yes, unfortunately today is a weekday")
else: # 5 Sat, 6 Sun
    print("It is the weekend, yay!")
