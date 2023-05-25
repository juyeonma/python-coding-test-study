from itertools import combinations
n, k = map(int, input().split())
data = [int(input()) for i in range(n)]

# dp로 풀어야하는데 dp 생각보다는 완전 탐색만 생각이 났다..ㅠ 
# => 조합을 이용한.. 하지만 삼중 포문이라 시간초과날 것 같아서 풀지는 못했다.

# dp에 너무 약하다. 결국 참고 답을 보았다. 
# 참고 : https://bitwise.tistory.com/504 / https://seongjuk.tistory.com/entry/BOJ-%EB%B0%B1%EC%A4%80-2293%EB%B2%88-%EB%8F%99%EC%A0%84-1
# 표로 정리를 하는 습관을 가지자..!
# 다시 풀기 위해 백준에는 제출하지 않아서 메모리와 시간은 모르겠다.

dp = [0] * (k+1)
dp[0] = 1
for i in range(n):
    for j in range(data[i], k+1):
        dp[j] += dp[j - data[i]]

print(dp[k])