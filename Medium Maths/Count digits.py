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


def count_digits(n: int) -> int:
    '''a function to count the digits in a number n'''
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

if __name__ == '__main__':
    print(count_digits(1567))
