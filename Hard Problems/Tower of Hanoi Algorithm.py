"""

The Tower of Hanoi is a classic mathematical puzzle involving three rods (A, B, and C) 
and n disks of different sizes. Initially, all disks are stacked on rod A in decreasing 
order of diameter - the largest disk at the bottom and the smallest at the top.
Goal is to move the entire stack to another rod (rod C) while following these rules:

Move only one disk at a time.
At each step, you can take the top disk from any rod and place it on another rod.
A disk can only be moved if it is the topmost disk of a rod.
No larger disk may be placed on top of a smaller disk.

Examples:
Input:  n = 3
Output: 
Disk 1 moved from A to C
Disk 2 moved from A to B
Disk 1 moved from C to B
Disk 3 moved from A to C
Disk 1 moved from B to A
Disk 2 moved from B to C
Disk 1 moved from A to C

Input: n = 4
Output:
Disk 1 moved from A to B
Disk 2 moved from A to C
Disk 1 moved from B to C
Disk 3 moved from A to B
Disk 1 moved from C to A
Disk 2 moved from C to B
Disk 1 moved from A to B
Disk 4 moved from A to C
Disk 1 moved from B to C
Disk 2 moved from B to A
Disk 1 moved from C to A
Disk 3 moved from B to C
Disk 1 moved from A to B
Disk 2 moved from A to C
Disk 1 moved from B to C

"""

# My Solution
# sizes can be represented as ints
# so for example 4 is the largest disk size while 1 is the smallest
# then we can use a list and its index, previous index can be treated as layer placement
# having a higher value at previous index would mean place of smaller on larger which is allowed
# having a lower value at previous index would mean placement of larger on smaller which is not allowed
# An if condition to check the sizes and enforce rule of prohibinting placement of
# larger on smaller
# number of rods are constant

def tower_of_hanoi(n: int) -> None:
    """Displays entire working process, Returns None"""
    rod_a = [x for x in range(1,n+1)]
    rod_a.sort(reverse=True)
    rod_b = []
    rod_c = []
    result = rod_a[:]
    index_count_a = 1
    index_count_b = 1
    index_count_c = 1
    while True:

        if not len(rod_b):
            popped = rod_a.pop()
            rod_b.append(popped)
            print(f'Disk {popped} moved from A to B')
            elements_in_a = len(rod_a) if len(rod_a) != 0 else index_count_a
            elements_in_b = len(rod_b) if len(rod_b) != 0 else index_count_b
        
        if not len(rod_c):
            popped = rod_a.pop()
            rod_c.append(popped)
            print(f'Disk {popped} moved from A to C')
            elements_in_a = len(rod_a) if len(rod_a) != 0 else index_count_a
            elements_in_c = len(rod_c) if len(rod_c) != 0 else index_count_c


        if elements_in_a:

            if rod_b[elements_in_b - 1] > rod_a[elements_in_a - 1]:
                popped = rod_a.pop()
                rod_b.append(popped)
                print(f'Disk {popped} moved from A to B')
                elements_in_a = len(rod_a) if len(rod_a) != 0 else index_count_a
                elements_in_b = len(rod_b) if len(rod_b) != 0 else index_count_b
                # print('works')
                

            elif rod_c[elements_in_c - 1] > rod_a[elements_in_a - 1]:
                popped = rod_a.pop()
                rod_c.append(popped)
                print(f'Disk {popped} moved from A to C')
                elements_in_c = len(rod_c) if len(rod_c) != 0 else index_count_c
                elements_in_a = len(rod_a) if len(rod_a) != 0 else index_count_a
                

        if elements_in_b:
            if rod_c[elements_in_c - 1] > rod_b[elements_in_b - 1]:
                popped = rod_b.pop()
                rod_c.append(popped)
                print(f'Disk {popped} moved from B to C')
                elements_in_b = len(rod_b) if len(rod_b) != 0 else index_count_b
                elements_in_c = len(rod_c) if len(rod_c) != 0 else index_count_c
                

            elif rod_a[elements_in_a - 1] > rod_b[elements_in_b - 1]:
                popped = rod_b.pop()
                rod_a.append(popped)
                print(f'Disk {popped} moved from B to A')
                elements_in_b = len(rod_b) if len(rod_b) != 0 else index_count_b
                elements_in_a = len(rod_a) if len(rod_a) != 0 else index_count_a
                

        if elements_in_c:

            if rod_b[elements_in_b - 1] > rod_c[elements_in_c - 1]:
                popped = rod_c.pop()
                rod_b.append(rod_c.pop())
                print(f'Disk {popped} moved from C to B')
                elements_in_c = len(rod_c) if len(rod_c) != 0 else index_count_c
                elements_in_b = len(rod_b) if len(rod_b) != 0 else index_count_b
                

            elif rod_a[elements_in_a - 1] > rod_c[elements_in_c - 1]:
                popped = rod_c.pop()
                rod_a.append(popped)
                print(f'Disk {popped} moved from C to A')
                elements_in_c = len(rod_c) if len(rod_c) != 0 else index_count_c
                elements_in_a = len(rod_a) if len(rod_a) != 0 else index_count_a
                

        if rod_c == result:
            break

        print(elements_in_a, elements_in_b, elements_in_c)

if __name__ == '__main__':
    tower_of_hanoi(4)
