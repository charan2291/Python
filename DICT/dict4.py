#AIM:a python program to sort the elements of a dictionary based on a key or value.
colors={10:'red',35:'green',15:'blue',25:'white'}
c1=sorted(colors.items(),key=lambda t:t[0])
print(c1)
c2=sorted(colors.items(),key=lambda t:t[1])
print(c2)
"""
OUTPUT:
[(10, 'red'), (15, 'blue'), (25, 'white'), (35, 'green')]
[(15, 'blue'), (35, 'green'), (10, 'red'), (25, 'white')]
