'''
# 백준_22944_죽음의 비. 골드 4. 풀이: 23.04.30 -> 실패

# 풀이방법
- 모든 우산 지대를 거치는 경우의 수(1개, 2개..)를 따져가면서 최솟값 구하기.
'''

'''
# 피드백
- 자꾸 67%에서 틀린다. 이유가 뭘까?
- 반례가 궁금하다. 테스트 케이스는 다 맞는데..
- 그리고, 설령 반례를 통과한다고 하더라도, 너무 시간 복잡도가 클거같다. 더 효율적인 코드는 없을까?
'''

# code
from itertools import permutations
import sys

# 한변의 길이 n, 체력 h, 우산 내구도 d
n, h, d = map(int, input().split())
arr = []
sx, sy = 0, 0
x, y = 0, 0
umb_zone = []
for i in range(n):
    tmp = list(input())
    # 우산 U, 현재 위치 S, 안전지대 E, 빈칸 .
    for j in range(n):
        if tmp[j] == 'U':
            umb_zone.append((i, j))
        elif tmp[j] == 'S':
            x, y = i, j
        elif tmp[j] == 'E':
            sx, sy = i, j

# 우산 안 쓰고도 갈 수 있다면,
len_min = abs(sx-x) + abs(sy-y)

if h - len_min >= 0:
    print(len_min)
    
# 우산을 써야만 한다면,,
else:
    answer = 1e9
    # 우산지대를 순서대로 들려보자.
    for len_umb_zone in range(1, len(umb_zone)+1):
        umn_per = list(permutations(umb_zone, len_umb_zone))
        nh, nx, ny = h, x, y
        for i in umn_per:
            umb = 0
            len_xy = 0
            for jx, jy in i:
                tmp_len_xy = abs(jx-nx) + abs(jy-ny)
                tmp = nh + umb - (tmp_len_xy-1)
                    
                # 우산지대 도착했는데 체력이 남았다면,
                if tmp > 0:
                    nh = tmp
                    umb = d-1
                    nx, ny = jx, jy
                    len_xy += tmp_len_xy
                    
            tmp_len_xy = abs(sx-nx) + abs(sy-ny)
            # 안전지대까지 도착했는데 체력이 남았다면,
            if nh + umb - (tmp_len_xy-1) > 0:
                len_xy += tmp_len_xy
                answer = min(answer, len_xy)
                # 최솟값이면 바로 출력 후 탈출
                if answer == len_min:
                    print(answer)
                    sys.exit(0) 
                
    # 도착할 수 없다면, -1 출력                  
    if answer == 1e9:
        print(-1)
    else:
        print(answer)
'''
# 결과
메모리:  KB
시간:  ms
코드 길이:  B
'''