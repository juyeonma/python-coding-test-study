# 풀이방법
# 1. 나올 수 있는 조합 구해서 더한 후 리스트에 넣기
# 2. 중복 X
# 3. 숫자를 차례대로 비교

# 메모리 : 96856KB
# 시간 : 536MS
import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))

data = []
# 1번
for i in range(1, n+1):
    for j in combinations(s, i):
        data.append(sum(j))
# 2번
data = list(set(data))
data.sort()
# 3번
for i in range(1, len(data)+1):
    if data[i-1] == i:
        continue
    else:
        print(i)
        sys.exit(0)
print(data[-1]+1)

# 시간초가 짧은 훨씬 간단한 코드(36ms)
# 참고 : https://www.acmicpc.net/source/52737816
# ! 간단한 방법들도 앞으로 생각해봐야겠다..
N = int(input())
L = sorted(list(map(int, input().split())))
num = 1
for i in L:
    if num < i:
        break
    num += i
print(num)
