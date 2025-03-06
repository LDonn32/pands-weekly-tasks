# accounts.py
# This programme reads in a 10 character account number 
# outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Author: Laura Donnelly

# resources: 
# https://docs.python.org/3/library/string.html
# https://docs.python.org/3/tutorial/introduction.html
# https://www.w3schools.com/python/python_strings.asp


# accounts.py

def mask_account_number(account_number):
    # Check if the account number is valid (i.e., 10 characters long)
    if len(account_number) == 10:
        # Replace the first 6 digits with X's and leave the last 4 visible
        masked_account_number = 'XXXXXX' + account_number[-4:]
        return masked_account_number
    else:
        return "Invalid account number. It must be exactly 10 characters long."

<<<<<<< HEAD
#  not working getting expected indented block error code. Will research this
# https://www.makeuseof.com/python-indentation-error-expected-block-error-fix/

=======
# Main function to interact with the user
if __name__ == "__main__":
    # Read the account number from the user
    account_number = input("Enter your 10-character account number: ")
    
    # Mask and display the account number
    result = mask_account_number(account_number)
    print("Masked account number:", result)
>>>>>>> d56cb037a0fa55ec122882bc33e7d567a46e04e5
