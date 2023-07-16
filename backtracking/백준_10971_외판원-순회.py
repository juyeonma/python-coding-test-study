'''
# 백준_10971_외판원 순회. 실버 2. 풀이: 23.07.12

# How to
- 문제의 조건:
    - W[i][j] 는 W[j][i]와 다를 수 있다. 
    - 길이 없을 수도 있다
    - 한 번 갔던 도시로는 다시 갈 수 없다. 
    - 항상 순회할 수 있는 경우만 입력으로 주어진다.

- DFS
- 항상 순회하므로, 0번 도시에서 출발
- 매번 다른 도시로 이동 가능한지 체크하고, 방문
- 마지막 도시라면, 출발 도시로 이동 가능할 경우 비용 갱신

## 반례
1 2 3
1 -> 2 -> 3 -> 1 return
1 -> 3 -> 1 return

3
0 10 100
2 0 200
3 30 0
정답: 132

# Review
- 풀이 시간: 30분
- 왜 이렇게 느리지..?
'''

# Code
# 1. DFS: 성공
## 메모리: 31256 KB, 시간: 508 ms
import sys
input = sys.stdin.readline

# 도시의 수 n, 도시간 비용 cost
n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
answer = int(1e9)

def dfs(now, cost, depth):
    global answer

    # 방문 처리
    visited[now] = True
    
    # 마지막 도시이고 출발 도시로 이동 가능하다면, 비용 갱신
    if depth == n-1 and city[now][0]:
        answer = min(answer, cost+city[now][0])
        return

    # 새로 방문하는 도시라면, 이동
    for next in range(n):
        # 다음 도시로 이동 가능하면,
        if not visited[next] and city[now][next]:
            dfs(next, cost+city[now][next], depth+1)
            visited[next] = False
        
dfs(0, 0, 0)
print(answer)
