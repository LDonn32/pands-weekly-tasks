# squareroot.py
# Weekly Task 06

# Author: Laura Donnelly


# Define function to return the square root of a number using Newton's method.
def sqrt(n, l):
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
    print(f"Approximate square root of {n} is {sqrt(n, l)}")



















