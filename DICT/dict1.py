#AIM:wite  python program to count the number of characters in the string and store them in dictionary data sturcture.
word=input("enter a word")
letterdict={}
for letter in word:
    letterdict[letter]=0
for letter in word:
    letterdict[letter]+=1
print(letterdict)
"""
INPUT:
enter a wordcharan
OUTPUT:
{'c': 1, 'h': 1, 'r': 1, 'n': 1, 'a': 2}
