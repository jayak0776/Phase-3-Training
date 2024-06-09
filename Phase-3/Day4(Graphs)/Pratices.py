# def changeCountKeys(s):
#     if s=='':
#         return 0
#     else:
#         s=s.lower()
#         c=0
#         for i in range(0,len(s)-1):
#             if s[i]!=s[i+1]:
#                 c+=1
#         return c        

# s="aAwW"
# print(changeCountKeys(s))

def ticket(scr,dest):
    d={
        "EFG":'A',
        "GHI":'A',
        "CDE":'B',
        "IJK":'B',
        "ABC":'C',
        "KLO":'C'
    }
    l=len(scr)
    li=[]
    for i in range(0,l):
        f=scr[i]
        k=dest[i]
        if d[f]!=d[k]:
            if d[f]=='C' or d[k]=='C':
                m=d[f]+'B'+d[k]
                li.append(m)
            else:    
                m=d[f]+d[k]
                li.append(m)
        else:
            li.append(d[f])
                
    return li        
        

src=["ABC","EFG"]
dest=["KLO","ABC"]
print(ticket(src,dest))
