#AIM:python program to retrieve keys,values,(key,values) pairs and sum of values.
dict={'A':10,'B':20,'C':35,'Anil':50}
print(dict)
print('keys in dict=',dict.keys())
print('values in dict=',dict.values())
print('items in dict=',dict.items())
s=sum(dict.values())
print('sum of values in the dictionary:',s)
"""
OUTPUT:
{'Anil': 50, 'A': 10, 'C': 35, 'B': 20}
keys in dict= dict_keys(['Anil', 'A', 'C', 'B'])
values in dict= dict_values([50, 10, 35, 20])
items in dict= dict_items([('Anil', 50), ('A', 10), ('C', 35), ('B', 20)])
sum of values in the dictionary: 115
