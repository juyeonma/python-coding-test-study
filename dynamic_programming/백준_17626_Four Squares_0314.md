# 백준_17626_Four Squares_0314: 실버 3 (23.03.15 풀이)
- python으로도 시간초과 안 나는 풀이는 DP 가 아니어서, 패스
- pypy로 풀어야 하지만, DP 풀이가 있음.
- `dp[i] = min(dp[i], dp[i - (j**2)] + 1)`
  - 숫자 i가 되는 제곱수들의 최소 개수(=dp[i])는 `dp[i에서 i보다 작은 제곱수를 뺸 값] + dp[i보다 작은 제곱수]`
  - 모든 제곱수의 dp 값은 1 이므로, 결국 `dp[i에서 i보다 작은 제곱수를 뺸 값]`의 최솟값을 구하는 것이 포인트.


### 풀이 방법
#### pypy 풀이
```python
import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    # 최솟값을 구해야하므로, 큰수로 초기화
    min_value = 1e9
    j = 1
    
    # dp[i에서 i보다 작은 제곱수를 뺸 값]의 최솟값을 구하기
    while (j ** 2) <= i:
        min_value = min(min_value, dp[i - (j ** 2)])
        j += 1
    dp[i] = min_value + 1

print(dp[n])
```

### 해설
```
예를 들면, 8일 때  

8보다 작은 제곱수: 1, 4  
모든 제곱수의 dp 값은 1  
dp[1] = dp[4] = 1  

즉 dp[8]은.. 
dp[8-1] + dp[1] = dp[7] + 1  
dp[8-4] + dp[4] = dp[4] + 1  

그러면, dp[7]은?
dp[7-1] + dp[1] = dp[6] + 1
dp[7-4] + dp[4] = dp[3] + 1

...
이런식으로 쪼개지고 쪼개짐.
즉, 낮은 숫자부터 차근차근 dp 값 채우면 됨.
```

### 결과
