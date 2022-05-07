#AIM:Write a python script to read N number of student details into nested list and convert that as a nested dictionary.
list=[]
k=("stutent name","roll no","branch","age")
n=int(input("enter number of students:"))
for i in range(n):
    v=[]
    a=input("enter student:")
    v.append(a)
    b=int(input("enter roll no of the student:"))
    v.append(b)
    c=input("enter the branch of the student:")
    v.append(c)
    d=int(input("enter the age of the student:"))
    v.append(d)
    list.append(v)
    d={}
    for j in range(len(list)):
        d[j]=dict(zip(k,list[j]))
print("The nested dictionary is")
print(d)
"""
OUTPUT:
enter number of students:3
enter student:P CHARAN REDDY
enter roll no of the student:29
enter the branch of the student:CSSE
enter the age of the student:18
enter student:M SRI HARSHINI
enter roll no of the student:26
enter the branch of the student:ECE
enter the age of the student:18
enter student:L CHANDANA
enter roll no of the student:5
enter the branch of the student:ECE
enter the age of the student:18
The nested dictionary is
{0: {'age': 18, 'branch': 'CSSE', 'roll no': 29, 'stutent name': 'P CHARAN REDDY'},
1: {'age': 18, 'branch': 'ECE', 'roll no': 26, 'stutent name': 'M SRI HARSHINI'},
2: {'age': 18, 'branch': 'ECE', 'roll no': 5, 'stutent name': 'L CHANDANA'}}


