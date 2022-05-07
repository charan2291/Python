#python's listr methods
num=[10,20,30,40,50]
n=len(num)
print('no.of elements in num: ',n)
num.append(60)
print('num after appending 60: ',num)
num.insert(0,5)
print('num after inserting 5 at 0th position: ',num)
num1=num.copy()
print('newly crweated list num1: ',num1)
num.extend(num1)
print('num after appending num1: ',num)
n=num.count(50)
print('no.of times 50 found in list num: ',n)
num.remove(50)
print('num after removing 50: ',num)
num.pop()
print('num after removing ending element: ',num)
num.sort()
print('num after sorting: ',num)
num.reverse()
print('num after reversing: ',num)
num.clear()
print('num after removing all elements: ',num)
"""OUTPUT:
no.of elements in num:  5
num after appending 60:  [10, 20, 30, 40, 50, 60]
num after inserting 5 at 0th position:  [5, 10, 20, 30, 40, 50, 60]
newly crweated list num1:  [5, 10, 20, 30, 40, 50, 60]
num after appending num1:  [5, 10, 20, 30, 40, 50, 60, 5, 10, 20, 30, 40, 50, 60]
no.of times 50 found in list num:  2
num after removing 50:  [5, 10, 20, 30, 40, 60, 5, 10, 20, 30, 40, 50, 60]
num after removing ending element:  [5, 10, 20, 30, 40, 60, 5, 10, 20, 30, 40, 50]
num after sorting:  [5, 5, 10, 10, 20, 20, 30, 30, 40, 40, 50, 60]
num after reversing:  [60, 50, 40, 40, 30, 30, 20, 20, 10, 10, 5, 5]
num after removing all elements:  []

      
