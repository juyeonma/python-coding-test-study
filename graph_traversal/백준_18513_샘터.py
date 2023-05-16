'''
# 백준_18513_샘터. 골드 4. 풀이: 23.05.14 -> 실패

# How to
- 불행도: 가장 가까운 샘터까지의 거리
## 방법 1: 시간 초과
- 샘터 사이의 거리를 측정하여 그만큼 집을 넣는다는 개념으로 접근
- 그러나, 매번 샘터사이의 거리를 측정하고, 나누고 등의 계산이 들어가서 그런지 시간 초과

## 방법 2: 메모리 초과
- bfs로 풀었으나..
- 샘터로부터의 거리, 집의 갯수, 누적된 정답의 3개의 변수를 계속 구함.
- 정해진 집의 갯수가 되면, 정답을 반환.
- 그러나 방문 체크용 리스트에서 메모리가 초과하는지, 아니면 bfs에서 무한루프에 걸렸는지, 여튼 메모리 초과.

# Review
'''
# Code 2: 메모리 초과
from collections import deque
import sys
input = sys.stdin.readline

# 샘터 갯수, 집 갯수
n, k = map(int, input().split())
saem = sorted(list(map(int, input().split())))

# 메모리 초과를 위해 적당한 길이로 하려 했으나..실패
if saem[0] < 0:
    a = saem[0]+k+1
else:
    a = k+1
    
if saem[-1] >= 0:
    b = saem[-1]+k
else:
    b = k
    
# 방문 체크
visit_plus = [0] * a
visit_minus = [0] * b

def bfs(q, cnt, answer):
    while q:
        x = q.popleft()
        
        # 샘터로부터의 거리
        if 0 <= x:
            d = visit_plus[x]
        else:
            d = visit_minus[-x]
        # 정답을 누적
        answer += d
        # 집의 갯수
        cnt += 1
        if cnt == k:
            return answer
        
        for i in [1, -1]:
            nx = x + i
            # 샘터라면, continue
            if nx in saem:
                continue
            # 지금 집의 위치가 양수인지 음수인지
            if 0 <= nx:
                if visit_plus[nx] == 0:
                    visit_plus[nx] = d+1
                    q.append(nx)
            else:
                if visit_minus[-nx] == 0:
                    visit_minus[-nx] = d+1
                    q.append(nx)


print(bfs(deque(saem), -n, 0))


# Code 1: 시간초과
import sys
input = sys.stdin.readline

# 샘터 갯수, 집 갯수
n, k = map(int, input().split())
saem = sorted(list(map(int, input().split())))
dic = dict(zip(list(range(1, k+1)), [0]*k)) 
    
# 샘터 사이의 거리를 반으로 나눔 -> 그만큼 겹치지 않게 집을 넣을 수 있음
for i in range(n-1):
    tmp = saem[i+1] - saem[i] - 1
    a = tmp // 2
    b = tmp % 2
    
    if a:
        for j in range(1, min(a, k)+1):
            dic[j] += 2
    if b:
        for j in range(1, min(a+b, k)+1):
            dic[j] += 1
        
for i in range(1, k+1):
    dic[i] += 2
    
answer = 0
# 차근차근 집의 갯수를 줄여가며, 정답을 누적
for i in range(1, k+1):
    if k >= dic[i]:
        k -= dic[i]
        answer += i*dic[i]
    else:
        answer += i*k
        break

print(answer)

'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''