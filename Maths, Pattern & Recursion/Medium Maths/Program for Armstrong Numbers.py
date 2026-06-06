"""

Given a number x, determine whether the given number is Armstrong's number or not. A positive integer of n digits is called an Armstrong number of order n (order is the number of digits) if

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

Here a, b, c and d are digits of input number abcd.....

Examples

Input: n = 153
Output: true
Explanation: 153 is an Armstrong number, 1*1*1 + 5*5*5 + 3*3*3 = 153

Input: n = 9474
Output: true
Explanation: 94 + 44 + 74 + 44 = 6561 + 256 + 2401 + 256 = 9474

Input: n = 123
Output: false
Explanation: 1³ + 2³ + 3³ = 1 + 8 + 27 = 36

"""

# My Solution
def is_armstrong(n: int) -> bool:
    """Returns True if armstrong number, otherwise False"""
    power = len(str(n))
    n_copy = n
    armstrong = 0
    while n != 0:
        digit = n % 10
        n = n // 10
        armstrong += pow(digit,power)
    if armstrong == n_copy:
        return True
    return False

if __name__ == '__main__':
    print(is_armstrong(153))


"""

Using Numeric Strings:

The idea is to determine if a number is an Armstrong number by first converting it to a string to easily access its digits and count them. Each digit is then raised to the power of the total number of digits, and the results are summed. If this sum is equal to the original number, it is classified as an Armstrong number. This approach leverages simple string manipulation and power calculation to perform the check efficiently.

Code:

def armstrong(n):
    
    # converting to string
    number = str(n)

    # number of digits
    digits = len(number)
    output = 0

    # sum of each digit raised to the power of number of digits
    for i in number:
        output += int(i) ** digits

    # check if equal to original number
    return output == n


if __name__ == "__main__":
    n = 153
    if armstrong(n):
        print("true")
    else:
        print("false")

"""