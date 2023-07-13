'''
# 백준_14888_연산자 끼워넣기. 실버 1. 풀이: 23.07.13

# How to
- 주의할 점:
    - 연산자 우선 순위를 무시하고 앞에서부터 진행한다.
    - 나눗셈은 정수 나눗셈으로 몫만 취한다.
    - 음수를 양수로 나눌 때, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
    - 1 ≤ Ai ≤ 100

- DFS
- 더하기, 빼기, 곱하기, 나누기의 개수가 남은 경우, 해당 연산으로 재귀.
- 수열을 다 계산한 경우, 최솟값과 최댓값 갱신.
- 나누기 할 때, 현재까지의 값이 음수인지 체크하기.

# Review
- 풀이 시간: 15분
- 예전에 실패했던 문제를 다시 풀었다.
- 찾아보니, 나누기에서 int(result / nums[idx+1]) 하면 더 간단하다.
'''

# Code
# 1.
## 메모리: 31256 KB, 시간: 64 ms
n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
max_answer, min_answer = -int(1e9), int(1e9)

def dfs(idx, result, plus, minus, mul, div):
    global min_answer, max_answer
    # 수열을 다 계산한 경우, 최솟값과 최댓값 갱신
    if idx == n-1:
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
        return
    
    # 더하기, 빼기, 곱하기, 나누기의 개수가 남은 경우, 해당 연산으로 재귀.
    if plus:
        dfs(idx+1, result + nums[idx+1], plus-1, minus, mul, div)
        
    if minus:
        dfs(idx+1, result - nums[idx+1], plus, minus-1, mul, div)

    if mul:
        dfs(idx+1, result * nums[idx+1], plus, minus, mul-1, div)

    if div:
        # dfs(idx+1, int(result / nums[idx+1]), plus, minus, mul, div-1)
        new_result = result // nums[idx+1]
        if result < 0:
            new_result = -(-result // nums[idx+1])
        dfs(idx+1, new_result, plus, minus, mul, div-1)
   
dfs(0, nums[0], plus, minus, mul, div)     
print(max_answer, min_answer, sep='\n')