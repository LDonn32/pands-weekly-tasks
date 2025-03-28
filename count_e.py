# Weekly task 7
# Write a program that reads in a text file and outputs the number of e's it contains
# Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line

# Author: Laura Donnelly


# https://www.geeksforgeeks.org/python-sys-module/

# https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments



# install modules
import os
import sys

# OS gives us functions to interact with the operating system like seeing if a file actually exists. 
# [Link] https://www.geeksforgeeks.org/os-module-python-examples/
# Sys gives us better control over input or output. User can engage with the terminal/ comand line more freely 
# [Link] https://www.geeksforgeeks.org/python-sys-module/

# define function
def count_e_in_file(filename):

    # here is when we define the function which will count the number of e's from the text in the program
    try:
        # Check if the file exists and is a text file
        if not os.path.isfile(filename):
            print(f"Error: '{filename}' does not exist or is not a valid file.")
            return
        
        # Open the file in read mode
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Count the occurrences of the letter 'e'

        content = file.read()

        # Counting 'e' and 'E'

        count = content.lower().count('e')  
        print(f"The number of 'e's in the file '{filename}' is: {count}")
        
        # Output the result

        print(f"The number of 'e' characters in the file '{filename}' is: {e_count}")
    
    # Configure our excpetions 

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")    

# Ensure that there is a filename argument

if len(sys.argv) != 2:
    print("Usage: python count_e.py <filename>")
    sys.exit(1)

# Get the filename from the command line argument

filename = sys.argv[1]

# Call the function to count 'e' in the given file

count_e_in_file(filename)


# still having trouble getting the file to read in the terminal - i think maybe linked to my actual directory or how i downloaded the file. 
# # Will try either linking my diretory to the program - but that wont work for anyone else running program? 
# maybe its the way i downlaoded the text file - will try this again and save it on desktop.  