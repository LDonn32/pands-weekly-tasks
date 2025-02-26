# accounts.py
# This programme reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Author: Laura Donnelly

# resources: 
# https://docs.python.org/3/library/string.html
# https://docs.python.org/3/tutorial/introduction.html
# https://www.w3schools.com/python/python_strings.asp

def mask_account_number():
# read the account number
account_number = input("Please enter a 10 - character account number: ")

# change first 6 numbers with X and keep last 4 numbers
mask_account_number = "XXXXXX" + account_number[-4:]

# print
print("masked account number:", mask_account_number)

#  not working getting expected indented block error code. Will research this