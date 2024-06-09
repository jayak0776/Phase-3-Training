def findVowels(i,l,s,res):
    vowels="aeiouAEIOU"
    if i==l:
        return res
    res=findVowels(i+1,l,s,res)
    if s[i] in vowels:
        res+=1
    return res

s="jayakumar"
print(findVowels(0,len(s),s,0))  

def findVowels(i, l, s):
    vowels = "aeiouAEIOU"
    if i >= l:
        return 0
    if s[i] in vowels:
        return 1 + findVowels(i + 1, l, s)
    else:
        return findVowels(i + 1, l, s)

s = "jayakumar"
print("Count is:", findVowels(0, len(s), s))


  