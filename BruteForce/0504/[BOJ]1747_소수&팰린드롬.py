# 풀이 방법
# 1. 팰린드롬 맞는지
# 2. 소수가 맞는지 => 함수로 뺌

# 메모리 : 31256KB
# 시간 : 512MS
import sys
input = sys.stdin.readline
INF = 1003002
n = int(input().rstrip())

# 2번


def solve(i):
    if i == 1:
        return False
    else:
        for j in range(2, i):
            if i % j == 0:
                return False
        return True


for i in range(n, INF):
    # 1번
    if i == int(str(i)[::-1]):
        if solve(i):
            print(i)
            break
