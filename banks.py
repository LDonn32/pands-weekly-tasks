# banks.py
# Weekly Task 02

# Author: Laura Donnelly


# Prompt the user for first amount of money in cents.
# See: https://www.geeksforgeeks.org/taking-input-from-console-in-python/

# Convert the inputted string to a float number.
# See: https://www.geeksforgeeks.org/float-in-python/

amount1 =float(input("Enter amount of money in cent:"))

# Prompt user for second amount of money in cents.

amount2 = float(input("Enter a second amount of money in cents:"))

# Add the two amounts and divide by 100 for decimal.
# This is to convert the cents into euros if the input goes over 99 cents.

Sum = (amount1 + amount2)/100

# Print with a F string to include the euro sign.
# See: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/

print(f"The sum of these is €{Sum}")

