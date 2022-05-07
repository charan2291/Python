str=input('enter elements separated by commas:').split(',')
list=[int(num) for num in str]
tup=tuple(list)
print('the tuple is:',tup)
ele=int(input('enter an element to search:'))
try:
    pos=tup.index(ele)
    print('Element position no:',pos+1)
exceptvalueError:
    print('Element not found in tuple')
"""
INPUT:
enter elements separated by commas:10,20,30,40,50,60
OUTPUT:
the tuple is:(10,20,30,40,50,60)
Element position to search:20
Element position no:2
