'''
# 백준_13975_파일 합치기 3. 골드 4. 풀이: 23.06.01

# How to
- 먼저 더한 것은 계속 누적해서 더해진다. 그러므로 작은걸 먼저 더하고, 큰걸 나중에 더하자.
- 즉, 매번 작은 것까리 더한다.
- 우선 순위 큐를 사용.
    - 가장 작은 파일 2개를 뽑아서 합치고, 정답에 누적한 후 큐에 넣는다.
- 모든 파일을 합치고 나면, 정답 출력.

## 예제
30 30 40 50

30+30 = 60 -> 60 40 50
40+50 = 90 -> 60 90
60+90 = 150
답: 60+90+150 = 300

# Review
- 이코테에서 유사한 문제를 푼적이 있다.
'''

# 성공 Code
import heapq

# sys를 사용하면, 메모리가 더 늘고 속도가 느려졌다.: 154588 KB 5328 ms
# import sys
# input = sys.stdin.readline

def solve(n):
    answer = 0
    q = list(map(int, input().split()))
    heapq.heapify(q)
    
    # 2개씩 더해야하므로, 적어도 파일이 2개는 남아야한다.
    while len(q) >= 2:
        # 가장 작은 파일 2개를 뽑아서 합침
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        a += b
        # 정답에 누적
        answer += a
        # 큐에 넣음(남은 파일들과 합쳐야하니까)
        heapq.heappush(q, a)
    
    return answer

for _ in range(int(input())):
    print(solve(int(input())))

'''
# Result
풀이 시간: 20분
메모리: 152744 KB
시간: 4984 ms
코드 길이: 333 B
'''