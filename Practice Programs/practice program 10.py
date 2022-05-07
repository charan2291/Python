#program to print prime numbers upto a given number
max=int(input("upto what number?"))
for num in range(2,max+i):
    for i in range(2,num):
        if(num%i)==0:
            break
        else:
            print(num)
"""
OUTPUT:
upto what number?
2
3
5
7
11
13
17
19
23
29
