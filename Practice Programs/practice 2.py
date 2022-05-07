"""AIM:write a python script to evaluate following expressions by considering necessary inputs.
1.a*x**2+b*x++c      2.a*x**5+b*x**3+c
3.(a*x+b)/(a*x-b)    4.x-a/b+c
"""
a=int(input("enter the integer value of a"))
b=int(input("enter the integer value of b"))
c=int(input("enter the integer value of c"))
x=int(input("enter the integer value of x"))
exp1=a*x**2+b*x+c
exp2=a*x**5+b*x**3+c
exp3=(a*x+b)/(a*x-b)
exp4=x-a/b+c
print("value of expression 1:",exp1)
print("value of expression 2:",exp2)
print("value of expression 3:",exp3)
print("value of expression 4:",exp4)


"""
INPUT:
enter the integer value of a10
enter the integer value of b15
enter the integer value of c20
enter the integer value of x25
OUTPUT:
value of expression 1: 240645
value of expression 2: 97890645
value of expression 3: 1.1276599574468085
value of expression 4: 44.333333333333333

