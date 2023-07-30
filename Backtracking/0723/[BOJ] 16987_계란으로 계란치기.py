# 틀린 풀이...(기록용..) => 구현 실패..
import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    a, b = map(int, input().split())
    data.append([a, b])
max_value = 0
def back(basic):
    global max_value
    if n-1 == basic:
        count = 0
        for i in range(n):
            if data[i][0] <= 0:
                count += 1
        max_value = max(max_value, count)
        return

    if data[basic][0] <= 0:
        back(basic+1)

    for i in range(n):
        if data[i][0] > 0 and data[basic][0] > 0 and i != basic:
            data[basic][0] -= data[i][1]
            data[i][0] -= data[basic][1]
            back(basic)
            data[basic][0] += data[i][1]
            data[i][0] += data[basic][1]
        
back(0)
print(max_value)

# 정답 풀이
# => 주연님 코드로 공부했습니다..