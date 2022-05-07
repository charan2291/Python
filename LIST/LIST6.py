#to display how many times an element occured in the list
x=[]
n=int(input('how many times?'))
for i in range(n):
    print('enter element:',end='')
    x.append(int(input()))
print('the lidt is:',x)
y=int(input('enter element to count:'))
c=0
for i in x:
    if (y==i):c+=1
print('{} is found {} times.'.format(y,c))
"""
OUTPUT:
how many times?5
enter element:40
enter element:20
enter element:30
enter element:40
enter element:50
the lidt is: [40, 20, 30, 40, 50]
enter element to count:40
40 is found 2 times.
