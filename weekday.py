# weekday.py 
# Weekly Task 05

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
