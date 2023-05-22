# 어떻게 풀 지 감도 안잡힌다... dp인거 몰랐으면 dp인지도 몰랐을 것 같다.
# 답을 보고 다른 문제 풀 때 dp의 정의를 다시 생각해보니 dp가 맞구나 싶었다.
# 어렵다 정말..ㅠㅠ
# 완벽히 내 것이 되었다는 느낌이 없다...

a = input()
b = input()
d= [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            d[i][j]=d[i-1][j-1]+1
        else:
            d[i][j]=max(d[i-1][j],d[i][j-1])

print(d[-1][-1])
