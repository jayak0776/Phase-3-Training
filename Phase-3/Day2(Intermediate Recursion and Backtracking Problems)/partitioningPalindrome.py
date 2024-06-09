class Solution:
    def partition(self,s):
        result=[]
        path=[]
        
        def solveIt(index):
            if index==len(s):
                result.append(path[:])
                return
            
            current=""
            for pos in range(index,len(s)):
                current+=s[pos]
                if current==current[::-1]:
                    path.append(current)
                    solveIt(pos+1)
                    path.pop()
        solveIt(0)
        return result
st="aab"
s=Solution()
print(s.partition(st))             