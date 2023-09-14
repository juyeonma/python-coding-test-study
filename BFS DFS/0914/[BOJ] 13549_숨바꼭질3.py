# 참고 좀 봤습니다....ㅠㅠ..
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
q = deque()
q.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
    s = q.popleft()
    if s == k:
        print(visited[s])
        break
    if 0 <= s-1 < 100001 and visited[s-1] == -1:
        visited[s-1] = visited[s] + 1
        q.append(s-1)
    if 0 < s*2 < 100001 and visited[s*2] == -1:
        visited[s*2] = visited[s]
        q.appendleft(s*2) # 0초 이기 때문에
    if 0 <= s+1 < 100001 and visited[s+1] == -1:
        visited[s+1] = visited[s] + 1
        q.append(s+1)

# appenleft를 좀 생각해두었다면 생각보다.. 숨바꼭질2 보다는 쉬운 문제가 아니었을까..싶었던 문제
# 숨바꼭질2을 이해하는데 좀 시간이 걸렸다면 비슷해서 바로 이해가 되었다..