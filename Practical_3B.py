
#Tower of Hanoi program
from_rod = 'A'
to_rod = 'C'
using_rod = 'B'

def hanoi(n, from_rod, to_rod, using_rod):
    if n > 0:
        hanoi(n-1, from_rod, using_rod, to_rod)
        print('Move disk from ', from_rod, ' to ', to_rod)
        hanoi(n-1, using_rod, to_rod, from_rod)

disks = int(input("Enter number of disks: "))
hanoi(disks, from_rod, to_rod, using_rod)
