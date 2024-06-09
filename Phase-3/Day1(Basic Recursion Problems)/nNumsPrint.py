# 1 TO N Numbers
def nNumsPrint(i,n):
    if i==n+1:
        return 
    print(i,end=" ")
    nNumsPrint(i+1,n)
nNumsPrint(1,5)
print()

def nTo1NumsPrint(n):
    if n==0:
        return 
    print(n,end=" ")
    nTo1NumsPrint(n-1)
nTo1NumsPrint(5)

