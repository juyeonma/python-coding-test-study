# 못풀었다. 실은 아이디어 생각은했는데 진짜 이렇게 다 해봐야된다고?라는생각이 들어서 못했다..
# 근데 원래 생각한대로 풀었어도 헤맸을 것같긴하다 왜나하면 두 구역으로 나눌때 값을 하나씩만 넣어도 되는데 두군데를 나눠서 한번에 큐에 넣으려고했다
# 이렇게 해도 되겠지만 이런방식으로 풀면 1구역과 나머지구역으로 나누는 경우를 따로 구해야한다. 조합을 구할 때 1개만 뽑는 경우에는 (1,),(2,)이런식으로나오기때문에..
# bfs는 나름 자신있었는데 이렇게 노드형식으로 된 bfs는 아직 약한것같다.
# 진짜 실전인것처럼 푸는것자체에 집중해보려고 노력해봐야겠다. 요즘 너무 정신이 헤이해진 기분이다..정신차리자..

# 주연님 풀이를 참고해서 풀었다. 문법에 대한 여러가지 부분을 배울 수 있었다.


from itertools import combinations
from collections import deque

# 조합을 이용해서 1부터  n//2까지 구하기 > 그이상의 수는 그 이전의 수 조합을 통해 다 구해지기때문에
# 구역을 둘로 나누어서 bfs돌리기
# bfs 둘 다 참이면 차이 구하기
# bfs에 vis배열 만들기 방문한 곳은 continue
# 방문안했는데 나눠진구역의 노드가 아니면 continue
# 나눠진 구역의 노드인데 방문안했으면 vis처리해주고 queue에 넣기
# vis 트루인부분과 구역이 같다면 참
# 나눈 두 구역이 모두 참이면 조합부분에서 합을 구하고 전체에서 그 합을 뺀값을 빼기 > 최소값으로 갱신

N = int(input())
population = [0] + list(map(int,input().split()))
poplation_sum = sum(population)

network={}
area = set(range(1,N+1))
min_diff=2e9

for i in range(1,N+1):
    if i not in network:
        network[i]=[]
    area_info =list(map(int,input().split()))[1:]
    for j in area_info:
        network[i].append(j)

def bfs(arr):
    queue=deque([arr[0]])
    vis=[0 for _ in range(N+1)]
    vis[arr[0]]=1
    while queue:
        cur_pos=queue.popleft()
        for i in network[cur_pos]:
            if vis[i]:
                continue
            if not vis[i] and i not in arr:
                continue
            vis[i]=1
            queue.append(i)
    
    if vis.count(1)==len(arr):
        return True
    else:
        return False

def diff(arr):
    s=0
    for i in arr:
        s+=population[i]
    return abs(poplation_sum-2*s)
        
for i in range(1,N//2+1):
    c=combinations(range(1,N+1),i)
    for area1 in c:
        area2=[j for j in range(1,N+1) if j not in area1]
        if not bfs(area1) or not bfs(area2):
            continue
        
        min_diff= min(min_diff,diff(area1))

if min_diff==int(2e9):
    print(-1)
else:
    print(min_diff)