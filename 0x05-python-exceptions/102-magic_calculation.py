#!/usr/bin/python3

def magic_calculation(a, b):
    # Initialize the result variable
    result = 0

    # Iterate from 1 to 3
    for i in range(1, 3):
        try:
            # Check if i is greater than a
            if i > a:
                # Raise an exception with the message 'Too far'
                raise Exception('Too far')
            else:
                # Calculate the intermediate result
                result += a ** b / i
        except:
            # If an exception occurs, set the result to b + a
            result = b + a
            # Exit the loop
            break

    # Return the final result
    return result
