# import sys
# import copy
# input = sys.stdin.readline

# # 1번 : 한 방향 # 2번 두 방향 : 반대 # 3번 두 방향 : 직각 # 4번 세 방향 # 5번 네 방향
# # 6 = 벽 만나면 종료...?..
# # 다른 CCTV를 만나면 통과..
# # 완전 탐색 같음..!
# # 다 하나씩 존재한다면..?..
# # 첫 번째 노드 : 1, 2, 3, 4
# # 두 번째 노드 : 1, 2
# # 세 번째 노드 : 1, 2, 3, 4
# # 네 번째 노드 : 1, 2, 3, 4
# # 다섯번째 노드 : 1
# n, m = map(int, input().split())
# office = [list(map(int, input().split())) for _ in range(n)]
# cctv = [[] for _ in range(6)]
# number = [1, 2, 3, 4, 5]
# temp = copy.deepcopy(office)
# for i in range(n):
#     for j in range(m):
#         if office[i][j] == 0:
#             continue
#         elif office[i][j] == 1:
#             cctv[1].append((i, j))
#         elif office[i][j] == 2:
#             cctv[2].append((i, j))
#         elif office[i][j] == 3:
#             cctv[3].append((i, j))
#         elif office[i][j] == 4:
#             cctv[4].append((i, j))
#         elif office[i][j] == 5:
#             cctv[5].append((i, j))

# # while True:
# for i in cctv[5]:
#     # 상-오-하-왼
#     for j in range(i[0]-1, -1, -1):
#         if office[j][i[1]] in number:
#             continue
#         elif office[j][i[1]] == 6:
#             break
#         temp[j][i[1]] = '#'
#     for j in range(i[1]+1, m):
#         if office[i[0]][j] in number:
#             continue
#         elif office[i[0]][j] == 6:
#             break
#         temp[i[0]][j] = '#'
#     for j in range(i[0]+1, n):
#         if office[j][i[1]] in number:
#             continue
#         elif office[j][i[1]] == 6:
#             break
#         temp[j][i[1]] = '#'
#     for j in range(i[1]-1, -1, -1):
#         if office[i[0]][j] in number:
#             continue
#         elif office[i[0]][j] == 6:
#             break
#         temp[i[0]][j] = '#'
#     office = copy.deepcopy(temp)

# for i in cctv[4]:
#     min_value = n * m + 1
#     cnt = 5
#     for k in range(4):
#         count = 0
#         if k == 0:
#             # 오 + 상 + 왼
#             for j in range(i[1]+1, m):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#             for j in range(i[0]-1, -1, -1):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#             for j in range(i[1]-1, -1, -1):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#         elif k == 1:
#             # 상 + 왼 + 하
#             for j in range(i[0]-1, -1, -1):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#             for j in range(i[1]-1, -1, -1):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#             for j in range(i[0]+1, n):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#         elif k == 2:
#             # 하 + 왼 + 오
#             for j in range(i[0]+1, n):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#             for j in range(i[1]-1, -1, -1):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#             for j in range(i[1]+1, m):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#         elif k == 3:
#             # 하 + 오 + 상
#             for j in range(i[1]-1, -1, -1):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#             for j in range(i[1]+1, m):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#             for j in range(i[0]-1, -1, -1):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#         for x in range(n):
#             for y in range(m):
#                 if temp[x][y] == 0:
#                     count += 1

#         if min_value > count:
#             min_value = count
#             cnt = k
#         temp = copy.deepcopy(office)

#     if cnt == 0:
#         # 오 + 상 + 왼
#         for j in range(i[1]+1, m):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#         for j in range(i[0]-1, -1, -1):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#         for j in range(i[1]-1, -1, -1):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#     elif cnt == 1:
#         # 상 + 왼 + 하
#         for j in range(i[0]-1, -1, -1):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#         for j in range(i[1]-1, -1, -1):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#         for j in range(i[0]+1, n):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#     elif cnt == 2:
#         # 하 + 왼 + 오
#         for j in range(i[0]+1, n):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#         for j in range(i[1]-1, -1, -1):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#         for j in range(i[1]+1, m):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#     elif cnt == 3:
#         # 하 + 오 + 상
#         for j in range(i[1]-1, -1, -1):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#         for j in range(i[1]+1, m):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#         for j in range(i[0]-1, -1, -1):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#     office = copy.deepcopy(temp)

# for i in cctv[3]:
#     min_value = n * m + 1
#     cnt = 5
#     for k in range(4):
#         count = 0
#         if k == 0:
#             # 오 + 상
#             for j in range(i[1]+1, m):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#             for j in range(i[0]-1, -1, -1):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#         elif k == 1:
#             # 상 + 왼
#             for j in range(i[0]-1, -1, -1):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#             for j in range(i[1]-1, -1, -1):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#         elif k == 2:
#             # 하 + 왼
#             for j in range(i[0]+1, n):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#             for j in range(i[1]-1, -1, -1):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#         elif k == 3:
#             # 하 + 오
#             for j in range(i[1]-1, -1, -1):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#             for j in range(i[1]+1, m):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#         for x in range(n):
#             for y in range(m):
#                 if temp[x][y] == 0:
#                     count += 1

