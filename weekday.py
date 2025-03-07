# This program outputs whether or 
# not today is a weekday

# Weekly task 5

# Author: Laura Donnelly

# Rescourses:
# https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
# https://www.w3schools.com/python/python_conditions.asp

# modified the program to include
# third output for friday
# used elif, if and else methods

# Using the .weekday() method of a datetime.date object
import datetime

# Get the current date ( 0 = Monday - 6 = Sunday)
weekno = datetime.date.today().weekday()
e 

if weekno == 4: # 4 is friday
    print("Tgif!!! It's Friday woohoo!!")
elif weekno < 5:  # less than 0 - 5 inlcuded (except 4 as defined in if)
    print("Yes, unfortunately today is a weekday")
else: # 5 Sat, 6 Sun
    print("It is the weekend, yay!")
