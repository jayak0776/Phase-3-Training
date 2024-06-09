def evenNums(i,n):
    if i>n:
        return
    if i%2==0:
        print(i,end=" ")
    evenNums(i+1,n)        
evenNums(0,5)
print()
def oddNums(i,n):
    if i>n:
        return
    if i%2!=0:
        print(i,end=" ")
    oddNums(i+1,n)        
oddNums(0,5)