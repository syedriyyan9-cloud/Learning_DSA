"""

Given a number n, return the count of digits in this number.

Example:

Input: n = 1567
Output: 4
Explanation: There are 4 digits in 1567, which are 1, 5, 6 and 7.

Input: n = 255
Output: 3
Explanation: There are 3 digits in 255, which are 2, 5 and 5.

"""

# Below is the iterative approach
# def count_digits(n: int) -> int:
#     '''a function to count the digits in a number n'''
#     count = 0
#     while n != 0:
#         count += 1
#         n //= 10
#     return count

# Below is the recursive approach
def count_digits(n: int) -> int:
    """a recurisve function to count the digits in a number n"""
    if n == 0:
        return 0
    else:
        n //= 10
        return 1 + count_digits(n)

if __name__ == '__main__':
    print(count_digits(12))




"""
Expected approach:

We can use log10(logarithm of base 10) to count the number of digits of positive numbers (logarithm is not defined for negative numbers). For negative numbers, first take the absolute value of n, since logarithm is not defined for negative values.
Digit count of n = floor(log10(n) + 1) 

Code:

import math

def countDigit(n):
    # Handle zero separately
    if n == 0: return 1

    # Convert negative to positive
    n = abs(n)

    return math.floor(math.log10(n)) + 1

if __name__ == "__main__":
    n = -58964
    print(countDigit(n))
"""