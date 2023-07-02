# 처음에 다 같은 방향으로 회전하는 줄 알고 헤맸다..
import sys
from collections import deque
input = sys.stdin.readline

wheel = deque()
# 같이 회전하는 톱니바퀴 찾기
def check(w, n, r):
    number = set()
    number.add((n, r))
    rt = r
    for i in range(n, 3):
        if wheel[i][2] != wheel[i+1][6]:
            rt *= -1
            number.add((i+1, rt))
        else:
            break
    rt = r
    for i in range(n, 0, -1):
        if wheel[i][6] != wheel[i-1][2]:
            rt *= -1
            number.add((i-1, rt))
        else:
            break
    return number

for _ in range(4):
    s = deque(input().rstrip())
    wheel.append(s)

k = int(input())
for _ in range(k):
    n, r = map(int, input().split())
    number = check(wheel, n-1, r)
    
    for i, j in number:
        wheel[i].rotate(j)

s = 1
total = 0
for i in range(4):
    if wheel[i][0] == '1':
        total += s
    s *= 2

print(total)

# 메모리 : 34184	시간 : 64