#AIM:write a python code to read four integer values seperated with commas and display the sum of those four numbers.
num=input("enter 4 numbers seperated with comma")
var=num.split(",")
print("list is:",var)
sum=0
for items in var:
    sum=sum+int(items)
    print("sum of nums in list:",sum)


"""
INPUT:
enter 4 numbers seperated with comma25,30,35,40
OUTPUT:
list is: ['25', '30', '35', '40']
sum of nums in list: 130

