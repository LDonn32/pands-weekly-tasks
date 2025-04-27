# es.py
# Weekly task 7

# Author: Laura Donnelly


# Import packages.

# Import sys to handle command-line arguments and exit the program.
import sys

#Import os to check if a given path is a valid file.
import os

# Define the function that will count the number of lowercase 'e's in a file.
def count_e(filename):

    # Error handling using try and except statements to catch any possible errors.
    try:

        # Open the file in read mode with UTF-8 encoding. 
        # Using with to close the file automaticall when done.

        with open(filename, 'r', encoding='utf-8') as file:

            # Read the file using read().
            text = file.read()

            # Count the number of lowercase 'e's.
            return text.count('e')
        
    # Error handling with except statement to catch when the file doesn't exist.    
    except FileNotFoundError:

        # Print error message for user. 
        print(f"Error: The file '{filename}' was not found.")

        # Exits the program with the error code 1, which means an error has occurred. 
        sys.exit(1)

    # Error handling with except statement to catch when a file can't be read as UTF-8 (e.g. png file, binary file).   
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

# Define the main function that will run the program.
def main():

    # Check for filename argument passed in the command line.
    # Use sys.argv to pass in the script name and the arguement. 
    if len(sys.argv) < 2:
        
        # Print a message to user if they dont input a file on how to do so.
        print("Run on Command line: python es.py <filename>")

        # Exit the program with the error code 1, which means an error has occurred.
        sys.exit(1)

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


# Run the main function using Name Gaurd. 
if __name__ == "__main__":
    main()
