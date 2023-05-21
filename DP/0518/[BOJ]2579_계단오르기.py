# 계단 오르기 문제가 이해가 가다가도
# 예제 : 10, 20, 15, 25, 10, 20에서
# 왜  10 + 20 + 25 + 10 + 20의 경로로 가는 건 안되는걸까?..하고 고민에 빠져서 문제를 풀지 못했다.
# 왜 저 경로는 안되는걸까요.. 이해시켜주실분 구합니다..ㅠㅠ..
# 는 결국 이해했습니다.. 세 개의 계단을 모두 밟아서는 안 된다를 세 개의 점프로 착각했던것이 문제였습니다..
# => 좀 더 규칙을 꼼꼼하게 생각해보는 습관을 가져야겠습니다..!

import sys
input = sys.stdin.readline
n = int(input())
data = list(int(input()) for _ in range(n))

# 참고 : https://bio-info.tistory.com/158
dp=[0]*(n)
if len(data) <= 2: # 계단이 2개 이하 => 다 더하기
    print(sum(data))
else: # 계단이 3개 이상
    dp[0]=data[0] # 첫째 계단
    dp[1]=data[0]+data[1] # 둘째 계단
    for i in range(2,n): # 세번째 계단부터 점화식 사용
        # i-1까지의 계단 점수 최댓값과 i-1, i계단의 합 / i-2까지의 계단 점수 최댓값과 i 계단의 합
        dp[i] = max(dp[i-3] + data[i-1] + data[i], dp[i-2] + data[i])
    print(dp[-1])

# 시간 : 40ms
# 메모리 : 31256KB