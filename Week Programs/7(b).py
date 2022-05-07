#AIM:Write a python script implement Towers of Hanoi problem.
def towers(n,a,c,b):
    if n==1:
        print('Move disk %i from pole %s to %s'%(n,a,c))
    else:
        towers(n-1,a,b,c)
        print('Move disk %i from pole %s to %s'%(n,a,c))
        towers(n-1,b,c,a)
n=int(input('Enter number of disks:'))
towers(n,'A','B','C')
"""
INPUT:
Enter number of disks:4
OUTPUT:
Move disk 1 from pole A to C
Move disk 2 from pole A to B
Move disk 1 from pole C to B
Move disk 3 from pole A to C
Move disk 1 from pole B to A
Move disk 2 from pole B to C
Move disk 1 from pole A to C
Move disk 4 from pole A to B
Move disk 1 from pole C to B
Move disk 2 from pole C to A
Move disk 1 from pole B to A
Move disk 3 from pole C to B
Move disk 1 from pole A to C
Move disk 2 from pole A to B
Move disk 1 from pole C to B
        
