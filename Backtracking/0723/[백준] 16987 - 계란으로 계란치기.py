첫번째 풀이로 풀고나서 다시 보니 뭔가 이상하다 왜 통과가 되는지 모르겠다.
풀 때는 "됐군" 하고 풀었는데..
너무 백트래킹의 기본틀에 갖혀서 풀려고 했던 것 같고 여러 조건을 다루는 건 처음이라 어려웠던 것 같다
for문 안에서 조건을 세우려고 했었는데 이런 생각이 경직된 사고를 하게 만든 것 같다

두번째 풀이는 주연님 풀이를 참고하였다. 

# n = int(input())
# eggs = [list(map(int,input().split())) for _ in range(n)]
# max_num = 0
# vis = [0]*n

# def dfs(k):
#     global max_num
#     if k==n:
#         max_num=max(max_num,vis.count(1))
#         return
    
#     if vis[k]:
#         dfs(k+1)
#         return

#     for i in range(n):
#         if not vis[i] and i!=k:
#             if eggs[k][0]<=eggs[i][1]:
#                 vis[k]=1
#                 if eggs[i][0]<=eggs[k][1]:
#                     vis[i]=1
#                     dfs(k+1)
#                     vis[i]=0
#                 else:
#                     eggs[i][0]-=eggs[k][1]
#                     dfs(k+1)
#                     eggs[i][0]+=eggs[k][1]
#                 vis[k]=0
#             else:
#                 eggs[k][0]-=eggs[i][1]
#                 if eggs[i][0]<=eggs[k][1]:
#                     vis[i]=1
#                     dfs(k+1)
#                     vis[i]=0
#                 else:
#                     eggs[i][0]-=eggs[k][1]
#                     dfs(k+1)
#                     eggs[i][0]+=eggs[k][1]
#                 eggs[k][0]+=eggs[i][1]

#     if k==n-1:
#         max_num=max(max_num,vis.count(1))
#         return
# dfs(0)
# print(max_num)

n = int(input())
eggs = [list(map(int,input().split())) for _ in range(n)]
max_num = 0
def dfs(k,count):
    global max_num
    if k==n:
        max_num = max(max_num,count)
        return
    
    if count==n-1:
        max_num = max(max_num,n-1)
        return
    
    if eggs[k][0]<=0:
        dfs(k+1,count)
        return

    for i in range(n):
        if eggs[i][0]>0 and i!=k:
            eggs[k][0]-=eggs[i][1]
            eggs[i][0]-=eggs[k][1]
            temp = 0
            if eggs[k][0]<=0:
                temp+=1
            if eggs[i][0]<=0:
                temp+=1
            dfs(k+1,count+temp)
            eggs[k][0]+=eggs[i][1]
            eggs[i][0]+=eggs[k][1]

dfs(0,0)
print(max_num)