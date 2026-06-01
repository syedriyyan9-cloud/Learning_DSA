"""

Given a positive integer n, find all the distinct divisors of n.

Examples:

Input: n = 10       
Output: [1, 2, 5, 10]
Explanation: 1, 2, 5 and 10 are the divisors of 10. 

Input: n = 100
Output: [1, 2, 4, 5, 10, 20, 25, 50, 100]
Explanation: 1, 2, 4, 5, 10, 20, 25, 50 and 100 are divisors of 100.

"""

# My Solution

def factors(n: int) -> list:
    """Returns a list of factors"""
    all_factors = []
    for i in range(1,n+1):
        if n % i == 0:
            all_factors.append(i)
    return all_factors

if __name__ == '__main__':
    print(factors(100))

"""

Expected Solution:
If we look carefully, all the divisors of a number appear in pairs.
For example, if n = 100, then the divisor pairs are:
(1, 100), (2, 50), (4, 25), (5, 20), (10, 10).

We need to be careful in cases like (10, 10)—i.e., when both divisors in a pair 
are equal (which happens when n is a perfect square). In such cases, we should include that 
divisor only once.
Using this fact, we can optimize our program significantly.

Instead of iterating from 1 to n, we only need to iterate from 1 to √n.
Why? Because for any factor a of n, the corresponding factor b = n / a forms a pair (a, b).
At least one of the two values in any such pair must lie within the range [1, √n].

Code:

import math

def printDivisors(n):
    divisors = []
    
    # Loop runs up to square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            
            # If both divisors are same (perfect square), add only once
            if n // i == i:
                divisors.append(i)
            else:
                
                # Add both divisors
                divisors.append(i)
                divisors.append(n // i)
    return divisors

if __name__ == "__main__":
    number = 10
    divisors = printDivisors(number)

    for div in divisors:
        print(div, end=" ")

"""