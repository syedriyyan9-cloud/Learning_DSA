"""

Given a m litre jug and a n litre jug where 0 < m < n, both initially empty and without any 
markings to measure intermediate quantities. You need to measure d litres of water where d < n. 
The operations you can perform are: 

Empty a Jug
Fill a Jug (You may assume that you have unlimited supply of water)
Pour water from one jug to the other until one of the jugs is either empty or full

Find the minimum number of operations required to obtain exactly d litres of water in 
either of the two jugs. If it is not possible, return -1.

Examples:

Input: m = 2, n = 3, d = 1
Output: 2
Explanation: 
1. Fill up the 3 litre jug
2. Pour 2 litre of water from the 3 litre jug to 2 litre Jug, Now the 3 litre jug has 1 
litre water.

Input: m = 3, n = 5, d = 4
Output: 6
Explanation: Explained in the above images.

Input: m = 2, n = 3, d = 5
Output: -1
Explanation: As d > n here, it is not possible to measure exactly 5 litres using the given jugs.

Input: m = 2, n = 4, d = 3
Output: -1
Explanation: Not possible since gcd(2, 4) = 2 does not divide 3.

"""