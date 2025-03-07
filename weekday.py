# This program outputs whether or 
# not today is a weekday

# Weekly task 4

# Author: Laura Donnelly

# Rescourses:
# https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python


# Using the .weekday() method of a datetime.date object
import datetime

# Get the current date
weekno = datetime.date.today().weekday()

# Check if today is a weekday
if weekno < 5:
    print("Yes, unfortunately today is a weekday")
else: # 5 Sat, 6 Sun
    print("It is the weekend, yay!")
