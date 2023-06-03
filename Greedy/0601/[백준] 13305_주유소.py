# 처음위치에서는 해당 위치의 주유비를 무조건 지불해야한다. 
# 그 주유비 * 다음위치까지의 거리를 cost 변수에 담고 그 다음위치의 주유비와 그 이전의 주유비를 비교해서 더적은 주유비를 골라서 그 다음 거리만큼 또곱해준다
# 마지막 위치의 도시는 도착지점이기 때문에 주유비가 의미가 없다
# 

n = int(input()) # 도시의 개수
d = list(map(int,input().split())) # 각 도시 사이의 거리
city_cost= list(map(int,input().split())) # 각 도시별 주유비 
cost = 0  # 각 도시를 지나면서 드는 총 주유비
min_city_cost=2e9 # 최소 주유비를 담을 변수, 먼저 최대값으로 초기화
for i in range(n-1):  #마지막 도시의 주유비는 알 필요 없으므로 그 이전까지 for문 돌리기
    min_city_cost=min(min_city_cost,city_cost[i]) #각 도시에 도착했을 때의 최소 주유비 갱신
    cost+=min_city_cost*d[i]  # 최소 주유비 x 다음 도시까지의 거리
print(cost)

# 풀이시간 12분
# 메모리 46584KB 시간 124ms

