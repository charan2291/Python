#AIM:Write a python script to delete strings from a list of strings.
X=input("enter:" ).split(",")
Y=X.copy()
n=len(X)
while len(set(X))!=n:
    for i in range(n):
        for j in range(i+1,n):
            if X[i]==X[j]:
                del Y[j]
                X=Y.copy()
                n=len(Y)
                break
        if n==n-1:
            break
print(X)
"""
INPUT:
enter:CHARAN,HARSHINI,THARUN,KSP,HARSHA,NAVYA,CHANDANA,THARUN,HARSHA,KSP
OUTPUT:
['CHARAN', 'HARSHINI', 'THARUN', 'KSP', 'HARSHA', 'NAVYA', 'CHANDANA']
    
