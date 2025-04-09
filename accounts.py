# Weekly Task 3 
# Author: Laura Donnelly

# Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
# Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs). 
# $ python accounts.py
# Please enter an 10 digit account number: 1234567890
# XXXXXX7890

# Extra:
# Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

# resources: 
# [Link] https://docs.python.org/3/library/string.html

# [Link] https://docs.python.org/3/tutorial/introduction.html#strings

# [Link] https://www.w3schools.com/python/python_strings.asp

# [Link] https://www.w3schools.com/python/python_conditions.asp



# Define the function.
def mask_account_number():
    # Read in the account number
    account_number = input("Please enter your 10-character account number: ")
    
    # Check if the input length is 10 characters
    if len(account_number) == 10:
        # Replace first 6 characters with X and keep the last 4 digits
        masked_account_number = 'XXXXXX' + account_number[-4:]
        
        # Output the masked account number
        print("Masked account number:", masked_account_number)
    else:
        print("Invalid number! Please ensure to enter a 10-character account number.")

# run the code
mask_account_number()
