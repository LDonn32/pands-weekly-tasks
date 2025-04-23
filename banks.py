# banks.py
# Weekly Task 0264


# Author: Laura Donnelly



# prompt user for first amount of money in cents
amount1 =float(input("Enter amount of money in cent:"))

#prompt user for second amount of money in cents
amount2 = float(input("Enter a second amount of money in cents:"))

# Add the two amounts and divide by 100 for decimal
Sum = (amount1 + amount2)/100

# print with a F string to include the euro sign
print(f"The sum of these is €{Sum}")

