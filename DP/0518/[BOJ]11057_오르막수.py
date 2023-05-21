# 문제가 이해가 안갔다..
# 문제를 어떻게 해야 이해가 잘 될까.. 고민해봐야겠다

# 설명을 찾았다.
# 참고 : https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-11057-%EC%98%A4%EB%A5%B4%EB%A7%89-%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python

# 오르막 수 : 수의 자리가 오름차순을 이루는 수, 인접한 수가 같아도 오름차순

# 길이 \ 맨 뒷자리 숫자 를 기준으로 dp 식을 세우면 되는거였다.
# 메모리 : 31256KB 시간 : 44ms
n = int(input())
dp = [1]*10
for i in range(1,n) :
    for j in range(1,10) :
        dp[j] += dp[j-1]

print(sum(dp)%10007)