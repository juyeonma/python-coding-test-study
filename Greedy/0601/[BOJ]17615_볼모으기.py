# 15점에서 계속 틀림... => 오른쪽으로 모는 경우만 구해서 그렇다..
# 참고 : https://zoosso.tistory.com/403
import sys
input = sys.stdin.readline
n = int(input())
ball = list(input().rstrip())

# 각 색깔의 개수 셈 => 작은 값이 답 후보(색의 모든 볼을 다 옮기는 경우)
red = ball.count("R")
blue = ball.count("B")

ans = min(red, blue)

# 가장 왼쪽부터 연속된 색깔의 개수를 세어서 해당색의 전체개수에서 뺌
# 기존의 답보다 작으면 갱신(나머지 볼을 왼쪽으로 옮기는 경우)
cnt = 0
for i in range(n):
    if ball[i] != ball[0]:
        break
    cnt += 1
if ball[0] == "R":
    ans = min(ans, red - cnt)
else:
    ans = min(ans, blue - cnt)
# 가장 오른쪽부터 연속된 색깔의 개수를 세어서 해당색의 전체개수에서 뺌
# 기존의 답보다 작으면 갱신(나머지 볼을 오른쪽으로 옮기는 경우)
cnt = 0
for i in range(n-1, -1, -1):
    if ball[i] != ball[-1]:
        break
    cnt += 1

if ball[-1] == 'R':
    ans = min(ans, red - cnt)
else:
    ans = min(ans, blue - cnt)

print(ans)

# 다음에 다시 풀기!!