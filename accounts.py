# accounts.py
# Weekly task 03

# Author: Laura Donnelly


# Orginal code before the EXTRA modification.

'''   
# Define the function.
def mask_account_number():
    # Prompt the user for their 10 character account number.
    account_number = input("Please enter your 10-character account number: ")
    

    # Check if the input length is actually 10 characters.
    if len(account_number) == 10:
        # Replace the first 6 characters with X to mask the numbers and keep the last 4 numbers.
        masked_account_number = 'XXXXXX' + account_number[-4:]
        
        # Print the masked account number.
        print("Masked account number:", masked_account_number)

    # Print an error message asking the user to try again.   
    else:
        print("Invalid number! Please ensure to enter a 10-character account number.")

# Run the program.
mask_account_number()
'''

# Extra: Modified programm to read in account numbers of any lenght.


# Define the function.
def mask_account_number():
    # Prompt the user for their account number.
    # No request for character lenght in the prompt.

    account_number = input("Please enter your account number: ")

    # Check the length of the account number and store as a variable to call on in the program.

    account_length = len(account_number)

    # Using if, else statements, check if the account number has at least 4 characters.

    if account_length >= 4:
        if account_length > 4:
            # If account number is greater than 4 it will mask all but the last 4 numbers.
            masked_account_number = 'X' * (account_length - 4) + account_number[-4:]
        else:
            # If the account number has exactly 4 numbers, show the whole number.
            masked_account_number = account_number

        # Print the masked account number.
        print("Masked account number:", masked_account_number)
    else:
        # If the account number has fewer than 4 digits, show the whole account number.
        print("Account number is too short, showing the whole number:", account_number)

# Run the code.
mask_account_number()















