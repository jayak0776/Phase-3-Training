def generateBinaryString(i,res,n):
    if i==n:
        print(res,end=" ")
        return
    generateBinaryString(i+1,res+'1',n)
    generateBinaryString(i+1,res+'0',n)

generateBinaryString(0,'',2)