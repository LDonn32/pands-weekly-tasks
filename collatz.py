# Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

# Have the program end if the current value is one.

# Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).

# Example of it running:

# $ python collatz.py

# Please enter a positive integer: 10

# 10 5 16 8 4 2 1

# Author: Laura Donnelly


# collatz.py

def collatz():
    # Prompt the user to input a positive integer
    number = int(input("Please enter a positive integer: "))
    
    # Ensure the number is positive
    if number <= 0:
        print("Please enter a positive integer.")
        return

    # Create a list to store the sequence
    sequence = []

    # Continue the process until the number becomes 1
    while number != 1:
        # Add the current number to the sequence
        sequence.append(number)
        
        # Apply the Collatz rule
        if number % 2 == 0:
            number = number // 2  # If even, divide by 2
        else:
            number = 3 * number + 1  # If odd, multiply by 3 and add 1
    
    # Add 1 to the sequence as the loop ends when number becomes 1
    sequence.append(1)
    
    # Output the sequence as a space-separated string
    print(" ".join(map(str, sequence)))

if __name__ == "__main__":
    collatz()
