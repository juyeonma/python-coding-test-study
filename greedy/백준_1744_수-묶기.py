'''
# 백준_1744_수 묶기. 골드 4. 풀이: 23.06.01

# How to
- 어떻게?
    - 1 보다 크면, 무조건 곱하는게 이득
    - 0이면, 양수일 떄는 더하고, 음수일 때는 곱하기(0이 되므로)
    - 음수끼리는 곱하는게 이득
    - 1은 무조건 더해야함
- 방법
    - 2 이상, 1, 0 이하로 나눈다.
    - 1은 무조건 더하므로, 먼저 정답에 더해줌
    - 2 이상(plus) 그룹은 내림차순, 0 이하(minus) 그룹은 오름차순 정렬
    - 각 그룹을 둘씩 짝지어서 곱함. 이때 홀수개면, 마지막은 더해줌.

# Review
- 맞힌 사람을 보니, 다들 다양하게 풀었다. 차근차근 이해해봐야지.
'''


# 성공 Code
import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

answer = nums.count(1)
plus = sorted([x for x in nums if x > 1], reverse=True)
minus = sorted([x for x in nums if x <= 0])

def solve(len_group, group):
    global answer
    check = 0
    # 홀수개면, 마지막은 따로 더해줌.
    if len_group % 2: # 홀수
        check = -1
        answer += group[-1]
    # 그룹 길이 + 홀수개일 경우 -1을 뺀 범위까지 2씩 탐색
    for i in range(0, len_group+check, 2):
        # 연속되는 두 원소를 더함
        answer += group[i] * group[i+1]
        
solve(len(plus), plus)
solve(len(minus), minus)

print(answer)
'''
# Result
풀이 시간: 40분
메모리: 31256 KB
시간: 40 ms
코드 길이: 514 B
'''