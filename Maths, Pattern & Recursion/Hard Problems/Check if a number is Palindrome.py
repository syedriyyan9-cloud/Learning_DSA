"""

Given an integer n, determine whether it is a palindrome number or not. A number is called a 
palindrome if it reads the same from forward and backward.

Examples:

Input: n = 12321
Output: True
Explanation: 12321 is a palindrome number because it reads same  forward and backward.

Input: n = -121
Output: True
Explanation:  We number is palindrome, we mainly ignore sign.

Input: n = 1234
Output:  False
Explanation: 1234 is not a palindrome number because it does not read the same forward and 
backward.

"""

# My Solution
# first convert numbers to positive
# then variable containing the opposite order of digits
# if both are same then true else false

def is_palindrome(n: int) -> bool:
    """Returns true if number is palindrome, otherwise false"""
    # convert number to positive
    if n < 0:
        n = -n
    n_copy = n
    # variable containing opposite order of digits
    opposite = 0
    while n > 0:
        opposite += n % 10
        opposite *= 10
        n //= 10
    opposite //= 10
    # if condition to check for palindrome
    if opposite == n_copy:
        return True
    return False

if __name__ == '__main__':
    print(is_palindrome(-121))

"""

Expected Approach:

The idea is to find the reverse of the original number and then compare the reversed number 
with the original number. If the reversed number is same as the original number, the number 
is palindrome. Otherwise, the number is not a palindrome.  

Code:

def isPalindrome(n):
    reverse = 0

    # Copy of the original number so that the original
    # number remains unchanged while finding the reverse
    temp = abs(n)
    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10

    # If reverse is equal to the original number, the
    # number is palindrome
    return (reverse == abs(n))
    
if __name__ == "__main__":
    
    n = 12321
    if isPalindrome(n) == True:
        print("True")
    else:
        print("False")

"""