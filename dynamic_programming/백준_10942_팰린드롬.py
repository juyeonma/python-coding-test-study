'''
# 백준_10942_팰린드롬?. 골드 4. 풀이: 23.05.21 -> 실패

# How to
- 참고: https://velog.io/@himi/백준-10942.-팰린드롬
- 팰린드롬: 반으로 쪼개서, 대응되는 양쪽이 같아야함.
    - 1 == n? -> 2 == n-1? -> 3 == n-3? ... = 팰린드롬이다.
    - 거꾸로 생각하면, 2~n-1이 팰린드롬일 때 1 == n이면, 팰린드롬이다.

# Review
- index 설정 때문에 고생했다. 당연히 시작 index를 처음 for문으로 썼지만, 계속 index가 에러가 났다.
- 결국 검색을 했고.. 아직 dp 테이블이 채워지지 않은 상태에서 순차적으로 탐색해서 그렇다는걸 알게됐다.
- 그런데 여전히 어렵다ㅠ 이렇게 범위를 교차로? 탐색하는건..너무 어렵다..ㅠㅠ
- 맞힌 사람 코드를 보아도 다들 엄청난 시간에, 바로 이해되지 않는 코드들이더라. 차근차근 이해해보자.
'''

# Code
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)]
# 1글자, 2글자인 경우 팰린드롬 기록
for i in range(n-1):
    dp[i][i] = 1
    if num[i] == num[i+1]:
        dp[i][i+1] = 1
dp[n-1][n-1] = 1
    
for i in range(n):
    for a in range(n-i):
        b = a + i
        # 2글자 이상일때, 양끝이 같고, 안이 팰린드롬이라면
        if a != b and num[a] == num[b] and dp[a+1][b-1]:
            dp[a][b] = 1

            
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])

'''
# Result
풀이 시간:
메모리: 61988 KB
시간: 2188 ms
코드 길이: 483 B
'''