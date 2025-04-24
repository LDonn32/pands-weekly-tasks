# es.py
# Weekly task 7

# Author: Laura Donnelly


# Import packages.

# Import sys to handle command-line arguments and exit the program.
import sys

#Import os to check if a given path is a valid file.
import os

# Define the function.
def count_e(filename):
    # Error handling using try and except statements.
    try:
        # Open the file in read mode with UTF-8 encoding.
        with open(filename, 'r', encoding='utf-8') as file:
            # Read in the file.
            text = file.read()
            # Count the number of lowercase 'e's.
            return text.count('e')
        
    # Error handling with except statement to catch when the file doesn't exist.    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    # Error handling with except statement to catch when a file can't be read as UTF-8 (e.g. png file, binary file)    
    except UnicodeDecodeError:
        print(f"Error: The file '{filename}' could not be read as a text file.")
        sys.exit(1)
    # Error handling with except statement to catch any other unexpected errors and print an error for user.
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    # Check for filename argument passed in the command line. 
    if len(sys.argv) < 2:
        print("Run on Command line: python es.py <filename>")
        sys.exit(1)

    # Store arguement as a variable to call on later.
    filename = sys.argv[1]

    # Check if the given file path is a valid file.
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a valid file.")
        sys.exit(1)

    # Call the function to count 'e's.
    number_of_es = count_e(filename)
    # Print out the results.
    print(f"The file '{filename}' contains {number_of_es} lowercase 'e' characters.")


# Run the main function using Name Gaurd. 
if __name__ == "__main__":
    main()
