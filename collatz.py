# collatz.py
# Weekly Task 04

# Author: Laura Donnelly


# This function allows the programme to take input from the user, which is used to ask the user for a positive integer

def collatz():
    # Prompt the user to input a positive integer
    number = int(input("Please enter a positive integer: "))
    
    # Ensure the number is positive
    if number <= 0:
        print("Please enter a positive integer.")
        return

    # Create a list to store the sequence
    sequence = []

    # Using a while loop, continue the process until the number becomes 1
    while number != 1:

        # Add the current number to the sequence using the append() function
        sequence.append(number)


        # Apply the Collatz rule using if and else statements
        if number % 2 == 0:
            number = number // 2  # If even, divide by 2
        else:
            number = 3 * number + 1  # If odd, multiply by 3 and add 1

    # Add 1 to the sequence as the loop ends when number becomes 1 using the append() function
    sequence.append(1)

    # Output the sequence as a space-separated string using the join() method
    print(" ".join(map(str, sequence)))

print(collatz())
  













