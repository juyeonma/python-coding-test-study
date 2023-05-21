# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 교육 들었을 때 풀었던 문제..!
# 포인트 : 이전에 나누어졌던 숫자 + 1과 dp[i-1]+1과 비교하기..!
# 시간 : 552ms
# 메모리 : 39068KB
n = int(input())
dp = [0]*(n+1)
for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])


# 시간이 짧은 버전(36ms)
# 전체적인 흐름은 비슷한 것 같다
# 참고 : https://www.acmicpc.net/source/54980023
x=int(input())
dp={1:0}
def rec(n):
    if n in dp.keys():
        return dp[n]
    if (n%3==0) and (n%2==0):
        dp[n]=min(rec(n//2)+1,rec(n//3)+1)
    elif n%3==0:
        dp[n]=min(rec(n//3)+1,rec(n-1)+1)
    elif n%2==0:
        dp[n]=min(rec(n//2)+1,rec(n-1)+1)
    else:
        dp[n]=rec(n-1)+1
    return dp[n]
print(rec(x))
