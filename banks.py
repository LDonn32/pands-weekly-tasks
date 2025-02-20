# banks.py
# this programme should do the following:
# prompts the user and read in two money amounts (in cent)
# Add the two amounts 
# Print out the answer in a human readable format with the euro sign and decimal point and cent of the amount

# Author: Laura Donnelly
# Weekly Task 02

# first attempt


amount1 =float(input("Enter amount of money in cent:"))

# I tested first line of code and runs ok 

amount2 = float(input("Enter a second amount of money in cents"))

# now I need to add them together

Sum = (amount1 + amount2)/100

#so far this reads but answer not being shown on terminal

# now i need to print this out so its readable
print(Sum)

# next i need to find out how to include the euro sign