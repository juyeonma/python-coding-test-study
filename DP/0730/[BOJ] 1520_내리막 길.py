# ...bfs아닌가..?...아닌가..

# 찾아보니 dfs + dp를 합쳐서 사용하는 것 같다..
# 참고 : https://studyandwrite.tistory.com/387
# 좀 더 이해필요..
# 이렇게 두 알고리즘을 섞어 쓰는 것은 아직 부족한 것 같다.....
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def dfs(sx, sy):
    # 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
    if sx == m-1 and sy == n-1:
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[sx][sy] != -1:
        return dp[sx][sy]
    
    ways = 0
    for i in range(4):
        nx, ny = sx + dx[i], sy + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[sx][sy] > graph[nx][ny]:
            ways += dfs(nx, ny)
    
    dp[sx][sy] = ways
    return dp[sx][sy]


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx, dy = [1,-1,0,0], [0,0,1,-1]

print(dfs(0,0))


# 그냥 궁금했던 부분..
# 메모이제이션이란?
# 동일한 계산을 반복해야 할 때 이전에 계산했던 값들을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 빠르게 할 수 있는 방법
# 참고 : https://velog.io/@4775614/%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98Memoization%EC%9D%B4%EB%9E%80

