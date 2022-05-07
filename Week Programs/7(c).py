#AIM:Write a python function primesqaure(I) thet takes a nonempty list of integers and returns True if the elements of I alternate between perfect squares and prime numbers,and returns False otherwise.Note that the elements sequence of squares and primes may begin with a square or with a prime.
import math
def prime_checker(num):
    flag=True
    if num==2:
        return True
    elif num<2:
        return False
    else:
        for i in range(2,int(num/2)):
            if num%i==0:
                flag=False
            break
    return flag
def is_square(integer):
    if integer==0:
        return False
    root=math.sqrt(integer)
    if int(root+0.5)**2==integer:
        return True
    return False
def primesquare(list_nums):
    if len(list_nums)==0:
        return False
    if len(list_nums)==1:
        if (is_square(list_nums[0]) or prime_checker(list_nums[0])):
            return True
        else:
            return False
    else:
        flag=True
        if is_square(list_nums[0]):
            check_for="prime"
        elif prime_checker (list_nums[1]):
            check_for="square"
        else:
            return False
    for i in range(1,len(list_nums)):
        if(check_for=='prime' and prime_checker(list_nums[i])):
                check_for='square'
        elif(check_for=='square' and is_square(list_nums[i])):
                check_for='prime'
        else:
            flag=False
            break
        if flag:
            return True
        else:
            return False
print(primesquare([4]))
print(primesquare([4,5,16,101,64]))
print(primesquare([5,16,101,36,27]))
"""
OUTPUT:
True
True
False




                    
                
                    

                
        
