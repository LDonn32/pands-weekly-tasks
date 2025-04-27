# weekday.py 
# Weekly Task 05

# Author: Laura Donnelly


# Import datetime module. 
import datetime

# Using the .weekday() method of a datetime.date object, get the current date ( 0 = Monday - 6 = Sunday).
weeknumber = datetime.date.today().weekday()

# Using if, else and elif statements, set conditions to print for certain days of the week.

# If weekday is 4, (4 is friday) print the below message.
if weeknumber == 4: 
    print("Tgif!!! It's Friday woohoo!!")

# For the days less than 5,  0 - 3 (as 4 is defined in if), print the below message.
elif weeknumber < 5:  
    print("Yes, unfortunately today is a weekday")

# Else for the weekend,  5 Sat, 6 Sun, print the below message.
else: 
    print("It is the weekend, yay!")
