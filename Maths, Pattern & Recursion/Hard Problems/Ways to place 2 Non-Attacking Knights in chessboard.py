"""

Given two integers, n and m, denoting dimensions of a chessboard. The task is to count ways 
to place a black and a white knight on an n * m chessboard such that they do not attack 
each other. The knights have to be placed on different squares.

Note: A knight can move two squares horizontally and one square vertically (L shaped), or 
two squares vertically and one square horizontally (L shaped). The knights attack each other 
if one can reach the other in one move.

Examples:

Input: n = 2, m = 2
Output: 12

Explanation: The first Kniight can be placed in any of the 4 cells and the second knight can 
be be placed in any of the remaining 3 cells. For a Knight to attack. one dimension must be 
at least 3.

Input: n = 2, m = 3
Output: 26

"""