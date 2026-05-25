"""
Given two integers n and m, print a hollow rectangle star pattern of the given n rows and m columns. In this pattern, stars (*) are printed on the boundary of the rectangle, while the inner area contains spaces.

Example:

Input: n = 6, m = 20
Output:
        * * * * * * * * * * * * * * * * * * * *
        *                                     *
        *                                     *
        *                                     *
        *                                     *
        * * * * * * * * * * * * * * * * * * * *

"""

def hollow_rectangle(n, m):
    """Print Hollow Rectangle"""
    first_line = 0
    last_line = n-1
    for i in range(n):
        if i == first_line or i == last_line:
            for _ in range(m):
                print('*', end='')
            print()
        else:
            print('*', end='')
            print((m-2) * ' ', end='')
            print('*')

if __name__ == '__main__':
    hollow_rectangle(6,20)