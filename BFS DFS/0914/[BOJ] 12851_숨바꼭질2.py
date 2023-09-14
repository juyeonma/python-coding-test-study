# bfs 풀이 : 참고 봤습니다....ㅠㅠ..
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
queue = deque()
queue.append(n)
way = [0] * 100001 # 0 ≤ N ≤ 100,000 이므로 최대크기로 초기화
cnt, result = 0, 0
while queue:
    a = queue.popleft()
    temp = way[a]
    if a == k: # k에 값이 도달하면
        result = temp
        cnt += 1 # 방문횟수
        continue
    
    for i in [a-1, a+1, a*2]:
        if 0 <= i < 100001 and (way[i] == 0 or way[i] == way[a] + 1):
            # 방문하지 않거나, 다음 방문이 이전 방문+1이면
            way[i] = way[a] + 1
            queue.append(i)

print(result)
print(cnt)