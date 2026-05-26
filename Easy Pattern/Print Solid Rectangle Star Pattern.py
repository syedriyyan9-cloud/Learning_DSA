"""
Given two integers n and m, print a solid rectangle pattern of stars with n rows and m columns. Each row has exactly m stars.


Input: n = 3, m = 5

Output: *****
        *****
        *****

Input: n = 4, m = 2

Output: **
        **
        **
        **
"""

def rectangle_pattern(n,m):
    """A function to print a solid rectangle of n rows and m columns"""

    for _ in range(n):
        print(m * '*')

if __name__ == '__main__':
    rectangle_pattern(3,5)