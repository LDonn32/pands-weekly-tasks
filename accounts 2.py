


# resources: 

# https://docs.python.org/3/library/string.html

# https://docs.python.org/3/tutorial/introduction.html#strings

# https://www.w3schools.com/python/python_strings.asp

def mask_account_number():
    # Read the account number
    account_number = input("Enter a 10-character account number: ")
    
    # Check if the input length is exactly 10 characters
    if len(account_number) == 10:
        # Replace the first 6 characters with 'X' and keep the last 4 digits
        masked_account_number = 'XXXXXX' + account_number[-4:]
        
        # Output the masked account number
        print("Masked account number:", masked_account_number)
    else:
        print("Invalid input! Please enter exactly a 10-character account number.")

# Call the function
mask_account_number()













