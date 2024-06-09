def divisibleByN(i,nums,n,k,res):
    if i==n:
        return 0
    res=divisibleByN(i+1,nums,n,k,res)
    if nums[i]%k==0:
        res+=nums[i]
    return res    
    
nums=[5,3,10,4,15,20]        
print(divisibleByN(0,nums,len(nums),5,0))
        