#         if min_value > count:
#             min_value = count
#             cnt = k
#         temp = copy.deepcopy(office)

#     if cnt == 0:
#         # 오 + 상
#         for j in range(i[1]+1, m):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#         for j in range(i[0]-1, -1, -1):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#     elif cnt == 1:
#         # 상 + 왼
#         for j in range(i[0]-1, -1, -1):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#         for j in range(i[1]-1, -1, -1):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#     elif cnt == 2:
#         # 하 + 왼
#         for j in range(i[0]+1, n):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#         for j in range(i[1]-1, -1, -1):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#     elif cnt == 3:
#         # 하 + 오
#         for j in range(i[1]-1, -1, -1):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#         for j in range(i[1]+1, m):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#     office = copy.deepcopy(temp)
# for i in cctv[2]:
#     min_value = n * m + 1
#     cnt = 5
#     for k in range(2):
#         count = 0
#         if k == 0:
#             # 왼-오
#             for j in range(i[1]-1, -1, -1):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#             for j in range(i[1]+1, m):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#         elif k == 1:
#             # 상-하
#             for j in range(i[0]-1, -1, -1):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#             for j in range(i[0]+1, n):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#         for x in range(n):
#             for y in range(m):
#                 if temp[x][y] == 0:
#                     count += 1
#         if min_value > count:
#             min_value = count
#             cnt = k
#         temp = copy.deepcopy(office)
#     if cnt == 0:
#         # 왼-오
#         for j in range(i[1]-1, -1, -1):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#         for j in range(i[1]+1, m):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#     elif cnt == 1:
#         # 상-하
#         for j in range(i[0]-1, -1, -1):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#         for j in range(i[0]+1, n):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#     office = copy.deepcopy(temp)
# for i in cctv[1]:
#     min_value = n * m + 1
#     cnt = 5
#     for k in range(4):
#         count = 0
#         if k == 0:
#             # 오른쪽
#             for j in range(i[1]+1, m):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#         elif k == 1:
#             # 상
#             for j in range(i[0]-1, -1, -1):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#         elif k == 2:
#             # 하
#             for j in range(i[0]+1, n):
#                 if office[j][i[1]] in number:
#                     continue
#                 elif office[j][i[1]] == 6:
#                     break
#                 temp[j][i[1]] = '#'
#         elif k == 3:
#             # 왼
#             for j in range(i[1]-1, -1, -1):
#                 if office[i[0]][j] in number:
#                     continue
#                 elif office[i[0]][j] == 6:
#                     break
#                 temp[i[0]][j] = '#'
#         for x in range(n):
#             for y in range(m):
#                 if temp[x][y] == 0:
#                     count += 1

#         if min_value > count:
#             min_value = count
#             cnt = k
#         temp = copy.deepcopy(office)
#     if cnt == 0:
#         # 오른쪽
#         for j in range(i[1]+1, m):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#     elif cnt == 1:
#         # 상
#         for j in range(i[0]-1, -1, -1):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#     elif cnt == 2:
#         # 하
#         for j in range(i[0]+1, n):
#             if office[j][i[1]] in number:
#                 continue
#             elif office[j][i[1]] == 6:
#                 break
#             temp[j][i[1]] = '#'
#     elif cnt == 3:
#         # 왼
#         for j in range(i[1]-1, -1, -1):
#             if office[i[0]][j] in number:
#                 continue
#             elif office[i[0]][j] == 6:
#                 break
#             temp[i[0]][j] = '#'
#     office = copy.deepcopy(temp)

# print(cctv)
# print()
# for i in office:
#     print(' '.join(map(str, i)))
# print()
# for i in temp:
#     print(' '.join(map(str, i)))
# result = 0
# for i in range(n):
#     for j in range(m):
#         if temp[i][j] == 0:
#             result += 1
# print(result)
# # 순서가 있기 때문에 틀린것같다..! => 완전 탐색이라고 볼 수 없음..
# 5 - 4 - 3 - 2 -1
# dfs 함수 응용해서 풀기 참고 : https://yeon-code.tistory.com/76

import copy
n, m = map(int, input().split())
cctv = []
office = []
direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    office.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])


def fill(office, d, x, y):
    for i in d:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if office[nx][ny] == 6:
                break
            elif office[nx][ny] == 0:
                office[nx][ny] = -1


def dfs(depth, office):
    global min_value
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += office[i].count(0)
        min_value = min(min_value, count)
        return

    temp = copy.deepcopy(office)
    cctv_num, x, y = cctv[depth]
    for i in direction[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(office)


min_value = n * m + 1
dfs(0, office)
print(min_value)
