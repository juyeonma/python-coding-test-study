'''
# 백준_2565_전깃줄. 골드 5. 풀이: 23.05.28 -> 실패

# How to
- 맨 뒤부터 시작하면, 더 작은 A에 더 큰 B가 있는가?
- 맨 앞부터 시작하면, 더 큰 A에 더 작은 B가 있는가?

0 1 1 3 3 3 3 3

## 반례
2
1 2
4 1
답:1

5
1 3
3 1
2 5
4 6
6 4
답: 2

2
2 4
5 6
답: 0

4
5 7
6 8
7 5
8 6
답: 2

# Review
- 질문게시판의 반례를 모두 통과했으나, 9%에서 틀린다. 왜지..?
- 아예 다른 접근을 사용해야겠다ㅠㅠ
'''

# Code
import sys
input = sys.stdin.readline

n = int(input())
arr =[list(map(int, input().split())) for _ in range(n)]
arr.sort()
dp = [0] * n

for a in range(n):
    b = arr[a][1]
    tmp = 0
    for j in range(a):
        # 선이 엇갈렸다면, +1
        if arr[j][1] > b:
            tmp += 1
            
        # 선이 바른 배열이라면, 이전 값 갱신
        else:
            dp[a] = max(dp[a], dp[j])
    # 엇갈린 갯수와의 최댓값 갱신
    dp[a] = max(dp[a], tmp)
    
print(max(dp))


'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''