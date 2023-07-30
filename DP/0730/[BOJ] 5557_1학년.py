# ..이게 어떻게 dp..?
# ㅠㅠ못풀었다..
# 참고 : https://enhjh.tistory.com/35
import sys
input=sys.stdin.readline

n=int(input())
dp=[[0 for _ in range(21)] for _ in range(n)]
arr=list(map(int, input().split()))

# 처음 숫자 셋팅
dp[0][arr[0]]=1

for i in range(1, n-1):
    for j in range(21):
        # 지난 계산했던 기록이 있는 행일 경우만 계산한다.
        if dp[i-1][j]:
            # 덧셈일 경우
            if 0<=j+arr[i]<=20:
                dp[i][j+arr[i]] += dp[i-1][j]
                
            # 뺄셈일 경우
            if 0<=j-arr[i]<=20:
                dp[i][j-arr[i]] += dp[i-1][j]

# 입력받았던 숫자 중 마지막 숫자와 일치하는 경우의 수가 얼마인지 출력
print(dp[n-2][arr[-1]])