"""

Given an integer n. Print numbers from n to 1 using recursion.

Examples:

Input: n = 3
Output: [3, 2, 1]
Explanation: Print numbers in reverse order from n down to 1.

Input: n = 10
Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Explanation: Print numbers in reverse order from n down to 1

"""

def display(n: int):
    """Displays n to 1 numbers"""
    if n == 0:
        return
    else:
        print(n)
        display(n-1)

if __name__ == '__main__':
    display(10)