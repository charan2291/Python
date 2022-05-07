#AIM:A function to calculate factorial values of numbers.
def fact(n):
    prod=1
    while n>=1:
        prod*=n
        n-=1
    return prod
for I in range(1,11):
    print("Factorial of {}is{}".format(I,fact(I)))
"""
OUTPUT:
Factorial of 1is1
Factorial of 2is2
Factorial of 3is6
Factorial of 4is24
Factorial of 5is120
Factorial of 6is720
Factorial of 7is5040
Factorial of 8is40320
Factorial of 9is362880
Factorial of 10is3628800
