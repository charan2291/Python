#AIM:Design a function that cann perform sum of two or three or four numbers.
def mysum(*arg):
    sum1=0
    for i in arg:
        sum1=sum1+i
    return sum1
print("sum1",mysum(1,2))
print("sum2",mysum(1,2,3))
print("sum3",mysum(1,2,3,4))
"""
OUTPUT:
sum1 3
sum2 6
sum3 10


