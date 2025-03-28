# Write a program that takes 
# a positive floating-point number as input and 
# outputs an approximation of its square root.

# create a function called <tt>sqrt</tt> that does this.


# Author: Laura Donnelly


#[Link] appropriated some code from below link. Modified it to take user input 
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

# Function to return the square root of
# a number using Newton's method
def squareRoot(n, l):
    # Assuming the sqrt of n as n only
    x = n

    # To count the number of iterations
    count = 0

    while True:
        count += 1

        # Calculate more closed x
        root = 0.5 * (x + (n / x))

        # Check for closeness
        if abs(root - x) < l:
            break

        # Update root
        x = root

    return root

# Take a positive floating-point number as input
n = float(input("Enter a positive number: "))

# Ensure that the number is positive
if n <= 0:
    print("Please enter a positive number.")
else:
    l = 0.00001  # Tolerance for the approximation
    print(f"Approximate square root of {n} is {squareRoot(n, l)}")



















