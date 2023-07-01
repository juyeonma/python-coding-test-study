'''
# 백준_5212_지구 온난화. 실버 2. 풀이: 23.06.29

# How to
- 인접한 세 칸 또는 네 칸이 바다인 땅은 잠긴다.
- 즉, 붙어있는 땅이 1개 이하인 땅은 잠긴다.

- 원래 지도를 복사해서 정답 지도를 만든다.
- 지도의 땅을 찾아서, 사방의 땅 개수를 구한다.
    - 사방의 땅이 1개 이하라면, 바다로 바꾼다.
    - 그대로 땅이라면, 정답의 크기 범위를 갱신한다.
- 정답 범위안에서 출력한다.

# Review
- 처음에 무심코 copy()를 썼다가, 헤맸다. 여기서 시간 대부분을 쏟았다..ㅎ
    - 다시 보니까 이중 리스트이므로 깊은 복사를 해야했다.
- 매번 정답의 크기 범위를 갱신했는데, 더 빠르고 효율적인 방법 없을까?
'''

# 성공 Code
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
dadohae = [list(input().rstrip()) for _ in range(r)]
answer = [i[:] for i in dadohae]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer_r1, answer_c1, answer_r2, answer_c2 = r-1, c-1, 0, 0

for x in range(r):
    for y in range(c):
        # 땅이라면,
        if dadohae[x][y] == 'X':
            tmp = 0
            # 사방에 땅이 몇개인지
            for i, j in zip(dx, dy):
                nx = x + i
                ny = y + j
                if 0 <= nx < r and 0 <= ny < c and dadohae[nx][ny] == 'X':
                    tmp += 1
            # 땅 -> 바다
            if tmp <= 1:
                answer[x][y] = '.'
                
            # 땅 -> 땅 그대로
            else:
                # 정답의 지도 크기 범위 갱신
                answer_r1, answer_c1 = min(answer_r1, x), min(answer_c1, y)
                answer_r2, answer_c2 = max(answer_r2, x), max(answer_c2, y)

# 정답 범위안에서 출력
for i in range(answer_r1, answer_r2+1):
    print(''.join(answer[i][answer_c1:answer_c2+1]))


'''
# Result
풀이 시간: 30분
메모리: 31256 KB
시간: 60 ms
코드 길이: 1069 B
'''