# 이건 스스로 못풀었습니다. 아이디어를 떠올리지 못했고, 배열을 이용해야 하나 싶었는데 아니었네요
# 진짜 다해본다는 생각을 못해서 못 풀었던 것 같습니다.
# 시간복잡도를 생각해보고 시간초과가 절대 나지 않는다고 생각된다면 바로 완탐으로 풀기!

H,W = map(int,input().split())
N = int(input())
sticker = [list(map(int,input().split())) for _ in range(N)]
sticker.sort(key = lambda x:-(x[0]*x[1]))
result=0
for i in range(N):
    for j in range(i+1,N):
        r1,c1 = sticker[i]
        r2,c2 = sticker[j]

        if (r1+r2 <= H and max(c1,c2)<= W) or (max(r1,r2) <= H and c1 +c2 <=W):
            result = max(result,r1*c1 + r2*c2)
        if (c1+r2 <=H and max(r1,c2)<=W) or (max(c1,r2) <= H and r1+c2 <=W):
            result = max(result,r1*c1 + r2*c2)
        if (c1+c2 <=H and max(r1,r2)<=W) or (max(c1,c2) <= H and r1+r2 <=W):
            result = max(result,r1*c1 + r2*c2)
        if (r1+c2 <=H and max(r2,c1)<=W) or (max(c2,r1) <= H and r2+c1 <=W):
            result = max(result,r1*c1 + r2*c2)
print(result)