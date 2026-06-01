"""

Given an integer n, we have to returns count of trailing zeroes in n! . 

Examples : 

Input: n = 5
Output: 1 
Explanation: Factorial of 5 is 120 which has one trailing 0.

Input: n = 10
Output: 2
Explanation: Factorial of 10  is 3628800 which have 2 trailing zeroes.

"""

# My Solution
# First calculate factorial and then use modulus to find trailing zeros

def factorial(n: int) -> int:
    """returns factorial of a number"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def trailing_zeros(n: int) -> int:
    """Returns the number of Trailing 0s"""
    factorial1 = factorial(n)
    count = 0
    while  (factorial1 % 10) == 0:
        factorial1 = factorial1 // 10
        count += 1
    return count

if __name__ == '__main__':
    print(trailing_zeros(50))


"""

Expected Approach:

The idea is to consider all prime factors of factorial n. A trailing zero is always produced by
prime factors 2 and 5. If we can count the number of 5s and 2s in n!, our task is done. 

Code:

def trailingZeroes(n):
    
    # Edge Case
    if (n < 0):
        return -1

    # Initialize result
    count = 0

    # Keep dividing n by
    # 5 & update Count
    while (n >= 5):
        n //= 5
        count += n

    return count


if __name__ == "__main__":
    n = 10
    print(trailingZeroes(n))


"""