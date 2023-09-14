# 진짜 다 잊었어요.... 죄송합니다...ㅠㅠㅠㅠ....... 주석달아서 달달 외우기라도 할게여..
import sys
input = sys.stdin.readline;

n = int(input());
graph = [list(map(int, input().split())) for _ in range(n)]

# 플로이드-워셜 알고리즘 => 모든 최단 경로를 구하는 알고리즘
for i in range(n):
    # 이중 for문으로 각 노드별 모든 통로를 살핌
    for j in range(n):
        for k in range(n):
            # 갈 수 잇는 경로인지 체크
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for g in graph:
    print(*g)
    
# 메모리 : 31256, 시간 : 212