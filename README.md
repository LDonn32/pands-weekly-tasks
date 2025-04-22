# pands-weekly-tasks

Author: Laura Donnelly


This ReadMe file will give a description for the the assigned weekly tasks and additional information and insights for the 2025 Programming and Scripting Module. 


# Technologies
This section covers what tools were used 

-Anaconda

-Git

-GitHub

-VSCode


# Requirements.txt
This file contains all the packages and libraries that were imported for the tasks.



# Installation/ how to run

Clone the repository:

```
git clone https://github.com/LDonn32/pands-weekly-tasks.git
```

Install requirements:

```
pip install -r requirements.txt
```

Run the desired program:

```
python banks.py
```

```
python accounts.py
```


# Weekly Task 02
Write a program called bank.py 

The program should:

- Prompt the user and read in two money amounts (in cent)
- Add the two amounts
- Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

## Code explained

The input function will asks the user in the terminal to input the money.
I am asking them to do so in cents, so I need to convert the money into cents in the code. 
I can do so using the float function

```
prompt user for first amount of money in cents
amount1 =float(input("Enter amount of money in cent:"))

prompt user for second amount of money in cents
amount2 = float(input("Enter a second amount of money in cents:"))
```

This calculation is then stored as a variable in Sum.
When this is printed later it should show as decimal to properly count the cents if the input is large enough to convert into euros.

```
# Add the two amounts and div
Sum = (amount1 + amount2)/100
```

## Resources:
Documentation for inputting the euro sign using f -strings

[Reference] https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/

Resources used for taking inputs from the terminal

[Reference] https://www.geeksforgeeks.org/taking-input-from-console-in-python/

Resources used to return a floating-point number from a number 

[Reference] https://www.geeksforgeeks.org/float-in-python/



# Weekly Task 03

Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890
Extra:
Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)


## Code explained 

Here I am defining the function and naming it mask_account_number. This will then ask the user for input() and what they input will be stored as a string.
```
# Define the function.
def mask_account_number():
    # Prompt the user for their 10 digit account number.
    account_number = input("Please enter your 10-character account number: ")
```
I am using len() function == 10 to make sure that the input is exactly 10 characters. I make the  I am using the [-4:] slice which will take from the 4th character from the end to the end.
```
    # Check if the input length is 10 characters.
    if len(account_number) == 10:
        # Replace first 6 characters with X to mask the digits and keep the last 4 digits
        masked_account_number = 'XXXXXX' + account_number[-4:]
```        
        # Print the masked account number.
        print("Masked account number:", masked_account_number)
        
    else:
        print("Invalid number! Please ensure to enter a 10-character account number.")
        
```

## EXTRA: Modified Code explained 


To get the length of the account number, I used the len() function which will return the number of characters in the string.
[Reference] https://www.w3schools.com/python/ref_func_len.asp

```
  account_length = len(account_number)
```

```
# Check if the account number has at least 4 characters.
if account_length >= 4:
    if account_length > 4:
        # Mask all but the last 4 digits
        masked_account_number = 'X' * (account_length - 4) + account_number[-4:]
```





## Resources:

[Reference] https://docs.python.org/3/library/string.html

[Reference] https://docs.python.org/3/tutorial/introduction.html#strings

[Reference] https://www.w3schools.com/python/python_strings.asp

[Reference] https://www.w3schools.com/python/ref_func_len.asp



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

[Reference] https://www.askpython.com/python/examples/collatz-conjecture

Python input() Function:

This function allows the programme to take input from the user, which is used to ask the user for a positive integer.

https://docs.python.org/3/library/functions.html#input

Used in this part of code:

   Prompt the user to input a positive integer
  number = int(input("Please enter a positive integer: "))

Python Lists
Lists are used to store multiple items in a single variable. Need this in the program to store the sequence of numbers
[Reference] https://www.w3schools.com/python/python_lists.asp

Python List append() Method
The append() method adds a single element to the end of a list. It modifies the original list in place and does not return a new list.
[Reference] https://www.w3schools.com/python/ref_list_append.asp

The while Loop
With the while loop the program can execute a set of statements as long as a condition is true.

[Reference] https://www.w3schools.com/python/python_while_loops.asp
[Reference] https://www.youtube.com/watch?time_continue=175&v=ECduJk00mUU&embeds_referring_euri=https%3A%2F%2Fwww.bing.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.bing.com&source_ve_path=Mjg2NjY

Used in this part of code:

  while number != 1:
        # Add the current number to the sequence
        sequence.append(number)

Python Conditional Statements:

This resource explains how if, else, and elif statements work in Python to handle different conditions like checking if a number is even or odd.
[Reference] https://www.w3schools.com/python/python_conditions.asp

Used in this part of code:

  if number % 2 == 0:
            number = number // 2  # If even, divide by 2
        else:
            number = 3 * number + 1  # If odd, multiply by 3 and add 1

Python String Methods and join():

The join() method is used to convert a list of numbers into a string with spaces between them.

[Reference] https://docs.python.org/3/library/stdtypes.html#str.join
[Reference] https://www.w3schools.com/python/ref_string_join.asp

Looked at examples others did
[Reference] https://codereview.stackexchange.com/questions/285429/automate-the-boring-stuff-with-python-the-collatz-sequence


Error on code -  IndentationError: expected an indented block after function definition

Below resources helped to fix, I wasn't spacing/tabing code correctly first time.
[Reference] https://www.youtube.com/watch?v=w5styN3Vaqw
[Reference] https://stackoverflow.com/questions/4446366/why-am-i-getting-indentationerror-expected-an-indented-block


# Weekly Task 05
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

You will need to search the web to find how you work out what day it is.

An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.


An example of running it on a Saturday is as follows:

$ python weekday.py
It is the weekend, yay!

There is no user input.


## Extra 
Modifed the program to include a third option for Friday. 
An example of running it on a Friday is as follows:

$ python weekday.py
Tgif!!! It's Friday woohoo!!

## Code explained 

## Rescourses: 

Documentation on how to import datetime and use weekday() method

[Reference] https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

Documentation on elif, if and else methods used in the code 

[Reference] https://www.w3schools.com/python/python_conditions.asp

# Weekly task 6
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 

This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.

## Code explained 


# Weekly Task 7 
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.

The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.

Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.



$ python es.py moby-dick.txt
116960

## Code explained 

# Weekly Task 8 
Write a program called plottask.py that displays:

a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range 0 to 10, 
on the one set of axes.
Some marks will be given for making the plot look nice (legend etc).

Please put a copy of the image of the plot (.png file) into the repository

## Code explained 


# Contact

Student ID: G00472977

Contact Email: G00472977@atu.ie


# Additional Rescources 

Useful template for creating this ReadMe file.

[Reference] https://github.com/othneildrew/Best-README-Template/blob/main/README.md

Useful to help format and use correct syntax for the ReadMe File, particularly for quoting code.

[Reference]  https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Python CheatSheet (2025)

[Reference] https://www.geeksforgeeks.org/python-cheat-sheet/



