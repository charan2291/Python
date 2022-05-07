def mysum(*num):
    sum1=0
    for i in num:
        sum1=sum1+i
    return sum1
print("mysum",mysum(1,2,4,5,7))
print("mysum",mysum(1,2,3,4,5))
print("mysum",mysum(1,2))
"""
OUTPUT:
mysum 19
mysum 15
mysum 3

