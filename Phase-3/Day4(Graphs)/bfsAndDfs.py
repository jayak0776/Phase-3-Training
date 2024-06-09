graph={
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','E'],
    'D':['B','E'],
    'E':['C','D']
}

# def bfs(start,graph):
#     visit=[start]
#     q=[start]
    
#     while len(q)!=0:
#         ele=q.pop()
#         for i in graph[ele]:
#             if i not in visit:
#                 q.append(i)
#                 visit.append(i)     
                          
#     # for key,value in graph.items():
#     #     if key is not q:
#     #         for i in value:
#     #             if i not in vist:
#     #                 q.append(i)
#     #                 vist.append(i)
#     #     else:
#     #         q.pop(key)  
#     return visit     
# print(bfs('B',graph))

def dfs(start,graph,visited=None):
    if visited==None:
        visited=[]
    visited.append(start)
    for ne in graph[start]:
        if ne not in visited:
            dfs(ne,graph,visited)
    return visited 
print(dfs('E',graph))       