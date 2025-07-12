#numpy random
# import numpy as np

# # Generate an array of 5 random integers between 10 and 50
# random_numbers = np.random.randint(10, 51, size=5)

# print("Random numbers:", random_numbers)


"""
Write a program to create a hollow pyramid pattern given below: 
*    
* *    
*   *   
*     *  
********
"""

rows = 5

for i in range(rows):
    # for j in range(rows - i - 1):
    #     print(" ", end="")  # Print leading spaces

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == rows - 1:
            print("*", end="")  # Print star at start, end, or full row at the bottom
        else:
            print(" ", end="")  # Print space inside the pyramid
    print()  # Move to the next line
