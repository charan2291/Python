#AIM:a python program to create dictionary with cricket players names and scores in a match.Also we are retrieving runs by entering the player's name.
x={}
print('how many players?',end='')
n=int(input())
for i in range(n):
    print('enter player name:',end='')
    k=input()
    print('enter runs:',end='')
    v=int(input())
    x.update({k:v})
print('\nplayers in this match:')
for pname in x.keys():
    print(pname)
print('enter player name:',end='')
name=input()
runs=x.get(name,-1)
if (runs==1):
    print('player nat found')
else:
    print('{}made runs{}.'.format(name,runs))
"""
INPUT:
how many players?3
enter player name:Sachin
enter runs:77
enter player name:Kohli
enter runs:40
enter player name:Dhoni
enter runs:98
OUTPUT:
players in this match:
Kohli
Dhoni
Sachin
enter player name:Dhoni
Dhonimade runs98.
