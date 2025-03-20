# Weekly task 7
# Write a program that reads in a text file and outputs the number of e's it contains
# Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line

# Author: Laura Donnelly


# https://www.geeksforgeeks.org/python-sys-module/

# https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments




# This defines a function named count_e_in_file. 
# The function takes one parameter, filename, which is expected to be the path to the file we want to read and count occurrences of 'e' in.

import os
import sys

def count_e_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Count occurrences of both 'e' and 'E'
            e_count = content.lower().count('e')
            return e_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    except IsADirectoryError:
        print(f"Error: Expected a file but found a directory: '{filename}'.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: The file '{filename}' is not a valid text file or contains invalid encoding.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Prompt the user for the filename
filename = input("Please enter the filename: ")

# Check if file exists and is a valid text file
if not os.path.isfile(filename):
    print(f"Error: '{filename}' is not a valid file.")
    sys.exit(1)

# Call the function to count occurrences of 'e'
e_count = count_e_in_file(filename)
print(f"The file '{filename}' contains {e_count} occurrences of the letter 'e'.")
