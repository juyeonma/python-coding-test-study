'''
# 백준_5557_1학년. 골드 5. 풀이: 23.07.29 -> 실패

# How to
- 기호: +, -
- 범위: 계산 도중이나 마지막까지 0 <= num <= 20
- 마지막 수 앞에 =. 즉 앞에까지 계산한 값 = 마지막 수

## 1. dfs: 시간초과
- 재귀로 했으나, 역시나 시간초과.

## 2. 실패
- 매 원소마다 경우의 수를 누적하려고 했으나, 중간에 조건에 맞지않아(0보다 작거나 20보다 큰 경우) 탈락하는 수를 빼지 않아 답이 맞지 않았다.


# Review
- 풀이 시간:
- 아무리 생각해도 dfs나 완전탐색으로 모든 경우의 수를 구하는 것 이외에는 dp로 구현이 떠오르지 않는다..
'''

# Code
# 1. dfs: 시간초과
## 메모리:  KB, 시간:  ms
n = int(input())
nums = list(map(int, input().split()))

# dp = [0] * n
answer = 0
def dfs(idx, result):
    global answer
    
    if idx == n-1:
        if result == nums[-1]:
            answer += 1
        return
    
    if 0 <= result <= 20:
        dfs(idx+1, result+nums[idx])
        dfs(idx+1, result-nums[idx])
    
dfs(0, 0)
print(answer)


# 2. 실패
## 메모리:  KB, 시간:  ms
n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1

result = {nums[0]}
for i in range(1, n-1):
    tmp = set()
    for j in result:
        if 0 <= j + nums[i] <= 20:
            tmp.add(j + nums[i])
            dp[i] += 1
            
        if 0 <= j - nums[i] <= 20:
            tmp.add(j - nums[i])
            dp[i] += 1
            
    result.update(tmp)        
    

for i in result:
    if i == nums[-1]:
        dp[-1] += 1
        
# print()