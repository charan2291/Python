#displaying the elements in reverse order
days=['sunday','monday','tuesday','wednesday','thursday']
print('\nIn reverse order:  ')
i=len(days)-1
while i>=0:
    print(days[i])
    i-=1
print('\nIn reverse order: ')
i=-1
while i>=-len(days):
    print(days[i])
    i-=1
"""
OUTPUT:
In reverse order:  
thursday
wednesday
tuesday
monday
sunday

In reverse order: 
thursday
wednesday
tuesday
monday
sunday
