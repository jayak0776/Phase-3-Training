store={}
store["1"]=""
store["2"]="abc"
store["3"]="def"
store["4"]="ghi"
store["5"]="jkl"
store["6"]="mno"
store["7"]="pqrs"
store["8"]="tuv"
store["9"]="wxyz"

class Solution:
    def lettersCombination(self,digits):
        result=[]
        if len(digits)==0:
            return result
        curResult=[]
        
        def solveIt(index):
            if index==len(digits):
                result.append("".join(curResult))
                return
            
            char=digits[index]
            for val in store[char]:
                curResult.append(val)
                solveIt(index+1)
                curResult.pop()
        solveIt(0)
        return result

digits=input()
s=Solution()
print(s.lettersCombination(digits))               