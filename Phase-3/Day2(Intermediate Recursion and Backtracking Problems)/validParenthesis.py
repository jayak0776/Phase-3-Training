def validParenthesisComb(n,res,l,open,close):
    if close>open:
        return
    if open>(n//2) or close>(n//2):
        return
    if len(res)==n:
        l.append(res)
        return 
    validParenthesisComb(n,res+'(',l,open+1,close)
    validParenthesisComb(n,res+')',l,open,close+1)
    return l     
print(validParenthesisComb(4,'',[],0,0))