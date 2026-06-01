"""

Given a number n, find all prime factors of n.
Note : Prime number is a natural number greater than 1 that has exactly two factors:1 and itself.

Examples:

Input: n = 18
Output: [2, 3, 3]
Explanation: The prime factorization of 18 is 2*(3^2).

Input: n = 25
Output: [5, 5]
Explanation: The prime factorization of  25 is 5^2.

"""

# My Solution
# First find factors of the number, filter only prime ones, then calculate factorization

def prime_factors(n: int) -> list:
    """Returns a list of prime_factors"""
    factor_list = []
    number = 2
    while number <= n/2:
        if n % number == 0:
            if prime_number(number):
                factor_list.append(number)
        number += 1
    return factor_list

def prime_number(n: int) -> int:
    """Returns number if it is prime otherwise None"""
    num = 2
    while num <= n/2:
        if n % num == 0:
            return None
        num += 1
    return n

def prime_factorization_numbers(n: int) -> list:
    """Returns the list of prime numbers used in prime factorization"""
    prime_list = prime_factors(n)
    factorization_list = []
    index = 0
    while index < len(prime_list):
        number = n / prime_list[index]
        if number.is_integer():
            factorization_list.append(prime_list[index])
            n //= prime_list[index]
            continue
        else:
            index += 1
    return factorization_list

if __name__ == '__main__':
    print(prime_factorization_numbers(30))


"""

Expected Approach:

Let a and b be two factors of n such that a*b = n.
If both are greater than sqrt(n), a*b > sqrt(n)*sqrt(n), 
which contradicts the expression a * b = n

Code:

import math
def primeFactors(n):
    
    # Print the number of two's that divide n
    while n % 2 == 0:
        print 2,
        n = n / 2
        
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
        
        # while i divides n , print i and divide n
        while n % i== 0:
            print i,
            n = n / i
            
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print n
    
if __name__ =="__main__":        
        
    n = 18
    primeFactors(n)

"""