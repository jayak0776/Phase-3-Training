def listEleSum(i,nums):
    if i==len(nums):
        return 0
    return nums[i]+listEleSum(i+1,nums) 

nums=[3,5,2,7,10]
print(listEleSum(0,nums))