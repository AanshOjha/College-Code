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


'''
*
**
***
****
***
**
*
'''

rows = 4  # Number of asterisks at the widest point

# 1) Increasing part
for i in range(1, rows + 1):    # 1 to rows
    for j in range(i):          # Print i stars
        print('*', end='')
    print()                     # Newline

# 2) Decreasing part
for i in range(rows - 1, 0, -1):  # rows-1 down to 1
    for j in range(i):            # Print i stars
        print('*', end='')
    print()
