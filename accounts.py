# accounts.py
# Weekly task 03

# Author: Laura Donnelly


# Orginal code before the EXTRA modification.

'''   
# Define the function.
def mask_account_number():
    # Prompt the user for their 10 digit account number.
    account_number = input("Please enter your 10-character account number: ")
    

    # Check if the input length is 10 characters.
    # See: https://www.w3schools.com/python/ref_func_len.asp
    
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
    # See: https://www.w3schools.com/python/ref_func_len.asp

    account_length = len(account_number)

    # Using if, else statements, check if the account number has at least 4 characters.
    # See: https://www.programiz.com/python-programming/if-elif-else

    if account_length >= 4:
        if account_length > 4:
            # Mask all but the last 4 digits.
            masked_account_number = 'X' * (account_length - 4) + account_number[-4:]
        else:
            # If the account number has exactly 4 digits, show the whole number.
            masked_account_number = account_number

        # Output the masked account number.
        print("Masked account number:", masked_account_number)
    else:
        # If the account number has fewer than 4 digits, show the whole account number.
        print("Account number is too short, showing the whole number:", account_number)

# Run the code.
mask_account_number()















