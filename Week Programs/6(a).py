#AIM:Write a python script to read N student details like name,rollnumber,branch and age.Sort the student details based on their names and display.
student_details=[]
n=int(input("enter the no of student details you are entering: "))
for i in range(0,n):
    student_details.append([])
    for j in range(0,1):
        student_details[i].append(input("enter the name of the student:"))
        student_details[i].append(input("enter the roll no of the student:"))
        student_details[i].append(input("enter the branch of the student:"))
        student_details[i].append(input("enter the age of the student:"))
print(student_details)
print(sorted(student_details))
"""
INPUT:
enter the no of student details you are entering: 3
enter the name of the student:P CHARAN REDDY
enter the roll no of the student:29
enter the branch of the student:CSSE
enter the age of the student:18
enter the name of the student:M SRI HARSHINI
enter the roll no of the student:26
enter the branch of the student:ECE
enter the age of the student:18
enter the name of the student:L CHANDANA
enter the roll no of the student:5
enter the branch of the student:ECE
enter the age of the student:18
OUTPUT:
[['P CHARAN REDDY', '29', 'CSSE', '18'], ['M SRI HARSHINI', '26', 'ECE', '18'], ['L CHANDANA', '5', 'ECE', '18']]
[['L CHANDANA', '5', 'ECE', '18'], ['M SRI HARSHINI', '26', 'ECE', '18'], ['P CHARAN REDDY', '29', 'CSSE', '18']]

