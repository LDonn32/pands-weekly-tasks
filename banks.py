# banks.py

# This programme should do the following:
# prompts the user and read in two money amounts (in cent)
# Add the two amounts 
# Print out the answer in a human readable format with the euro sign and decimal point and cent of the amount


# Author: Laura Donnelly



# prompt user for first amount of money in cents
amount1 =float(input("Enter amount of money in cent:"))

#prompt user for second amount of money in cents
amount2 = float(input("Enter a second amount of money in cents:"))

# Add the two amounts and divide by 100 for decimal
Sum = (amount1 + amount2)/100

# print with a F string to include the euro sign
print(f"The sum of these is €{Sum}")

