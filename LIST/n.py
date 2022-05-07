#to display to create a list with employees data.
emp=[]
n=int(input('how many employees?'))
for i in range(n):
    print('enter id:',end='')
    emp.append(int(input()))
    print('enter name:',end='')
    emp.append(input())
    print('enter salary:',end='')
    emp.append(float(input()))
print('the list created with employees data.')
id=int(input('enter employee id:'))
for i in range(len(emp)):
    print('id={:d}','name={:s}','salary={:.2f}'.format(emp[i],emp[i+1],emp[i+2]))
    break
"""
OUTPUT:
how many employees?3
enter id:10
enter name:P CHARAN REDDY
enter salary:9000.50
enter id:11
enter name:K SAI PURANDHAR
enter salary:9000.00
enter id:12
enter name:A HARSHA
enter salary:9000.75
the list created with employees data.
enter employee id:10
id={:d} name={:s} salary=10.00
