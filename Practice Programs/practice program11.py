#program to display fibonacci series
n=int(input('how many fibonacci?'))
f1=0
f2=1
c=3
if n==1:
    print(f1)
elif n==2:
    print(f1,'\n',f2,sep='')
else:
    print(f1,'\n',f2,sep='')
    while c<n:
        f=f1+f2
        print(f)
        f1,f2=f2,f
        c+=1
"""
OUTPUT:
how many fibonacci?10
0
1
1
2
3
5
8
13
21
    
