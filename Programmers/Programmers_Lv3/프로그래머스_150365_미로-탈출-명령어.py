'''
# 프로그래머스_150365_미로 탈출 명령어. Lv 3. 풀이: 23.06.16 -> 실패 -> 성공

# How to
- BFS 풀이
- 핵심은, 매번 '도착할 수 없는 거리'인지 체크하는것
- 먼저 k번 안에 도착할 수 없는 거리 or 도착할 수 없다면(홀짝이 안맞아서), 실패
    - 홀짝이 안 맞는다는건, k와 출발지~도착지 거리가 홀수면 홀수, 짝수면 짝수여야 한다는것.
- 큐에 넣을때, 사전순으로 앞선 문자열을 뽑아야하므로, 경로 문자열이 맨 앞에 들어감
- 매번 아래, 왼쪽, 오른쪽, 위 순서대로 이동하면서 경로 문자열에 추가하고, 큐에 넣음
    - 이때, 도착할 수 없는 거리인지 체크
    - 남은 거리가 0이라면, 도착지인지 판단 후 return
    - 큐에 넣을 때, 처음 k에서 길이가 1개씩 줄어야함. 즉 깊이가 1 증가하는 개념.


# Review
- DFS로 풀다가, 결국 힌트에서 BFS라는 것을 본 후 풀이 성공
- 특히 BFS 내부에서 남은 문자열 길이가 남은 거리보다 짧은 경우, 즉 너무 많은 거리가 남은 경우를 체크하는게 핵심이었다.
'''


# 1. DFS: 실패
def dfs(n, m, x, y, r, c, k, result, depth):
    # 범위에서 벗어나면, return
    if x < 0 or y < 0 or n <= x or m <= y:
        return False
    
    # k개를 탐색했다면, 도착지인지 따진 후 return
    if depth == k:
        if (x, y) == (r, c):
            return result
        else:
            return False
    
    # d l r u 순서로 우선순위를 지닌다.
    d = dfs(n, m, x+1, y, r, c, k, result+'d', depth+1)
    l = dfs(n, m, x, y-1, r, c, k, result+'l', depth+1)
    r = dfs(n, m, x, y+1, r, c, k, result+'r', depth+1)
    u = dfs(n, m, x-1, y, r, c, k, result+'u', depth+1)

    if d:
        return d
    elif l:
        return l
    elif r:
        return r
    elif u:
        return r
    else:
        return False
#     answer = [i for i in [d, l, r, u] if i]

#     if answer:
#         return min(answer)
#     else:
#         return False
    
def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    
    # 홀수+홀수 = 짝수, 짝수+짝수 = 짝수
    len1 = abs(x-r) + abs(y-c)
    if (k - len1) % 2:
        return answer
    
    answer = dfs(n, m, x-1, y-1, r-1, c-1, k, '', 0)
    
    if answer:
        return answer
    else:
        return 'impossible'


# 2. BFS: 성공
# 테스트 19 〉	통과 (28.27ms, 14.8MB)
import heapq

def bfs(n, m, r, c, q):
    while q:
        s, depth, x, y = heapq.heappop(q)
            
        # 방향 설정: 아래, 왼쪽, 오른쪽, 위 순서대로 이동
        dic = {'d': [1, 0], 'l': [0, -1], 'r': [0, 1], 'u': [-1, 0]}
        for i in dic:
            nx = x + dic[i][0]
            ny = y + dic[i][1]
            
            if nx < 0 or ny < 0 or n <= nx or m <= ny:
                continue
                
            ndepth = depth-1
            left_len = abs(nx-r)+abs(ny-c)
            
            # 남은 거리가 너무 많거나 or 도착할 수 없다면(홀짝이 안맞아서)
            if ndepth < left_len or (ndepth - left_len) % 2:
                continue
                
            # 남은 거리가 0이라면, 도착지인지 판단 후 return
            if not ndepth:
                if (nx, ny) == (r, c):
                    return s+i
                continue
           
            # 계속 이동해야 하므로, q에 추가
            heapq.heappush(q, (s+i, ndepth, nx, ny))

    return "impossible"


def solution(n, m, x, y, r, c, k):
    left_len = abs(x-r)+abs(y-c)
    # k번 안에 도착할 수 없는 거리 or 도착할 수 없다면(홀짝이 안맞아서), 실패
    if k < left_len or (k - left_len) % 2:
        return "impossible"
    
    # 사전순으로 앞선 문자열을 뽑아야하므로, 경로 문자열이 맨 앞에 들어감
    q = [('', k, x-1, y-1)]
    heapq.heapify(q)

    return bfs(n, m, r-1, c-1, q)


# 다른 사람 풀이
## 도착지점이 출발지점보다 위 아래 왼쪽 오른쪽 중 어느 방향인지를 따져서 이동
def solution(n, m, x, y, r, c, k):
    answer = ''
    #x,y -> r,c 
    #좌상단이 1,1/ 우하단이 n,m
    #세로,가로  -> 2.3이 S
    diff = abs(x-r)+abs(y-c)
    if diff%2!=k%2 or diff>k:
        return 'impossible'
    #dlru 순서 

    rest = k-diff
    lcount = 0
    rcount = 0
    dcount = 0
    ucount = 0
    if x<r : #내려가야함
        dcount = r-x
    else:
        ucount = x-r
    if y<c :
        rcount = c-y
    else:
        lcount = y-c

    dplus = min( n-max(x,r), rest//2)
    rest -= dplus*2

    lplus = min( min(y,c)-1, rest//2)
    rest -= lplus*2

    answer = 'd'*(dcount+dplus)+'l'*(lcount+lplus)+'rl'*(rest//2)+'r'*(rcount+lplus)+'u'*(dplus+ucount)
    print(lcount,lplus,rcount,rest)

    return answer


'''
# Result
풀이 시간: 실패(+ 30분)

'''