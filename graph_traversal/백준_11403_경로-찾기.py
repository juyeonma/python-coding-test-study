'''
# 백준_11403_경로-찾기. 실버 1. 풀이: 23.09.15 -> 실패

# How to

## 반례

# Review
- 풀이 시간:
- 구상하는게 어려웠다. 실버 1인데도..
- 간신히 DFS로 했지만, 시간초과. BFS로 해야하는걸까?
'''

# Code
# 1. DFS: 시간초과 실패
## 메모리:  KB, 시간:  ms
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(i, road):
    for j in range(n):
        # 연결된다면
        if arr[i][j]:
            # 이전 경로와도 연결하고
            for before in road:
                arr[before][j] = 1
            # 경로에 추가하며 dfs 재귀로 들어간다.
            if i not in road:
                dfs(j, road|{i})

for i in range(n):
    dfs(i, set())
    
for i in arr:
    print(*i)