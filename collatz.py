# collatz.py

# This program asks the user to input a positive int and outputs sucessive values following the collatz rule
# Collatz rule:
# If even number inputted, divide by 2
# If odd, multiply by 3 and add 1
# The program will end if the current value is one.

# Author: Laura Donnelly

# rescources:

# Information on the Collatz Problem
# [Link] https://www.askpython.com/python/examples/collatz-conjecture

# Looked at examples others did 
# [Link] https://codereview.stackexchange.com/questions/285429/automate-the-boring-stuff-with-python-the-collatz-sequence

# Error on code - IndentationError: expected an indented block after function definition
# Below resources helped to fix, I wasn't spacing/tabing code correctly first time
# [Link] https://www.youtube.com/watch?v=w5styN3Vaqw 
# [Link] https://stackoverflow.com/questions/4446366/why-am-i-getting-indentationerror-expected-an-indented-block


# This function allows the programme to take input from the user, which is used to ask the user for a positive integer.

# resources:
# [Link] https://docs.python.org/3/library/functions.html#input

def collatz():
    # Prompt the user to input a positive integer
    number = int(input("Please enter a positive integer: "))
    
    # Ensure the number is positive
    if number <= 0:
        print("Please enter a positive integer.")
        return

# Python Lists Lists are used to store multiple items in a single variable. Need this in the program to store the sequence of numbers

# resources:
# [Link] https://www.w3schools.com/python/python_lists.asp

    # Create a list to store the sequence
    sequence = []

# The while Loop With the while loop the program can execute a set of statements as long as a condition is true.

# resources:
# [Link] https://www.w3schools.com/python/python_while_loops.asp
# [Link] https://www.youtube.com/watch?time_continue=175&v=ECduJk00mUU&embeds_referring_euri=https%3A%2F%2Fwww.bing.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.bing.com&source_ve_path=Mjg2NjY


    # Continue the process until the number becomes 1
    while number != 1:

# Python List append() Method The append() method adds a single element to the end of a list. 
# It modifies the original list in place and does not return a new list.

# resources:
# [Link] https://www.w3schools.com/python/ref_list_append.asp


        # Add the current number to the sequence
        sequence.append(number)

# This resource explains how if, else, and elif statements work in Python
# to handle different conditions like checking if a number is even or odd.

# resources:
# [Link] https://www.w3schools.com/python/python_conditions.asp

        # Apply the Collatz rule
        if number % 2 == 0:
            number = number // 2  # If even, divide by 2
        else:
            number = 3 * number + 1  # If odd, multiply by 3 and add 1

    # Add 1 to the sequence as the loop ends when number becomes 1
    sequence.append(1)

# The join() method is used to convert a list of numbers into a string with spaces between them.

# resources:
# [Link] https://docs.python.org/3/library/stdtypes.html#str.join https://www.w3schools.com/python/ref_string_join.asp

    # Output the sequence as a space-separated string
    print(" ".join(map(str, sequence)))

print(collatz())
  













