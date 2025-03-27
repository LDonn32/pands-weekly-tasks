# Write a program that takes 
# a positive floating-point number as input and 
# outputs an approximation of its square root.

# create a function called <tt>sqrt</tt> that does this.


# Author: Laura Donnelly

# Resources on New
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/


def sqrt(n, tolerance=1e-10):
    # 

    if n < 0:
        raise ValueError("Input must be a positive number")
    
    # Initial guess (could be any positive number, but n/2 is a reasonable start)
    guess = n / 2.0
    
    # Iteratively improve the guess using Newton's method
    while True:
        # Calculate a new guess
        new_guess = 0.5 * (guess + n / guess)
        
        # Check if the difference between guesses is within the tolerance
        if abs(new_guess - guess) < tolerance:
            break
        
        # Update guess for the next iteration
        guess = new_guess
    
    return guess

# still working on getting this to print out on terminal.
# testing a few ideas before researching 

# print(guess)

# no i need to get inputs and string messages for user input then output
# researching and coming back to this


# return two varriables 
# assign two varriables
# print two varriables
# use an f statement to run 