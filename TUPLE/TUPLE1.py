#a python program to accept elements in the form of a tuple and display their sum and average
num=eval(input("enter element in ():"))
sum=0
n=len(num)
for i in range(n):
    sum+=num[i]
print('sum of numbers:',sum)
print('average of numbers:',sum/n)
"""
INPUT:
enter element in ():(1,2,3,4,5)
OUTPUT:
sum of numbers: 15
average of numbers: 3.0
