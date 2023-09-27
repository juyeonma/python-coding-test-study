'''
# 백준_12851_숨바꼭질2. 골드 4. 풀이: 23.09.15 -> 실패

# How to
- BFS
- 걷거나 or 순간이동 하면서
    - 더 낮은 시간이면, 시간 갱신 및 큐에 추가
    - 이미 최저 시간이면, 경우의 수 +1

## 예제
5 17
10 9 18 17 => 4초
10 20 19 18 17 => 4초

## 반례
5 237
답: 
10
5

# Review
- 풀이 시간: 2시간..
- 반례찾느라 시간 다보냈다. 결국 질문게시판을 봤는데, 역시 반례에서 틀렸더라.
- 도저히 왜 틀렸는지 모르겠다 ㅠㅠ
    - 방문처리 및 정답 기록을 딕셔너리로 했는데, 이게 아닌가..?
    - 숨바꼭질3는 맞았는데 숨바꼭질2는 틀린걸 보면, 경우의 수를 세는게 문제같다.
'''

# Code
# 1. BFS: 40%에서 실패
## 메모리:  KB, 시간:  ms
from collections import deque
n, k = map(int, input().split())

# 수빈이의 위치별 시간과 경우의 수 딕셔너리
subin = {n: [0, 1]}

def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == k:
            continue
        
        # 걷거나 순간이동 하면서
        for nx in [x+1, x-1, 2*x]:
            if 0 <= nx <= 100_000:
                # 새로운 위치이거나 더 낮은 시간이면, 시간 갱신 및 큐에 추가
                if nx not in subin or subin[x][0]+1 < subin[nx][0]:
                    subin[nx] = [subin[x][0]+1, subin[x][1]]
                    q.append(nx)
                    
                # 이미 최저 시간이면, 경우의 수 +1
                elif subin[x][0]+1 == subin[nx][0]:
                    subin[nx][1] += 1
                    
bfs(n)
print(subin[k], sep='\n')
