from itertools import combinations
n,m = map(int, input().split())
chicken, house=[],[] 

for i in range(n):
    data=list(map(int, input().split()))
    for j in range(n):
        if data[j]==1:
            house.append((i,j))
        if data[j]==2:
            chicken.append((i,j))
            
can=list(combinations(chicken,m)) #치킨집 m개의 조합을 모두 구하는 함수

def get_sum(cand):
    result=0
    for hx, hy in house: #집과 치킨집의 거리를 모두 계산
        temp=1e9
        for cx,cy in cand:
            temp=min(temp, abs(hx-cx)+abs(hy-cy))
        result+=temp #최소 거리를 모두 더함
    return result

result=1e9
for i in can:
    result=min(result,get_sum(i))
print(result)

#코드길이 726b
#시간 372ms