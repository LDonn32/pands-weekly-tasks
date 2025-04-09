# Weekly Task 02
# Author: Laura Donnelly


# banks.py
# this programme should do the following:
# prompts the user and read in two money amounts (in cent)
# Add the two amounts 
# Print out the answer in a human readable format with the euro sign and decimal point and cent of the amount


# prompt user for first amount of money in cents
amount1 =float(input("Enter amount of money in cent:"))

#prompt user for second amount of money in cents
amount2 = float(input("Enter a second amount of money in cents:"))

# input function will asks the user in the terminal to input the money.
# I am asking them to do so in cents
# however I need to convert the money into cents in the code also
# I can do so using the float function
#[Reference] https://www.geeksforgeeks.org/taking-input-from-console-in-python/
#[Reference] https://www.geeksforgeeks.org/float-in-python/

# Add the two amounts and divide by 100 for decimal
Sum = (amount1 + amount2)/100

# This calculation is then stored as a variable in Sum
# when this is printed later it should show as decimal to properly count the cents if the input is large enough to convert into euros

# print with a F string to include the euro sign
print(f"The sum of these is €{Sum}")

#[Link] https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/