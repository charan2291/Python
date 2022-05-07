#to display to find common elements in two lists.
scholar1=['vinay','krishna','saraswathi','govind']
scholar2=['rosy','govind','tanushri','vinay','vishal']
s1=set(scholar1)
s2=set(scholar2)
s3=s1.intersection(s2)
common=list(s3)
print(common)
"""
OUTPUT:
['vinay', 'govind']
