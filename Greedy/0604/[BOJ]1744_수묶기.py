# => 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능을 보고
# 같은 숫자는 묶는 것이 안되는 줄 알았는데.. 말 그대로 자기 자신만 불가능한것이었다....ㅠ....
# 반례보고 찾았는데 반례보기 전까지 한참을 헤맸던 것 같다
# 그래서 반례보고 원래 풀던 방식을 바꾸어서 푼 버전
import sys
input = sys.stdin.readline
n = int(input())

data = [int(input()) for _ in range(n)]

data.sort()
if n <= 1:
    print(data[0])
else:
    plus_one = 0
    plus = 0
    zero = 0
    minus = 0
    for i in range(n):
        if data[i] < 0:
            minus += 1
        elif data[i] == 0:
            zero += 1
        elif data[i] == 1:
            plus_one += 1
        else:
            plus += 1
    
    total = plus_one

    
    if minus > 0:
        sample = data[:minus]
        for i in range(int(minus/2)):
            total += (sample.pop(0) * sample.pop(0))
            minus -= 2
        if minus >= zero:
            for i in range(zero):
                sample.pop(0)
        else:
            for i in range(minus):
                sample.pop(0)
        total += sum(sample)
    if plus > 0:
        sample = data[-plus:][::-1]
        for i in range(int(plus/2)):
            total += (sample.pop(0) * sample.pop(0))
        total += sum(sample)
    print(total)

# 메모리 : 31256KB	시간 : 40ms