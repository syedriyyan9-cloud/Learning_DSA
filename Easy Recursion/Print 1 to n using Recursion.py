"""
Given an integer n. Print numbers from 1 to n using recursion.

Examples:

Input: n = 3
Output: [1, 2, 3]
Explanation: We have to print numbers from 1 to 3.

Input: n = 10
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

def show(n :int):
    """this function prints numbers from 1 to n."""
    if n == 0:
        return 0
    show(n-1)
    print(n)
        
if __name__ == '__main__':
    show(3)