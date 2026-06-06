"""

Given a number n, check whether it is a prime number or not.
Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Input: n = 7
Output: true
Explanation: 7 is a prime number because it is greater than 1 and has no divisors other than 1 and itself.

Input: n = 25
Output: false
Explanation: 25 is not a prime number because it is divisible by 5 (25 = 5 * 5), so it has divisors other than 1 and itself.

Input: n = 1
Output: false
Explanation: 1 has only one divisor (1 itself), which is not sufficient for it to be considered prime.

"""

# My Approach
def is_prime(n: int) -> bool:
    """Checks whether a number is prime or not, returns True or False"""
    n1 = 2
    while n1 <= (n//2):
        if n % n1 == 0:
            return False
        n1+= 1
    return True

if __name__ == '__main__':
    print(is_prime(6))

"""

Expected approach:

Numbers that are divisible by 2 or 3 are not prime, so we can skip them entirely. To check whether a number is prime, it is sufficient to test only the numbers of the form 6k ± 1 up to √n.

Code:

import math

def isPrime(n):

    # Check if n is 1 or 0
    if n <= 1:
        return False

    # Check if n is 2 or 3
    if n == 2 or n == 3:
        return True

    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    #Check numbers of the form 6k ± 1 up to √n
    i = 5
    while i*i<=n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
  n = 7
  if(isPrime(n)): 
    print("true")
  else:
    print("false")

"""