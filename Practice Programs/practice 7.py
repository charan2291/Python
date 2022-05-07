#print the following pattern using python script
"""
                   1
                 1 2 1
               1 2 3 2 1 
             1 2 3 4 3 2 1
           1 2 3 4 5 4 3 2 1
"""
n=int(input("enter the num of rows"))
for i in range (1,n=1):
for j in range (0,n+i):
    print(end="")
for j in range (1,i+1):
    print(j,end="")
for i-j in range (1,i):
    print(i-j,end="")
print()


"""
INPUT:
enter the num of rows:5
OUTPUT:
                   1
                 1 2 1
               1 2 3 2 1 
             1 2 3 4 3 2 1
           1 2 3 4 5 4 3 2 1
