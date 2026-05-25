"""
Given an integer n, print Floyd's Triangle with n rows. Floyd's Triangle is a right-angled triangular pattern formed using consecutive natural numbers starting from 1.

Example:

Input: 6

Output:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21

"""

def floyd_triangle(n):
    """Print floyd triangle"""
    inc = 1
    for i in range(1, n+1):
        for _ in range(i):
            print(inc, end=" ")
            inc += 1
        print()

if __name__ == '__main__':
    floyd_triangle(6)