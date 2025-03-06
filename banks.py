# banks.py
# this programme should do the following:
# prompts the user and read in two money amounts (in cent)
# Add the two amounts 
# Print out the answer in a human readable format with the euro sign and decimal point and cent of the amount

# Author: Laura Donnelly
# Weekly Task 02



amount1 =float(input("Enter amount of money in cent:"))

# I tested first line of code and runs ok 

amount2 = float(input("Enter a second amount of money in cents:"))

# now I need to add them together

Sum = (amount1 + amount2)/100

# ok now it reads but i need to add the decimal point
# going to try an F string 
# https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/


print(f" The total sum is:"€{sum}")

# invalid charcater for €, i will need to import this. 
# Error message is including Unicode escape Sequence
# Will try this U+20AC


