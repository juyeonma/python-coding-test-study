'''
# 백준_18430_무기-공학. 골드 4. 풀이: 23.07.09 -> 실패

# How to
- 범위가 작다: (1 ≤ N, M ≤ 5) 
- DFS
- 매번 4가지 모양에 대해 방문 처리 후 그 다음 방문 or 방문 안하고 그 다음 방문

## 예제
2 3
7 5 4
3 2 9
정답: 46

## 반례
2 5
100 1 1 1 1
1 1 100 1 100
정답: 606

# Review
- 날개를 방문 처리한 이후, 다음 좌표를 어떻게 설정해야할지 모르겠다.
- 모든 좌표를 탐색하면 종료해야하는데, 어떻게 종료 조건을 설정해야할지 모르겠다.
- 무엇보다.. DFS와 재귀에 대해서 더 공부해야겠다..
'''

# 
import sys
n, m = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(n)]
    
# dx = [[0, 1], [0, 1], [-1, 0], [-1, 0]]
# dy = [[-1, 0], [1, 0], [0, -1], [0, 1]]    

# 날개 1, 날개 2, 그 다음 방문1, 그 다음 방문2
dx = [[0, 1, 1, 2], [0, 1, 1, 2], [-1, 0, -2, -1], [-1, 0, -2, -1]]
dy = [[-1, 0, -2, -1], [1, 0, 2, 1], [0, -1, -1, -2], [0, 1, 1, 2]]    

visited = [[0]*m for _ in range(n)]
answer = 0

def out_map(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return True
    return False

def dfs(x, y, power):
    global answer
    
    if (x, y) == (n-1, m-1):
        power += tree[x][y]*2 + tree[x-1][y] + tree[x][y-1]
        answer = max(answer, power)
        print(answer)
        sys.exit(0)
    
    # 범위를 벗어나거나 방문했다면,
    if out_map(x, y) or visited[x][y]:
        return

    # check = False
    # if (x, y) == (n-1, m-1):
    #     check = True
        
    visited[x][y] = 1
    for i, j in zip(dx, dy):
        nx1, ny1 = x + i[0], y + j[0]
        nx2, ny2 = x + i[1], y + j[1]
        
        next_x1, next_y1 = x + i[2], y + j[2]
        next_x2, next_y2 = x + i[3], y + j[3]
        
        # 범위를 벗어나거나 방문했다면,
        if out_map(nx1, ny1) or out_map(nx2, ny2) or visited[nx1][ny1] or visited[nx2][ny2]:
            continue
        
        # 이번 부메랑 방문하고, 그 다음 방문
        visited[nx1][ny1], visited[nx2][ny2] = 1, 1
        n_power = power + tree[x][y]*2 + tree[nx1][ny1] + tree[nx2][ny2]
        
        dfs(next_x1, next_y1, n_power)
        dfs(next_x2, next_y2, n_power)
        
        # 이번 부메랑 방문 안하고, 날개 방문
        visited[x][y], visited[nx1][ny1], visited[nx2][ny2] = 0, 0, 0
        dfs(nx1, ny1, power)
        dfs(nx2, ny2, power)
        
    # if check:
    #     answer += power
    answer = max(answer, power)
    return


# 너무 작아서 부메랑을 만들 수 없는 경우
if n < 2 or m < 2:
    print(0)
    
else:
    dfs(0, 0, 0)
    print(answer)
    
    
'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''