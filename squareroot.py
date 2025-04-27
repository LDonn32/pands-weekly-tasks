# squareroot.py
# Weekly Task 06

# Author: Laura Donnelly


# Define function to return the square root of a number using Newton's method.
def sqrt(n, l):

    # This will be the first guess where the code guesses the square root of n as n.
    x = n

    # Using while true, keep improving the guess until it gets close.
    while True:
      
        # Do this by calculating using Newton's Method (x+ (n/x)). This should get x closer to the square root and give the program a more accurate guess.
        root = 0.5 * (x + (n / x))

        
        # Root is the new guess.
        # X is the old guess.
        # (root - x) will check the difference between the new and old guess.
        # Using the abs() function to return the absolute value of it.
        # If the number is close enough to the old one, the loop while break.
        if abs(root - x) < l:
            break

        # Update the guess to the new number.
        x = root

    # Return the final guess.
    return root

# Prompt user to input a positive number. Use float() function to convert it to floating-point number.
n = float(input("Enter a positive number: "))

# Ensure that the number inputted is actually a positive number. Print message to user to try again if not.
if n <= 0:
    print("Please enter a positive number.")

# Set the tolerance to how close it gets to the square number, set at 5 decimals for accuracy.
else:
    l = 0.00001  
    
# Print the results.
    print(f"Approximate square root of {n} is {sqrt(n, l)}")



















