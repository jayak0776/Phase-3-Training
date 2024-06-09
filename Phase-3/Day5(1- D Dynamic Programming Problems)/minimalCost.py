class Solution:
    def minimizeCost(self, height, n, k):
        # def solveIt(index):
        #     if index==n-1:
        #         return 0
            
        #     result=100000000
        #     for i in range(1,k+1):
        #         nextIndex=index+i
        #         if nextIndex>=n:
        #             break
        #         currentCost=abs(height[index]-height[nextIndex])+sloveIt(nextIndex)
        #         result=min(result,currentIndex)
        #     return result  
        
        # def sloveItMemoization(index):
        #     cache=[-1]*n
        #     if index==n-1:
        #         return 0
        #     if cache[index]==-1:
        #         return cache[-1]
            
        #     result=100000000
        #     for i in range(1,k+1):
        #         nextIndex=index+i
        #         if nextIndex>=n:
        #             break
        #         currentCost=abs(height[index]-height[nextIndex])+sloveIt(nextIndex)
        #         result=min(result,currentIndex)
        #         cache[index]=result
        #     return result
        
        def solveItUsingTabulation(index):
            cache=[-1]*n
            cache[n - 1] = 0 
            for index in range(n - 2, -1, -1):
                result = 100000000 
                for i in range(1, k + 1):
                    nextIndex = index + i 
                    if nextIndex >= n:
                        break 
                    currCost = abs(height[index] - height[nextIndex]) + cache[nextIndex]
                    result = min(result, currCost)
                cache[index] = result
            return cache[0]
            
        return solveItUsingTabulation(0) 
 
s=Solution()
print(s.minimizeCost([10, 30, 40, 50, 20],5,3))    