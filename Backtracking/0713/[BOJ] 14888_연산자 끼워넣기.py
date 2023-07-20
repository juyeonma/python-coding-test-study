n = int(input())
number = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

min_value = int(1e9)
max_value = -int(1e9)

def solve(s, a, b, c, d):
    global min_value, max_value
    if len(number) == 1:
        min_value = min(s, min_value)
        max_value = max(s, max_value)
        return

    if a > 0:
        a -= 1
        first = number.pop(0)
        second = number.pop(0)
        number.insert(0, first+second)
        solve(number[0], a, b, c, d)
        number.pop(0)
        number.insert(0, second)
        number.insert(0, first)
        a += 1
    
    if b > 0:
        b -= 1
        first = number.pop(0)
        second = number.pop(0)
        number.insert(0, first-second)
        solve(number[0], a, b, c, d)
        number.pop(0)
        number.insert(0, second)
        number.insert(0, first)
        b += 1

    if c > 0:
        c -= 1
        first = number.pop(0)
        second = number.pop(0)
        number.insert(0, first*second)
        solve(number[0], a, b, c, d)
        number.pop(0)
        number.insert(0, second)
        number.insert(0, first)
        c += 1

    if d > 0:
        d -= 1
        first = number.pop(0)
        second = number.pop(0)
        if first < 0:
            number.insert(0, abs(first)//second * -1)
        else:
            number.insert(0, first//second)
        solve(number[0], a, b, c, d)
        number.pop(0)
        number.insert(0, second)
        number.insert(0, first)
        d += 1

solve(0, a, b, c, d)
print(max_value)
print(min_value)

# 	메모리 : 31256	시간 : 92ms

# 숫자도 같이 solve에 넘겨줬으면 더 빨랐을 것 같다!
# 보완할 점!
# https://www.acmicpc.net/source/28897807 풀이 참고
import sys
N = int(sys.stdin.readline())
nums = [int(i) for i in sys.stdin.readline().split()]
a,b,c,d = map(int, sys.stdin.readline().split())

res = []
def btk(cnt, cur, a, b, c, d):
    if cnt == N:
        res.append(cur)
        return
    
    if a > 0: btk(cnt+1, cur+nums[cnt], a-1, b, c, d)
    if b > 0: btk(cnt+1, cur-nums[cnt], a, b-1, c, d)
    if c > 0: btk(cnt+1, cur*nums[cnt], a, b, c-1, d)
    if d > 0: btk(cnt+1, int(cur/nums[cnt]), a, b, c, d-1)


btk(1, nums[0], a,b,c,d)
print(max(res))
print(min(res))
