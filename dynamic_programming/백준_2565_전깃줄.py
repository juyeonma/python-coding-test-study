'''
# 백준_2565_전깃줄. 골드 5. 풀이: 23.05.28 -> 실패

# How to
- 꼬였다는건?
    - 맨 뒤부터 시작하면, 더 작은 A에 더 큰 B가 있는가?
    - 맨 앞부터 시작하면, 더 큰 A에 더 작은 B가 있는가?
    
- 구글링 -> 가장 긴 증가하는 수열을 구하는 문제와 같다는것!
    - 꼬였다는 것은, 증가하는 수열의 어긋나는 부분이 있다는것
    - 전체 길이 - 가장 긴 증가하는 수열 길이 = 꼬인 전깃줄 개수의 최솟값
    
- 점화식: 이전 A와 연결된 B가 더 작을 경우(즉 증가하는 수열이면)
if arr[i][1] > arr[j][1]:
    dp[i] = max(dp[i], dp[j]+1)


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
- '가장 긴 증가하는 수열'을 구하는 것이라는 힌트를 듣고 그대로 푸니까.. 바로 성공
    - 문제에서 근본적으로 묻는게 뭔지를 바로 캐치해야하는구나!
'''

# 힌트 -> 성공
# '가장 긴 증가하는 수열'을 구하는 문제임 -> 전체 갯수에서 가장 긴 수열의 길이를 뺌
# 31388	KB 40 ms
import sys
input = sys.stdin.readline

n = int(input())
arr =[list(map(int, input().split())) for _ in range(n)]
arr.sort()
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        # 이전 A와 연결된 B가 더 작을 경우(즉 증가하는 수열이면)
        if arr[i][1] > arr[j][1]:
            # 수열의 길이 갱신
            dp[i] = max(dp[i], dp[j]+1)
# 꼬였다는 것은, 증가하는 수열의 어긋나는 부분이 있다는것.
# 그러므로 전체 길이 - 가장 긴 증가하는 수열 길이 = 꼬인 전깃줄 개수의 최솟값
print(n-max(dp))


# 실패 Code
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