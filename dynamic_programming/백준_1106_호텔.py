'''
# 백준_1106_호텔. 골드 5. 풀이: 23.05.26 -> 실패

# How to
- 1 <= 최소 고객 수 c <= 1000
- 1 <= 도시 수 n <= 20
- 1 <= 비용, 고객 수 <= 100
- 출력값 최대: 100*1000 = 100_000

비용: 고객
1: 1
2: 5
3: 6
4: 10
5: 11
6: 12, 15, 12, 12


# Review
- 비용마다 가능한 최대 고객수를 기록하고, 그 기록수가 목표를 넘는 순간 출력하도록 했다.
    - 그러나 실패.. 또는 시간초과. 아니 왜 실패하는걸까?
    - 예제와 반례는 다 맞았는데도 실패하는 것을 보면, 히든 케이스가 있는가보다.
- 비록 실패했지만, 입력을 바로 딕셔너리로 저장하는 법을 찾으면서 dictionary comprehension을 조금 배웠다.

## 1. 기본
dic = dict()
for _ in range(n):
    a, b = map(int, input().split())
    dic[a] = b
    
## 한 문장에: 1번이 제일 좋아보인다.
dic1 = dict(map(lambda _: tuple(map(int, input().split())), range(n)))
dic2 = dict((a, b) for _ in range(n) for a, b in [map(int, input().split())])
dic3 = {int(x): int(y) for _ in range(n) for x, y in [input().split()]}
dic4 = dict(map(lambda xy: (int(xy[0]), int(xy[1])), [input().split() for _ in range(n)]))

'''

# 1. 실패 Code
import sys
input = sys.stdin.readline

# 최소 고객 수 c, 도시 수 n
c, n = map(int, input().split())
# 비용 a, 증가하는 고객 수 b
# dictionary comprehension
dp = dict(map(lambda _: tuple(map(int, input().split())), range(n)))
min_cost, max_cost = min(dp), max(dp)

for i in range(min_cost, 100_001):
    for j in range(1, i):
        jj = i-j
        if j in dp and jj in dp:
            tmp = dp[j] + dp[jj]
            if i in dp:
                dp[i] = max(dp[i], tmp)
            else:
                dp[i] = tmp
                
    if i in dp and dp[i] >= c:
        print(i)
        # print({key: dp[key] for key in sorted(dp)})
        sys.exit(0)
  

# 2. 시간초과 Code
import sys
input = sys.stdin.readline

# 최소 고객 수 c, 도시 수 n
c, n = map(int, input().split())
# 비용 a, 증가하는 고객 수 b
dp = [0] * 100_001
min_cost = int(1e9)
for _ in range(n):
    a, b = map(int, input().split())
    dp[a] = max(dp[a], b)
    min_cost = min(min_cost, a)

for i in range(min_cost, 100_001):
    for j in range(1, i):
        jj = i-j
        dp[i] = max(dp[i], dp[j] + dp[jj])
                
    if dp[i] >= c:
        print(i)
        sys.exit(0)

# 3. 이번에는?! 39%에서 시간초과..
import sys
input = sys.stdin.readline

# 최소 고객 수 c, 도시 수 n
c, n = map(int, input().split())
# 비용 a, 증가하는 고객 수 b
arr = sorted(list(map(int, input().split())) for _ in range(n))
min_cost, max_cost = arr[0][0], arr[-1][0]
max_num = c*max_cost + 1
dp = [0] * max_num
for a, b in arr:
    dp[a] = max(dp[a], b)

for i in range(min_cost, max_num):
    for j in range(1, i):
        jj = i-j
        dp[i] = max(dp[i], dp[j] + dp[jj])
                
    if dp[i] >= c:
        print(i)
        sys.exit(0)
          
        
'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''