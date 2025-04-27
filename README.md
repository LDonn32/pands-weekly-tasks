# pands-weekly-tasks

Author: Laura Donnelly


This ReadMe file for the 2025 Programming and Scripting Module for the H. Dip in Science in Data Analytics, ATU will do the following:

* Give a description for each of the assigned weekly tasks.
  
* Show how to run the programs.
  
* State what technologies and libraries were used.
  
* Present additional information, comments and insights for code used in each of the tasks.

* Includes references and additional resources used.


# Technologies

## This section covers what tools were used: 

[Anaconda](https://www.anaconda.com/download)

[Git](https://git-scm.com/downloads)

[GitHub](https://github.com/)

[VSCode](https://code.visualstudio.com/)


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

Run the desired program from the weekly tasks:

```
python banks.py
```

```
python accounts.py
```

```
python collatz.py
```

```
python weekday.py
```

```
python squareroot.py
```

```
python es.py <filename.txt>
```

NOTE: To run the es.py program with the mobydick.txt file in the repository use the below. More details on this in task 7.

```
python es.py mobydick.txt
```

```
plottask.py
```


# Weekly Task 02 - bank.py 
Write a program called bank.py 

The program should:

- Prompt the user and read in two money amounts (in cent)
- Add the two amounts
- Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

## Code explained

The input function will asks the user in the terminal to input the money. I used the resource [GeeksforGeeks.org](https://www.geeksforgeeks.org/taking-input-from-console-in-python/) for taking inputs from the terminal. 

I am asking them to do so in cents, so I need to convert the money into cents in the code. 
I can do so using the float function. I looked at [GeeksforGeeks.org](https://www.geeksforgeeks.org/float-in-python/) for information on returning a floating-point number from a number.

```
prompt user for first amount of money in cents
amount1 =float(input("Enter amount of money in cent:"))

prompt user for second amount of money in cents
amount2 = float(input("Enter a second amount of money in cents:"))
```

This calculation is then stored as a variable in Sum.
When this is printed later it should show as decimal to properly count the cents if the input is large enough to convert into euros. 
I used the resource [Geeksforgeeks.org](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/) for inputting the euro sign using f -strings.

```
# Add the two amounts and div
Sum = (amount1 + amount2)/100

# Print with a F string to include the euro sign.
print(f"The sum of these is €{Sum}")
```


# Weekly Task 03 - accounts.py

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
    # Prompt the user for their 10 character account number.
    account_number = input("Please enter your 10-character account number: ") 
```
I am using len() function == 10 to make sure that the input is exactly 10 characters. I used this resource [len() Function](https://www.w3schools.com/python/ref_func_len.asp) on w3schools. I am using the [-4:] slice which will take from the 4th character from the end to the end. I refer to information on [Datacamp.com](https://www.datacamp.com/tutorial/python-slice) on how to do this. 
```
# Check if the input length is actually 10 characters.
if len(account_number) == 10:
    # Replace the first 6 characters with X to mask the numbers and keep the last 4 numbers.
    masked_account_number = 'XXXXXX' + account_number[-4:]
```        
        # Print the masked account number.
        print("Masked account number:", masked_account_number)
        
    # Print an error message asking the user to try again.        
    else:
        print("Invalid number! Please ensure to enter a 10-character account number.")
        


## EXTRA: Modified Code explained 


To get the length of the account number, I used the len() function which will return the number of characters in the string [len() Function](https://www.w3schools.com/python/ref_func_len.asp).

```
# Prompt the user for their account number.
# No request for character lenght in the prompt.

  account_length = len(account_number)
  
```

To modify the program to handle different character lenghts, I used the if, else statements, I found this resource really helpful to understand how to use them [Programiz.com](https://www.programiz.com/python-programming/if-elif-else).

When handling account numbers with more than 4 characters, I set the program to only show the last 4 characters. For example, if an account number with 6 characters is entered, the first 2 will be masked and the last 4 will be visable.

```
# Using if, else statements, check if the account number has at least 4 characters.
if account_length >= 4:
    if account_length > 4:
        # If account number is greater than 4 it will mask all but the last 4 numbers.
        masked_account_number = 'X' * (account_length - 4) + account_number[-4:]
```

When handling account numbers with exactly 4 characters, I decided to show the whole number rather than mask the only 4 characters. My thinking behind this is so that the account number is readable in the output terminal. I contemplated masking 2 characters instead of 4 for these cases, but my assumption would be for most bank accounts is that you need the last 4 characters to identify a users bank account.

```
else:
    # If the account number has exactly 4 digits, show the whole number.
    masked_account_number = account_number
```

I took the same logic from above and applied it to if there are account numbers with less than 4 characters. I also added in a message for the user for feedback, incase they missed a number. 

```
else:
    # If the account number has fewer than 4 digits, show the whole account number.
    print("Account number is too short, showing the whole number:", account_number)
```


# Weekly Task 4 - collatz.py
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).

Example of it running:

$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1


## Code explained

I define my function and prompt user input 
[input()function](https://docs.python.org/3/library/functions.html#input), I convert the number inputted to an interger [W3 Schools int()](https://www.w3schools.com/python/ref_func_int.asp)

```
# Define the function.
# This function allows the programm to take input from the user, which is used to ask the user for a positive integer.

def collatz():
    # Prompt the user to input a positive integer.
    number = int(input("Please enter a positive integer: "))
```


I need to ensure that the number the user inputs is also a positive integer. I did this by applying an if statement see [Programiz.com](https://www.programiz.com/python-programming/if-elif-else) for information on if,else statements.


```
# Ensure the number is positive.
if number <= 0:
    print("Please enter a positive integer.")
    return
```

[W3schools Python Lists](https://www.w3schools.com/python/python_lists.asp) are used to store multiple items in a single variable. I used a list in the program to store the sequence of numbers.

```
# Create a list to store the sequence.
sequence = []
```

Next I added a while loop. With the while loop, the program can execute a set of statements as long as a condition is true. 
[W3schools While Loop](https://www.w3schools.com/python/python_while_loops.asp) is a great resource for understanding how to use a while loop. I also found this video helpful [Youtube.com](https://www.youtube.com/watch?time_continue=175&v=ECduJk00mUU&embeds_referring_euri=https%3A%2F%2Fwww.bing.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.bing.com&source_ve_path=Mjg2NjY). For information on conditional statements, i refer to [W3schools Python Conditions](https://www.w3schools.com/python/python_conditions.asp).

```
# Continue the process until the number becomes 1.
while number != 1:

```

I used the append() method [W3schools append()](https://www.w3schools.com/python/ref_list_append.asp) which adds a single element to the end of a list. It modifies the original list in place and does not return a new list.

```
# Add the current number to the sequence using the append() function.
sequence.append(number)
```

I applied the Collatz rule to the program using if and else statements. These statements will check if the number is even or odd and then apply the corresponding rule (If even, divide by 2) or (If odd, multiply by 3 and add 1).

```
# Apply the Collatz rule using if and else statements.

# If even, divide by 2
if number % 2 == 0:
    number = number // 2  
# Else if it is odd, multiply by 3 and add 1
else:
    number = 3 * number + 1  
```


While number !=1: stops when the number becomes 1, it actually doesn't add it in the sequence, it's the end of the Collatz chain. I need to include 1 manually and I do this by using the Append() Method.

```
    # Add 1 to the sequence as the loop ends when number becomes 1 using the append() function.
    sequence.append(1)
```

I used the join() method [Python.org join()](https://docs.python.org/3/library/stdtypes.html#str.join), [W3schools.com join()](https://www.w3schools.com/python/ref_string_join.asp) to convert a list of numbers into a string with spaces between them.

```
    # Output the sequence as a space-separated string.
    print(" ".join(map(str, sequence)))
```


## Additional Resources:

**Information on the Collatz Problem.**

[AskPython.com](https://www.askpython.com/python/examples/collatz-conjecture)

**Looked at examples others did.**

[Code Review.com](https://codereview.stackexchange.com/questions/285429/automate-the-boring-stuff-with-python-the-collatz-sequence)

**Errors on code** - *IndentationError: expected an indented block after function definition.*

Below resources helped to fix, I wasn't spacing/tabing code correctly first time.

[Youtube.com](https://www.youtube.com/watch?v=w5styN3Vaqw)

[Stackoverflow.com](https://stackoverflow.com/questions/4446366/why-am-i-getting-indentationerror-expected-an-indented-block)


# Weekly Task 05 - weekday.py
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

You will need to search the web to find how you work out what day it is.

An example of running this program on a Thursday is given below.

```
$ python weekday.py
Yes, unfortunately today is a weekday.
```
An example of running it on a Saturday is as follows:

```
$ python weekday.py
It is the weekend, yay!
```
There is no user input.

## Extra 
Modifed the program to include a third option for Friday. 
An example of running it on a Friday is as follows:

```
$ python weekday.py
Tgif!!! It's Friday woohoo!!
```

## Code explained 

To start, I need to import the module datetime, I checked [Stackoverflow.com](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python) and [Geeksforgeeks.org](https://www.geeksforgeeks.org/python-datetime-weekday-method-with-example/) for information on this module.  This module handles dates and times and will allow me to get the current day of the week. I will use the Weekday() Method to get the days of the week. 
The days of the week are represented as such; 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday.

```
# Import datetime module.
import datetime

# Using the .weekday() method of a datetime.date object, get the current date ( 0 = Monday - 6 = Sunday).
weeknumber = datetime.date.today().weekday()
```
I use if, else and elif statements to output what day of the week it is, see [W3schools.com](https://www.w3schools.com/python/python_conditions.asp) for information on if statememts. I ensure to match the numbers to their respective days as per the Weekday() Method.

```
# If weekday is 4, (4 is friday) print the below message.
if weeknumber == 4: 
    print("Tgif!!! It's Friday woohoo!!")

# For the days less than 5,  0 - 3 (as 4 is defined in if), print the below message.
elif weeknumber < 5:  
    print("Yes, unfortunately today is a weekday")

# Else for the weekend,  5 Sat, 6 Sun, print the below message.
else: 
    print("It is the weekend, yay!")
```



# Weekly task 6 - squareroot.py
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 

This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.



## Code explained 

I define the function as sqrt as requested in the task. The function will take in two inputs, N and 1.  N represents the number of the square root I am trying to find. 1 represents the tolerance. The tolorence is how accurate I want the program to be. I will set it as up to 5 decimal points later in the code for accuracy. I looked at [Geeksforgeeks.org](https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/) as a starting point for this code.

```
# Define function to return the square root of a number using Newton's method.
def sqrt(n, l):

```

Using Newton's method, I am guessing that the square root is n itself. I am using this as a starting point as I set the program to guess until it finds the closest number. I also am using count to keep track of how many times I loop the program before I start a while loop. Information on count() method found at [Geeksforgeeks.org](https://www.geeksforgeeks.org/python-list-count-method/).

```
  # This will be the first guess where the code guesses the square root of n as n.
  x = n

  # Use a counter to track how many guesses the program makes.
  count = 0
```

I start an infinate while loop that will count, see information on while loops at [Geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-use-while-true-in-python/). Then I add Newton's Method.

```
    # Using while true, keep improving the guess until it gets close.
while True:
   # Do this by calculating using Newton's Method (x+ (n/x)). This should get x closer to the square root and give the program a more accurate guess.
   root = 0.5 * (x + (n / x))
```

I compare how much the new guess root differs from the old guess x. If the changeis close enough, it breaks the loop. The Python abs() function will return the absolute value, see [Geeksforgeeks.org](https://www.geeksforgeeks.org/abs-in-python/)  for information on abs() function. It makes sure the number remains a positive integer. 

```
# Root is the new guess.
# X is the old guess.
# (root - x) will check the difference between the new and old guess.
# Using the abs() function to return the absolute value of it.
# If the number is close enough to the old one, the loop while break.
if abs(root - x) < l:
    break
```

I update the root to the newest guess. I use return function to return the closest value of root.

```
        #  Update the guess to the new number.
        x = root

    return root
```

Next I need to get user input. I do this by asking the user to input a positive interger. I then convert it to a floating point number from a string inputted by the user using the float() function. See information on [Geeksforgeeks float()](https://www.geeksforgeeks.org/float-in-python/)

```
# Prompt user to input a positive number. Use float() function to convert it to floating-point number.
n = float(input("Enter a positive number: "))
```

I use an if statements to make sure the user input is in fact a positive number. If the user enters 0 or a negative number it will show the error message "Please enter a positive number". I refer back to [W3schools Python Conditions](https://www.w3schools.com/python/python_conditions.asp) for information on if, else statements and python conditions.

```
# # Ensure that the number inputted is actually a positive number. Print message to user to try again if not.
if n <= 0:
    print("Please enter a positive number.")
```

I use else statements to run the function if the number is valid. I set the tolorenece level as 0.00001 to get as close as possible to the root number. Then I call the sqrt function and print out results. 

```
# Set the tolerance to how close it gets to the square number, set at 5 decimals for accuracy.
else:
    l = 0.00001 
    print(f"Approximate square root of {n} is {sqrt(n, l)}")

 Print the results.
   print(f"Approximate square root of {n} is {sqrt(n, l)}")
```

## Additional Rescourses: 

**How to get square root in python** 

[stackoverflow.com](https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python)



# Weekly Task 7 - es.py
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.

The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.

Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.


$ python es.py moby-dick.txt
116960


## Code explained 

I make some assumptions before starting this program: I am only looking at lower case 'e' for this code. The file to read in will be a txt file. If user input doesnt give me a file name or an incorrect file type, I need the program to print out an error message.


I import packages OS and SYS. Sys gives better control over input or output. Users can engage with the terminal/ comand line more freely. I found information on SYS at[Geeksforgeeks.org](https://www.geeksforgeeks.org/python-sys-module/). OS allows me to check file paths, if they exist or not. I found information on OS at [Geeksforgeeks.org](https://www.geeksforgeeks.org/os-module-python-examples/).
```

# Import packages.

# Import sys to handle command-line arguments and exit the program.
import sys

#Import os to check if a given path is a valid file.
import os

```
I define the function as count_e and this will take in the file name.

```
# Define the function that will count the number of lowercase 'e's in a file.
def count_e(filename):
```

I start error handling for the program. I will use try, except statements. I found the resources on [W3schools.com Try Except](https://www.w3schools.com/python/python_try_except.asp) and 
[Realpython.com Python Exceptions](https://realpython.com/python-exceptions/) helpful here.

First, I use try which will follow the code set out in the with the open() function. This will open the file, 'r' opens it for reading (default). I include 'with' before open as it will ensure to automatically close the file after. I refer to [www.pythontutorial.net](https://www.pythontutorial.net/python-basics/python-read-text-file/) for information on how to read a textfile. I was getting the error 'ValueError: I/O operation on closed file' with first draft of the code, I believe I wasn't closing the file in the right way and after I used the 'With' function it didn't occur. 

I add in encoding='utf-8' to read the text file. When I tried to run the code without including it, I got the error 'the file mobydick.txt could not be read as a text file', so I read back on the resource on [www.pythontutorial.net](https://www.pythontutorial.net/python-basics/python-read-text-file/) about utf-8, I realised the moby dick text file I am using has some other language characters in it so I needed to include UTF-8 it in to read the characters in the file correctly.

I use file.read() [Geeksforgeeks.org using read()](https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/) to read in the text file as a string and then return it to count the number of lowercase 'e's using str.count() (changed to text.count to match the variable name). Information on count() was found at [W3schools.com](https://www.w3schools.com/python/ref_string_count.asp).

```
  # Error handling using try and except statements to catch any possible errors.
try:
    # Open the file in read mode with UTF-8 encoding. 
    # Using with to close the file automaticall when done.
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the file using read().
        text = file.read()
        # Count the number of lowercase 'e's.
        return text.count('e')
```

Moving onto except cases for the error handling. I use except to catch files that don't exist. If the file inputed by the user doesnt exist, the message file not found will be printed on the terminal. I use sys.exit(1) which means there was an error and that is why the program is exiting. I found information on sys.exit on [Stackoverflow.com](https://stackoverflow.com/questions/9426045/difference-between-exit0-and-exit1-in-python), which was helpful to understand the different error code 0 and 1.
```
# Error handling with except statement to catch when the file doesn't exist.    
except FileNotFoundError:
    # Print error message for user. 
    print(f"Error: The file '{filename}' was not found.")
    # Exits the program with the error code 1, which means an error has occurred
    sys.exit(1)
```
I use except UnicodeDecodeError to catch any files inputted that aren't text files. For example, binary files, png files. To test this, I used the plottask.png file from Weekly Task 08 to make sure the error message prints. I use Exception next, stored as e to catch any other types of unexpected errors that could come through the program. 
Information on using Exception was found on [stackoverflow.com](https://stackoverflow.com/questions/18982610/difference-between-except-and-except-exception-as-e) and on [Python.org](https://docs.python.org/3/library/exceptions.html#os-exceptions).


```
# Error handling with except statement to catch when a file can't be read as UTF-8 (e.g. png file, binary file)    
except UnicodeDecodeError:
    # Print error message for user.
    print(f"Error: The file '{filename}' could not be read as a text file.")
    # Exit the program with the error code 1, which means an error has occurred.
    sys.exit(1)

# Error handling with except statement to catch any other unexpected errors and print an error for user.
except Exception as e:

  # Print error message for user.
  print(f"An unexpected error occurred: {e}")
  # Exit the program with the error code 1, which means an error has occurred.
  sys.exit(1)
```

Now after setting up the error handling, I look at the main function (which I have named, main). I use the len()- function, see [Realpython.com len()](https://realpython.com/len-python-function/),  to count the number of arguments passed to the command line. Since the iteration starts with 0, it also counts the name of the program as one argument. This line checks the script es.py, with the index 0 and the arguement passed in, the file name, with the index 1. So I have the if statement to check for less than 2 to only check for the script name and the arguement passed in. It checks for if the user inputed a file name, and then prints out information for the user on how to run the program. I found the information on using sys.argv on [Geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/) and [Stackoverflow.com](https://stackoverflow.com/questions/29045768/how-to-use-sys-argv-in-python-to-check-length-of-arguments-so-it-can-run-as-scri) helpful here. 

```
# Define the main function that will run the program.
def main():

    # Check for filename argument passed in the command line.
    # Use sys.argv to pass in the script name and the arguement. 
    if len(sys.argv) < 2:
        
        # Print a message to user if they dont input a file on how to do so.
        print("Run on Command line: python es.py <filename>")

        # Exit the program with the error code 1, which means an error has occurred.
        sys.exit(1)
```

I store the filename as the second arguement. I use the os.path.isfile(), see 
[Geeksforgeeks.org os.path.isfile()](https://www.geeksforgeeks.org/python-os-path-isfile-method/), to check if the file actually exists and is a file, that it is not a directory or invalid path. If it is not, it will print out an error for the user. I call the function to count the number of 'e's in the file and then print out the results for the user. 

```
# Store the file name inputted as the second argument.
filename = sys.argv[1]

# Check if the given file path actually is a valid file.
if not os.path.isfile(filename):
    # If so, print error message for user.
    print(f"Error: '{filename}' is not a valid file.")
    # Exit the program with the error code 1, which means an error has occurred.
    sys.exit(1)

# Call the function to count 'e's.
number_of_es = count_e(filename)
# Print out the results.
print(f"The file '{filename}' contains {number_of_es} lowercase 'e' characters.")
```

I use the name gaurd to make sure that main() only runs when this file is being used, and not when it's imported into another Python script. Information on name gaurd was found on [Stackoverflow.com Name Gaurd](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

```
# Run the main function using Name Gaurd. 
if __name__ == "__main__":
    main()
```

## Additional Rescourses: 

**Additional Information on SYS Module.**

[Stackoverflow.com](https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments)

**Additional Information on OS Module.**

[w3schools.com](https://www.w3schools.com/python/module_os.asp))

**Additional Information on OS Exceptions.**

[Python.org](https://docs.python.org/3/library/exceptions.html#os-exceptions)

**Unicode Documentation (encoding='utf-8').**

[Python.org](https://docs.python.org/3/howto/unicode.html)

**Additional Information on Name Guard.**

[Betterstack.com](https://betterstack.com/community/questions/what-does-if-name-is-main-do-in-python/)


# Weekly Task 8 - plottask.py
Write a program called plottask.py that displays:

a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range 0 to 10, 
on the one set of axes.

Some marks will be given for making the plot look nice (legend etc).

Please put a copy of the image of the plot (.png file) into the repository

## Code explained 

To generate a histogram, I use numpy and matplotlib libraries. I import pyplot which I use to plot the function.

```
import numpy as np
import matplotlib.pyplot as plt
```


I create the normal distribution next with the information given in the task: 1000 values, mean=5, std=2.

```
# Create a normal distribution with the values, mean and standard deviation given in task outline.
mean = 5
std_dev = 2
num_samples = 1000
```


I use the random.normal function in numpy to generate random data for my histogram.

```
# Generate some random data using the normal distribution.
data = np.random.normal(mean, std_dev, num_samples)
```

I am using plt.subplot() to show the histogram and function plot side by side. I follow [Matplotlib Subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html) documentation. I also follow the guidance from the [Matplot lib Histogram](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html) documentation to plot out my histogram. Using plt.hist() I divide the data in 30 bins to make the histogram tidy, I set the label as Normal Distribution which will reflect on the legend later.  I set the title of the histogram with plt.title(), as well as the names of the x and y axis using plt.xlabel() and plt.ylable() respectively. See [Matplot lib Pyplot.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html), [Matplot lib Pyplot.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html) and [Matplot lib Pyplot.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html) for details on this.

Working with histograms I need to make sure my axis are correctly set up. I set the xlabel as 'Value'. This sets the x axis to show the values or bins.  I set the y label as 'Frequency'. This sets the y axis to shows the frequency of how often the data shows up in the range. 

```
# Plot the histogram.
# 1 row, 2 columns, first subplot.
plt.subplot(1, 2, 1)

plt.hist(data, bins=30, color='pink', edgecolor='purple', label='Normal Distribution')
plt.title('Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
```

I add the legend to the Histogram. I use loc='upper left' to try not be in the way of the graphs data. I refer to [Geeksforgeeks.org](https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/) on guidance about adding a legend to the histogram.

```
# Add a legend to the histogram.
plt.legend(loc='upper left')
```

I plot the function using the np.arange() function, see [Numpy.org np.arange()](https://numpy.org/doc/stable/reference/generated/numpy.arange.html) for guidance, then I have to create the x values for the rang of 0 - 10 as instructed in the task. I add a step of 0.1. I selected a smaller step size as it gives me a smoother visual for the graph. I tested with a step of 1 and it was hard to read. I also refer to [Geeksforgeeks.org](https://www.geeksforgeeks.org/numpy-arrange-in-python/) for guidance on the np.arange function.

```
# Plot the function h(x) = x^3 using np.arange().
# Create x values from 0 to 10 with a step of 0.1.
x_values = np.arange(0, 10, 0.1)  
```

I calculate the function h(x)=x3. I need to take x, and raise it to the power of 3. I do this by using the exponentiation operator **. I looked this up at 
[Geeksforgeeks.org](https://www.geeksforgeeks.org/python-program-to-find-cube-of-a-number/).
```
# Calculate y = x^3.
y_value = x_values**3  
```

I follow the guidance from the [Matplotlib Plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html) documentation to plot out my function plot. Same as when I was plotting my histogram, I  add my x and y values, I set the colour, label the function and the title. I add a legend the same way as I did for the histogram.

```
# Create the function plot.
# 1 row, 2 columns, second subplot.
plt.subplot(1, 2, 2)  

plt.plot(x_values, y_value, color='purple', label='h(x) = x^3')
plt.title('Plot of h(x) = x^3')
plt.xlabel('x')
plt.ylabel('h(x)')

# Add a legend to the function plot.
plt.legend(loc='upper left' )
```
I save the histogram and plot as a PNG using plt.save fig. I refer to information on [matplotlib.org](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html) for this.  Note: I had to change the flow of plt.show() and plt.savefig(). If I ran plt.show() first, the saved file would come up blank. They were interferring with each other. So I have plt.savefig() come first. 

```
# Save the histogram and plot.
plt.savefig('plottask.png')

```
Using subplots means that the graps could overlap at the axis, title etc. I researched the tight_layout() function on [Geeksforgeeks.org](https://www.geeksforgeeks.org/matplotlib-pyplot-tight_layout-in-python/) and use it to prevent any overlap and keep the grap looking tidy. Then I use plt.show() to show the graph. 
```
# Adjust layout to avoid any overlap of the histogram or plot.
plt.tight_layout()

# Display the plots.
# This will open a window showing the plots.
plt.show()
```

## Additional Rescourses: 

**Information on Histograms, particularly useful for information on the Horizontal and Vertical axis.**

[Geeksforgeeks.org](https://www.geeksforgeeks.org/histogram/)

**Datacamp Guide to Histograms.**

[Datacamp.com](https://www.datacamp.com/blog/frequency-histograms?utm_source=chatgpt.com)




# Contact Information

Student ID: G00472977

Contact Email: G00472977@atu.ie


# Rescources:

Useful template for creating this ReadMe file- [Github Best ReadMe Template](https://github.com/othneildrew/Best-README-Template/blob/main/README.md)

Useful to help format and use correct syntax for the ReadMe File, particularly for quoting code or references - [Githubdocs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

Useful introduction to Python - [Python.org](https://docs.python.org/3/tutorial/introduction.html#)

Python CheatSheet (2025) - [Geeksforgeeks.org](https://www.geeksforgeeks.org/python-cheat-sheet/)



