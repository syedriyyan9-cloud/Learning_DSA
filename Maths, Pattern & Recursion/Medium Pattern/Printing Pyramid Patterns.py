"""

Given a positive integer n, print a pyramid pattern consisting of stars (*) 
such that the number of rows equals n. The pyramid should be center-aligned as 
shown in the example below.

Example:

input: 3
output:
            *
           ***
          *****

"""

def pyramid(n: int) -> None:
    """Prints pyramid with n rows"""
    print(n * ' ', end='')
    print('*')
    for j, k in zip(range(n-1,0,-1),range(1,n)):
        print(j * ' ', end='')
        print((k + (k+1)) * '*')
        # print('asdf')


if __name__ == '__main__':
    pyramid(5)