# 문제 이해부터 못했다...ㅜㅜ...
# 참고 : https://kyun2da.github.io/2021/04/06/dragonCurve/
# 시뮬레이션 문제
# 1. x, y, d, g 받아주기
# 2. 방향 저장
# 3. 세대만큼 방향 규칙에 의해 방향 정보 저장하기
# 4. 저장된 방향 정보에 1 넣어주고 꼭짓점 변경
# 5. 총 네 꼭짓점이 모두 드래곤커브인것 찾기
import sys
input = sys.stdin.readline

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 초기화
arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    arr[x][y] = 1

    move = [d]

    # g 세대가 될때까지 반복
    # 방향 규칙 => 이전 세대의 정보를 뒤집어 거기에 1 더하기, 4면 처음 0으로 돌리기
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i-1]+1) % 4)
        move.extend(tmp)
    # 세대의 방향에 1 넣어주고 꼭짓점 변경
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        arr[nx][ny] = 1
        x, y = nx, ny

# 네 꼭짓점이 모두 드래곤 커브의 일부인 것 찾기
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            ans += 1
print(ans)
