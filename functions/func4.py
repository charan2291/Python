#AIM:A function to check if a given number is prime or not.
def prime(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
        if x==1:
            print(num,"is not prime")
        else:
            print(num,"is prime")
    return x
num=int(input("Enter a number"))
result=prime(num)
"""
OUPUT:
Enter a number45
45 is not prime
