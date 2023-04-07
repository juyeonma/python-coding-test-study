# loling3님의 코드 참고
# 문제 분석
# 최소 3 최대 3000
# 문제 구현
# 1. 배열 선언
# 2. 유성과 땅 값을 저장
# 2-1. 가로x, 세로로 저장
# 2-2. 유성은 값 저장 -> . 으로 변경
# 2-3. 땅은 최소값만 저장
# 3. 유성이 이동할 수 있는 거리를 구하기
# 4. 거리만큼 이동하여서 유성 값 채우기

import sys
input = sys.stdin.readline
r, s = map(int, input().split())

data = [list(input().rstrip()) for _ in range(r)]
star = [[] for _ in range(s)]
ground = [r] * s

for i in range(r):
    for j in range(s):
        if data[i][j] == 'X':
            star[j].append(i)
            data[i][j] = '.'
        elif data[i][j] == '#':
            if ground[j] == r:
                ground[j] = i
d = r
for i in range(s):
    if star[i] and d > ground[i] - max(star[i]):
        d = ground[i] - max(star[i])
for i in range(s):
    for j in range(len(star[i])):
        data[star[i][j] + d-1][i] = 'X'

for i in range(r):
    print(''.join(data[i]))
