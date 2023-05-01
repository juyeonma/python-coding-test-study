# 65%에서 틀림..ㅜㅜ
# 틀린 이유는?
# 아무래도 s와 d를 구분해주지 않았기 때문인 것 같다..! => 확실하진 않음..ㅜ..
# 질문 게시판에서 예시 부분이 통과되지 않았기 때문(s와 d로 인한 반례)에 그렇게 생각중

# 풀이 방법
# bfs를 찾아보다가 전에 풀었던 바이러스를 응용하면 될 것 같다는 느낌을 토대로 풀어보았다.
# visited에 이동 거리를 넣어주고
# h가 남아있으면 이동 거리 넣기 / h가 없으면 넣어주지 않기로 구현
import sys
from collections import deque
# input = sys.stdin.readline

# n, h, d = map(int, input().split())
# data = list(list(input().rstrip()) for _ in range(n))

# start_x = start_y = 0
# for i in range(n):
#     for j in range(n):
#         if data[i][j] == 'S':
#             start_x = i
#             start_y = j

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# visited = [[0] * n for _ in range(n)]


# def bfs(s, h, data, visited, start_x, start_y):
#     global d
#     q = deque()
#     q.append((s, h, start_x, start_y))

#     visited[start_x][start_y] = s
#     while q:
#         s, h, x, y = q.popleft()

#         if h == -1:
#             break
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < n:
#                 if data[nx][ny] == '.' and not visited[nx][ny] and h > 0:
#                     visited[nx][ny] = s + 1
#                     q.append((s+1, h-1, nx, ny))
#                 elif data[nx][ny] == 'U' and not visited[nx][ny] and h > 0:
#                     q.append((s+1, h+d, nx, ny))
#                     visited[nx][ny] = s + 1
#                 elif data[nx][ny] == 'E' and not visited[nx][ny] and h > 0:
#                     # print return은 찾아보고 도움을 받은 부분
#                     print(s+1)
#                     return
#     print(-1)


# bfs(0, h, data, visited, start_x, start_y)


# 참고: https: // westmino.tistory.com/97
# 메모리 : 37524KB	시간 : 784ms
from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, h, d = map(int, input().split())
board = []

sx = sy = -1
for x in range(n):
    board.append(list(input().strip()))
    if sx == -1:
        for y in range(n):
            if board[x][y] == 'S':
                sx, sy = x, y


def solv():
    visited = [[0]*n for _ in range(n)]
    q = deque([(sx, sy, h, 0, 0)])
    visited[sx][sy] = h

    while q:
        x, y, now_h, now_d, cnt = q.pop()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if point_validator(nx, ny):
                if board[nx][ny] == 'E':
                    print(cnt+1)
                    return
                nxt_h = now_h
                nxt_d = now_d

                if board[nx][ny] == 'U':
                    nxt_d = d

                if nxt_d == 0:
                    nxt_h -= 1
                else:
                    nxt_d -= 1

                if nxt_h == 0:
                    continue

                if visited[nx][ny] < nxt_h:
                    visited[nx][ny] = nxt_h
                    q.appendleft((nx, ny, nxt_h, nxt_d, cnt+1))

    print(-1)


def point_validator(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True


solv()
