# Weekly Task 3 
# Author: Laura Donnelly

# Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
# Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs). 
# $ python accounts.py
# Please enter an 10 digit account number: 1234567890
# XXXXXX7890

# Extra:
# Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

# Resources: 
# [Reference] https://docs.python.org/3/library/string.html

# [Reference] https://docs.python.org/3/tutorial/introduction.html#strings

# [Reference] https://www.w3schools.com/python/python_strings.asp

# [Reference] https://www.w3schools.com/python/python_conditions.asp

# [Reference] https://www.w3schools.com/python/ref_func_len.asp


# orginal code before the EXTRA modification.

'''   
# Define the function.
def mask_account_number():
    # Prompt the user for their 10 digit account number.
    account_number = input("Please enter your 10-character account number: ")
    

    # Check if the input length is 10 characters.
    if len(account_number) == 10:
        # Replace first 6 characters with X to mask the digits and keep the last 4 digits
        masked_account_number = 'XXXXXX' + account_number[-4:]
        
        # Print the masked account number.
        print("Masked account number:", masked_account_number)
        
    else:
        print("Invalid number! Please ensure to enter a 10-character account number.")

# run code
mask_account_number()
'''

# Extra: Modified programm to read in account numbers of any lenght.


# Define the function.
def mask_account_number():
    # Prompt the user for their account number.
    account_number = input("Please enter your account number: ")

    # Get the length of the account number.
    # the len() function will return the number of characters in the string.
    # [Reference] https://www.w3schools.com/python/ref_func_len.asp

    account_length = len(account_number)


    # Check if the account number has at least 4 characters.
    if account_length >= 4:
        if account_length > 4:
            # Mask all but the last 4 digits
            masked_account_number = 'X' * (account_length - 4) + account_number[-4:]
        else:
            # If the account number has exactly 4 digits, show the whole number
            masked_account_number = account_number

        # Output the masked account number
        print("Masked account number:", masked_account_number)
    else:
        # If the account number has fewer than 4 digits, show the whole account number
        print("Account number is too short, showing the whole number:", account_number)

# Run code.
mask_account_number()















