import heapq
n = int(input())
graph = [[*map(int, input().split())] for _ in range(n)]
graph.sort()

# 여기까지 풀고.. 한시간 이상 고민해봤는데 안풀렸다..
# heapq 를 사용한다면 어떻게 사용해야할지 몰랐는데(빼는 방법만 계속 생각했던 것 같다..)
# 오히려 추가해서 방의 길이를 통해서 구하는 방법이었다..
# 참고 : https://hongcoding.tistory.com/79
room = []
heapq.heappush(room, graph[0][1])

for i in range(1, n):
    if graph[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
        heapq.heappush(room, graph[i][1]) # 새로운 회의실 개설
    else:# 현재 회의실에 이어서 회의 개최 가능
        heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop 후 새 시간 push
        heapq.heappush(room, graph[i][1])

print(len(room))
