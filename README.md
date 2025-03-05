# pands-weekly-tasks



# Weekly Task 02
Write a program called bank.py 

The program should:

- Prompt the user and read in two money amounts (in cent)
- Add the two amounts
- Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

## Resources:
Documentation for inputting the euro sign

https://stackoverflow.com/questions/40612344/how-to-output-a-euro-sign-in-c
https://www.fileformat.info/info/unicode/char/search.htm?q=%E2%82%AC




# Weekly Task 03

Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890
Extra:
Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)


# Weekly Task 4
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).

Example of it running:

$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1


## Resources:

Information on the Collatz Problem

https://www.askpython.com/python/examples/collatz-conjecture

Python input() Function:

This function allows the programme to take input from the user, which is used to ask the user for a positive integer.

https://docs.python.org/3/library/functions.html#input

Used in this part of code:

   Prompt the user to input a positive integer
  number = int(input("Please enter a positive integer: "))

Python Lists
Lists are used to store multiple items in a single variable. Need this in the program to store the sequence of numbers
https://www.w3schools.com/python/python_lists.asp

Python List append() Method
The append() method adds a single element to the end of a list. It modifies the original list in place and does not return a new list.
https://www.w3schools.com/python/ref_list_append.asp

The while Loop
With the while loop the program can execute a set of statements as long as a condition is true.

https://www.w3schools.com/python/python_while_loops.asp
https://www.youtube.com/watch?time_continue=175&v=ECduJk00mUU&embeds_referring_euri=https%3A%2F%2Fwww.bing.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.bing.com&source_ve_path=Mjg2NjY

Used in this part of code:

  while number != 1:
        # Add the current number to the sequence
        sequence.append(number)

Python Conditional Statements:

This resource explains how if, else, and elif statements work in Python to handle different conditions like checking if a number is even or odd.
https://www.w3schools.com/python/python_conditions.asp

Used in this part of code:

  if number % 2 == 0:
            number = number // 2  # If even, divide by 2
        else:
            number = 3 * number + 1  # If odd, multiply by 3 and add 1

Python String Methods and join():

The join() method is used to convert a list of numbers into a string with spaces between them.

https://docs.python.org/3/library/stdtypes.html#str.join
https://www.w3schools.com/python/ref_string_join.asp

Looked at examples others did
https://codereview.stackexchange.com/questions/285429/automate-the-boring-stuff-with-python-the-collatz-sequence

Found resources on whats called a name gaurd to help code run smoothly

https://stackoverflow.com/questions/419163/what-does-if-name-main-do

Error on code -  IndentationError: expected an indented block after function definition

Below resources helped to fix, I wasn't spacing/tabing code correctly first time.
https://www.youtube.com/watch?v=w5styN3Vaqw
https://stackoverflow.com/questions/4446366/why-am-i-getting-indentationerror-expected-an-indented-block

