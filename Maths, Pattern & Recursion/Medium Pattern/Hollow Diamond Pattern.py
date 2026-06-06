"""

Given an integer N, print the pattern shown below.

Examples:
input = 5
output:
                    *
                *       *
            *               *
        *                       *
    *                               *
        *                       *
            *               *
                *       *
                    *
"""

def hollow_diamond(n: int) -> None:
    """draws a hollow diamond"""

    # prints the first star
    print(n * " ", end="")
    print("*")

    # prints the top of the diamond after first star
    for j,k in zip(range(n-1,0,-1), range(1,n)):
        print(j * " ", end="")
        print("*", end="")
        print(k * 2 * " ", end="")
        print("*")
    
    #prints the bottom of the diamond after mid line
    for j,k in zip(range(n,0,-1), range(n)):
        print(k * " ", end="")
        print("*", end="")
        print(j * 2 * " ", end="")
        print("*")

    # prints the last star
    print(n * " ", end="")
    print("*")


if __name__ == '__main__':
    hollow_diamond(7)