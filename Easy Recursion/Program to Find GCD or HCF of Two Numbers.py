"""

Given two positive integers a and b, the task is to find the GCD of the two numbers.

Note: The GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers 
is the largest number that divides both of them. 

Examples:

Input: a = 20, b = 28
Output: 4

Explanation: The factors of 20 are 1, 2, 4, 5, 10 and 20. The factors of 28 are 1, 2, 4,
7, 14 and 28. Among these factors, 1, 2 and 4 are the common factors of both 20 and 28. 
The greatest among the common factors is 4.

Input: a = 60, b = 36
Output: 12
Explanation: GCD of  60 and 36 is 12.

"""

def GCD(n: int, m: int):
    """Calculates the Greatest Common Divisor of n and m"""
    if n == 0 or m == 0:
        return 
    else:
        pass