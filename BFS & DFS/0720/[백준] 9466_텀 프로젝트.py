# 코드 1이 시간초과인 이유는 n이 십만인데 어떤 인덱스에서 완벽한 사이클이 안이루어진다고해서 그냥 넘어가면
# 시간복잡도가 너무 커진다
# 그렇기 때문에 완벽한 사이클이 아니더라도 사이클이 그려지는 만큼은 방문처리를 해줘야한다.
# 그리고 사이클이 안되는 학생들을 굳이 다시 방문할 필요가 없기때문에 이 학생들도 방문했다는 처리를 해준다
# 먼저 dfs가 돌때 -1로 초기화 시켜주고 사이클이되는 학생들만 1로 다시 초기화 해준다


코드1 : 시간초과
import sys

t = int(input())
def dfs(i,k):
    c=0
    while not (i==k and c):
        if k in check:
            return False
        check.add(k)
        k=students[k]
        c+=1
    return True

for _ in range(t):
    n = int(input())
    students = [0]+list(map(int,sys.stdin.readline().split()))
    vis = [0]*(n+1)
    for i in range(1,n+1):
        if not vis[i]:
            check = set()
            if dfs(i,i):
                for j in check:
                    vis[j]=1
    print(vis.count(0)-1)

코드2: 통과
import sys
sys.setrecursionlimit(10**6)
t = int(input())

def dfs(i):
    while i not in temp_vis:
        if vis[i]: # 이미 사이클이 안되는 학생들로 연결되는 경우
            return False
        vis[i]=-1 # 일단 먼저 모두 -1로 갱신
        temp_vis.add(i)
        i = students[i]
    return i # temp_vis에 있따는건 사이클이 된다는 의미이므로 마지막 들어온 것을 리턴
        
def check(i,k): # 마지막부터 반대로 돌아가면서 1로 방문처리
    if not vis[k]==1:
        vis[k]=1
        check(i,students[k])

for _ in range(t):
    n = int(input())
    students = [0]+list(map(int,sys.stdin.readline().split()))
    vis = [0]*(n+1)
    for i in range(1,n+1):
        if not vis[i]: # 방문 처리가 안 된 곳만
            temp_vis = set()
            temp = dfs(i)
            if temp: 
                check(temp,temp)

    print(vis.count(-1))

#걸린시간 1시간 27분
#메모리 : 65428kb 시간 : 3072ms


# 나중에 다시볼 다른 사람 코드
# import sys 
# sys.setrecursionlimit(10**6)

# t = int(input())

# def dfs(i):
#     global count
#     vis[i]=1
#     cycle_list.append(i)
#     if vis[stu[i]]:
#         if stu[i] in cycle_list:
#             count -= len(cycle_list[cycle_list.index(stu[i]):])
#         return
#     else:
#         dfs(stu[i])

# for _ in range(t):
#     n = int(input())
#     stu = [0]+list(map(int,sys.stdin.readline().split()))
#     vis = [0]*(n+1)
#     count=n
#     for i in range(1,n+1):
#         if not vis[i]:
#             cycle_list = []
#             dfs(i)
    
#     print(count)
