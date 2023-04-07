h,w = map(int, input().split())

block=list(map(int, input().split()))

cnt=0

for i in range(1,w-1):
    left=max(block[:i]) #i값을 기준으로 좌우 최대값 저장
    right=max(block[i+1:])
    m = min(left, right) #그것중에 작은 값저장
    
    if m>block[i]: #조건을 만족하면 빗물이 고임
        cnt+=m-block[i] # 벽 높이에다가 바닥 높이를 뺌

print(cnt)