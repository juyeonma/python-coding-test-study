# 스터디하면서 비슷한 유형을 풀어봤었는데 못 풀었다.
#이런 방식으로 dp를 다루는게 익숙하지 않나보다
# 배낭문제라고 하는데.. 못 풀 줄 몰랐다...

t = int(input())

for _ in range(t):
    n = input()
    nums = list(map(int,input().split()))
    m = int(input())

    memo=[1]+[0]*m

    for num in nums:
        for i in range(num,m+1):
                memo[i] += memo[i-num]

    print(memo[m])