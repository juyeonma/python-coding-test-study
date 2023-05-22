# 1. 테이블 정의
# d[i]= i를 1로 만들기 위해 필요한 연산 사용 횟수의 최솟값

# 2. 점화식
# d[12]=?
# 3으로 나누거나(d[12]=d[4]+1) 2로나누거나(d[12]=d[6]+1) 1을 빼거나(d[12]=d[11]+1)
# d[12]= min(d[4]+1,d[6]+1,d[11]+1)
# d[k] = 3으로 나누어지면 d[k/3]+1 2나눠지면 d[k/2]+1 1을 빼면 d[k-1]+1 중 최솟값

# 3. 초기값 정의
# d[1]=0

#bfs로도 가능해서 bfs로도 풀어봤는데 bfs가 시간이 훨씬 절약됐다
#dp는 1부터 n까지 모두 채워넣는다면 bfs는 모든 경우를 탐색한 것이 아니라 2배 3배 +1 만 탐색하거나 /2 /3 -1 만 탐색해서 시간이 절약되었다.
#하지만 bfs로 풀어도 시간이 오래 걸린 경우가 있었는데 마지막 답의 배열요소를 구할 때 바로 while문을 탈출시켜주지 않는 경우 오래 걸렸다.
# 모든 경우가 다 들어갈 수있다고 했을 때 x3씩 늘어나서 마지막 요소에서 바로 탈출하는 것이 아니라 q에 값이 없을때까지 돈다면 오래걸리는 것 같다.

# 메모리 39068KB 시간 536ms
n = int(input())    
d= [0]*(n+1)    #값을 하위값부터 차례대로 저장하기 위한 배열

for i in range(2,n+1): 
    d[i]=d[i-1]+1   # 1로 빼는 경우는 무조건 가능하니까 먼저 값을 d[i]에 넣어준다
    if i%3==0:  # 3으로 나누어떨어지면 값 비교
        d[i]=min(d[i],d[i//3]+1)
    if i%2==0:  # 2로 나누어떨어지면 값 비교
        d[i]=min(d[i],d[i//2]+1)
print(d[n]) #최종 값 출력


# # 메모리 41264KB 걸린시간 72ms
# from collections import deque

# x= int(input())
# vis=[0]*(x+1)

# q = deque([x])
# while q:
#     cur_x=q.popleft()
#     for i in range(2,4):
#         if not cur_x%i and not vis[cur_x//i]:
#             vis[cur_x//i]=vis[cur_x]+1
#             q.append(cur_x//i)
#     if not vis[cur_x-1]:
#         vis[cur_x-1]=vis[cur_x]+1
#         q.append(cur_x-1)
#     if cur_x<=3:
#         break

# print(vis[1])

#메모리 40092KB 시간 76ms
# from collections import deque
# import sys
# n = int(input())
# if n==1:
#     print(0)
#     sys.exit()
# vis=[0]*(n+1)
# q=deque([n])
# while q:
#     x = q.popleft()
#     if not vis[x-1]:
#         vis[x-1]=vis[x]+1
#         q.append(x-1)
#     for i in [2,3]:
#         if x%i==0:
#             nx=x//i
#             if not vis[nx]:
#                 vis[nx]=vis[x]+1
#                 q.append(x//i)
#     if vis[1]:
#         print(vis[1])
#         break

#메모리 71844KB 시간 740ms
# from collections import deque
# n = int(input())
# vis=[0]*(n+1)
# q=deque([n])
# while q:
#     x = q.popleft()
#     if not vis[x-1] and x-1>=1:
#         vis[x-1]=vis[x]+1
#         q.append(x-1)
#     for i in [2,3]:
#         if x%i==0:
#             nx=x//i
#             if not vis[nx] and nx>=1:
#                 vis[nx]=vis[x]+1
#                 q.append(x//i)
# print(vis[1])

# 메모리 47160KB 시간 956ms

# from collections import deque
# n = int(input())
# vis = [0]*(n+1)

# q=deque([1])
# while q:
#     x=q.popleft()
#     for i in [2,3]:
#         nx = x*i
#         if nx>n or vis[nx]:
#             continue
#         if not vis[nx]:
#             vis[nx]=vis[x]+1
#         q.append(nx)
#     if x+1>n or vis[x+1]:
#         continue
#     if not vis[x+1]:
#         vis[x+1]=vis[x]+1
#     q.append(x+1)

# print(vis[n])