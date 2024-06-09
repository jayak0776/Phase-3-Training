def maxEle(i,nums):
    if i==len(nums):
        return i
    return max(nums[i],maxEle(i+1,nums))

nums=[3,5,2,7,10]
print(maxEle(0,nums))

def minEle(i,nums):
    if i==len(nums):
        return i
    return min(nums[i],minEle(i+1,nums))

nums=[3,5,2,7,10]
print(minEle(0,nums))