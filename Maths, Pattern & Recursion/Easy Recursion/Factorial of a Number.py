"""

Given a non-negative integers n, compute the factorial of the given number. 
Factorial of n is defined as n * (n -1) * (n - 2) * ... * 1. For n = 0, the 
factorial is defined as 1.

Examples:

Input: n = 5
Output: 120
Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120

Input: n = 4
Output: 24
Explanation: 4! = 4 * 3 * 2 * 1 = 24

Input: n = 0
Output: 1

Input: n = 1
Output: 1

"""

def factorial(n: int):
    """calculate factorial of n"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
if __name__ == '__main__':
    print(factorial(5))