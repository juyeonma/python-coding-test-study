'''
# 백준_2580_스도쿠. 골드 5. 풀이: 23.07.21

# How to
- 정사각형 그룹 인덱스 구하려면,
8 // 3 = 2그룹
8 % 3 = 2번째

- 빈칸을 별도의 리스트로 만든 뒤, 인덱스를 진전시키며 dfs를 돌린다.
- 이때, 가로 세로 그룹에 없는 숫자들을 후보로 지정하여, 이 숫자들을 빈칸에 넣고 다음 인덱스로 넘어간다.
    - 미리 세로, 그룹의 숫자 집합을 담을 리스트를 만들어서 매번 체크를 해서 시간을 줄인다.
- 인덱스 범위를 벗어난 경우, 탐색이 끝났으므로 출력 후 종료

# Review
- 풀이 시간: 2시간
- 파이썬으로는 통과인데 pypy로는 시간초과인 이유가 뭘까..?
- 여전히 느리다.
- 가로, 세로, 그룹에 없는 숫자를 고르는 코드를 더 좋은 방식으로 구현할 순 없을까?
'''

# Code
# 1. 성공
## 메모리: 31256 KB, 시간: 1980 ms
## pypy: 82% 시간초과
import sys
input = sys.stdin.readline

board = [input().split() for _ in range(9)]

# 빈칸 리스트
zero = []
for i in range(9):
    for j in range(9):
        if board[i][j] == '0':
            zero.append((i, j))
n = len(zero)

visited = [False] * n

# 세로, 그룹의 숫자 집합을 저장할 곳
nums_col = [set() for _ in range(9)]
nums_group = [[set() for _ in range(3)] for _ in range(3)]

# 후보 숫자 고르기: 가로, 세로, 그룹에 모두 없는 것
def make_candi(x, y, ngx, ngy):
    candi = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    
    # 가로
    candi -= set(board[x])
    
    if not candi:
        return []
    
    # 세로
    if not nums_col[y]:
        col = set()
        for i in range(9):
            col.add(board[i][y])
        nums_col[y] = col
        
    candi -= nums_col[y]
    
    if not candi:
        return []
    
    # 그룹
    if not nums_group[ngx][ngy]:
        group = set()
        gx, gy = ngx*3, ngy*3
        for i in range(gx, gx+3):
            group = group | set(board[i][gy:gy+3])
        nums_group[ngx][ngy] = group
        
    candi -= nums_group[ngx][ngy]
    
    return candi

def dfs(idx):
    # 인덱스 범위를 벗어난 경우, 탐색이 끝났으므로 출력 후 종료
    if idx == n:
        for i in board:
            print(' '.join(i))
        sys.exit(0)
    
    # 이미 방문했다면, 즉 빈칸이 아니면, 되돌아감
    if visited[idx]:
        return
    
    # 현재 인덱스에 해당하는 빈칸의 좌표
    x, y = zero[idx]
    ngx, ngy = x//3, y//3
    # 후보 숫자를 넣고 재귀로 들어감.
    for num in make_candi(x, y, ngx, ngy):
        board[x][y] = num
        nums_col[y].add(num)
        nums_group[ngx][ngy].add(num)
        visited[idx] = True

        dfs(idx+1)
        
        board[x][y] = 0
        nums_col[y].remove(num)
        nums_group[ngx][ngy].remove(num)
        visited[idx] = False
        
dfs(0)