"""

Given two numbers b(base) and e(exponent), calculate the value of be.

Examples: 

Input: b = 3.00000, e = 5
Output: 243.00000

Input: b = 0.55000, e = 3
Output: 0.16638

Input: b = -0.67000, e = -7
Output: -16.49971

"""

def power_function(b, e):
    if e == 0:
        return 1
    if e < 0:
        return 1 / power_function(b, -e)
    return b * power_function(b, e - 1)


if __name__ == '__main__':
    print(power_function(2,4))
