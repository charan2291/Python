#to display to retrieve elements from a matrix and dispaly them
mat=[[1,2,3],[4,5,6],[7,8,9]]
print('display the list as it is:')
print(mat)
print('display row by row:')
for r in mat:
    print(r)
print('display each clouomn in row0:')
for c in mat[0]:
    print('%d'%c,end='')
print()
print('display each coluomn in row1:')
for c in mat[1]:
    print('%d'%c,end='')
print()
print('display each column in row2:')
for c in mat[2]:
    print('%d'%c,end='')
print()
print('display all elements using for:')
for r in mat:
    for c in r:
        print(c,end='')
    print()
print('diaplay all elements using for:')
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print('%d'%mat[i][j],end='')
    print()
"""
OUPUT:
display the list as it is:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
display row by row:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
display each clouomn in row0:
123
display each coluomn in row1:
456
display each column in row2:
789
display all elements using for:
123
456
789
diaplay all elements using for:
123
456
789
    
