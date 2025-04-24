# es.py
# Weekly task 7

# Author: Laura Donnelly


# Import packages
import sys
import os

# Define the function.
def count_e(filename):
    # Error handling.
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            return text.count('e')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: The file '{filename}' could not be read as a text file.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    # Check for filename argument
    if len(sys.argv) < 2:
        print("Run on Command line: python es.py <filename>")
        sys.exit(1)

    # Store arguement as a variable.
    filename = sys.argv[1]

    # Check if the path is a file
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a valid file.")
        sys.exit(1)

    # Call the function to count 'e's.
    number_of_es = count_e(filename)
    print(f"The file '{filename}' contains {number_of_es} lowercase 'e' characters.")


# Run the main function.
if __name__ == "__main__":
    main()
