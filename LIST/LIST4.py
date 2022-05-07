#finding biggest and smallest numbers in a list of numbers
x=[]
print('how many elements?',end='')
n=int(input())
for i in range(n):
    print('enter element:',end='')
    x.append(int(input()))             
print('the list is: ',x)
big=x[0]
small=x[0]
for i in range(1,n):
    if x[i]>big: big=x[i]
    if x[i]<small: small=x[i]
print('maximum is:',big)
print('minimum is:',small)
"""
OUTPUT:
how many elements?5
enter element:20
enter element:10
enter element:5
enter element:20
enter element:15
the list is:  [20, 10, 5, 20, 15]
maximum is: 20
minimum is: 5
    
