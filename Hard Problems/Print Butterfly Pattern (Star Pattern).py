"""

Given an integer N, print a butterfly star pattern with 2N − 1 rows. The number of stars
increases from 1 to N in the upper half and then decreases from N − 1 to 1 in the lower half,
forming a symmetric butterfly shape.


Examples:

Input: 3
Output: 
*      *
**  **
*****
**  **
*      *

Input: 5
Output: 
*              *
**          **
***      ***
****  ****
*********
****  ****
***      ***
**          **
*              *
"""

# My Solution
# first focus on creating ladder pattern
# then inverse it to get the lower part
# then work on legs of butterfly

def butterfly(n: int) -> None:
    """Returns None, prints a butterfly pattern"""
    # prints upper half
    for i in range(1,n):
        print(i * '*', end="")
        print(((n-i) * n) * ' ', end="")
        print(i * '*')
    # prints backbone or body
    print((n*2-1) * '*')
    # prints lower half
    for j in range(n-1, 0, -1):
        print(j * '*', end="")
        print(((n-j) * n) * ' ', end="")
        print(j * '*')

if __name__ == '__main__':
    butterfly(3)

"""

Expected Appraoch:

The butterfly pattern can be printed using nested loops. The outer loop runs for all rows, 
while three inner loops are used to print the left stars, spaces, and right stars. In the 
upper half, the number of stars increases and spaces decrease. In the lower half, the stars 
decrease and spaces increase, forming the butterfly shape.

Code:

def main():

    # Number of rows
    n = 5

    # Variables to store number of spaces and stars
    spaces = 2 * n - 1
    stars = 0

    # The outer loop will run for (2 * n - 1) times
    for i in range(1, 2 * n):

        # Upper half of the butterfly
        if i <= n:
            spaces = spaces - 2
            stars += 1

        # Lower half of the butterfly
        else:
            spaces = spaces + 2
            stars -= 1

        # Print stars
        for j in range(1, stars + 1):
            print("*", end="")

        # Print spaces
        for j in range(1, spaces + 1):
            print(" ", end="")

        # Print stars
        for j in range(1, stars + 1):
            if j != n:
                print("*", end="")

        print()


if __name__ == "__main__":
    main()

"""