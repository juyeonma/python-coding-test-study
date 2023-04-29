# 풀이 방법
# 나올 수 있는 경우를 다 구현
# 총 19번의 경우를 리스트안에 넣고 계산
# 단점 : 시간이 엄청 오래 걸림..
# 시간 : 7352ms..
# 메모리 : 37572KB
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

t_x = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 0, 1, 1], [0, 1, 2, 2], [0, 0, 1, 2], [0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1], [0, 0, 1, 2], [0, 1, 2, 2],
       [0, 1, 1, 2],  [0, 1, 1, 2], [0, 0, 1, 1], [1, 1, 0, 0],  [0, 0, 0, 1], [0, 1, 1, 1],  [0, 1, 1, 2], [0, 1, 1, 2]]
t_y = [[0, 1, 2, 3], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1], [0, 0, 1, 2], [0, 1, 2, 2], [0, 1, 2, 0], [2, 0, 1, 2], [0, 1, 0, 0], [1, 1, 0, 1],
       [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 1, 2], [0, 1, 1, 2], [0, 1, 2, 1], [1, 0, 1, 2],  [1, 0, 1, 1], [0, 0, 1, 0], ]

max_value = 0
data = list(list(map(int, input().split())) for _ in range(n))
for i in range(19):
    dx = t_x[i]
    dy = t_y[i]

    for x in range(n):
        for y in range(m):
            value = 0
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]

                if 0 <= nx < n and 0 <= ny < m:
                    value += data[nx][ny]
                else:
                    value = 0
                    break
            max_value = max(max_value, value)
print(max_value)

# 빠른 풀이의 경우 DFS를 많이 사용한다는 것을 알 수 있었다..
# DFS 풀이 공부하기!
