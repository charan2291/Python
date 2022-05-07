#sorting a list using bubble sort techique
x=[]
print('how many elements?',end='')
n=int(input())
for i in range(n):
    print('enter element:',end='')
    x.append(int(input()))
print('original list:',x)
flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if x[j]>x[j+1]:
             t=x[j]
             x[j+1]=t
             flag=True
    if flag==False:
        break
    else:
        flag=False
print('sorted list:',x)
"""
OUTPUT:
how many elements?5
enter element:1
enter element:5
enter element:4
enter element:3
enter element:2
original list: [1, 5, 4, 3, 2]
sorted list: [1, 5, 5, 5, 5]
             
