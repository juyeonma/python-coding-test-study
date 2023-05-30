'''
# 백준_13305_주유소. 실버 3. 풀이: 23.05.30

# How to
2번 Code
- 기준 인덱스와 그 이후를 차례대로 기름값을 비교한다.
- 기름값이 같거나 다음 기름값이 더 싼 경우, 정답에 거리*기름값을 더해줌
- 기준이 되는 인덱스를 갱신

# Review
- 서브테스크는 처음이라 당황했는데, 결국 문제의 조건을 다 지키면 100점이 나오는거였다.
- 기름값은 n개이지만 거리는 n-1개라는걸 유의해야했다.
- 결국 기준 인덱스를 고정한 채 인덱스를 증가시키며 기름값을 비교하는게 핵심이었다.
    - while문으로 범위 내에서 반복했는데,
    - 맞힌 사람을 보니까(3번 Code) 그냥 for문을 썼는데, 이게 더 직관적이고 간편하며 빠른 코드였다.
        - 더 싼 기름값일 경우에만 기준 인덱스를 갱신하고, 매번 거리*기준 기름값을 더한다.

'''

# 1. 17점 부분성공: 42684 KB 124 ms -> 나머지 런타임 에러
# index 설정 범위에서 문제: next의 범위가 초과되는걸 고려하지 않았다.
import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

answer = 0
now, next = 0, 1

while now < n-1:
    answer += road[now] * oil[now]
    
    while oil[now] < oil[next]:
        answer += road[next] * oil[now]
        next += 1
    else:
        now = next
        next += 1
    
print(answer)


# 2. 100점 성공: 46076 KB 156 ms
import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

answer = 0
now, next = 0, 1

while now < n-1:   
    while next < n and oil[now] < oil[next]:
        next += 1
    else:
        answer += sum(road[now:next]) * oil[now]
        now = next
        next += 1
    
print(answer)


# 3. 모범 답안(맞힌 사람): 100점: 46384 KB 108 ms
import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_oil = oil[0]
answer = 0

for i in range(n-1):
    # min 함수를 써도 되지만, 더 느림: 128 ms
    # min_oil = min(min_oil, oil[i])
    if oil[i] < min_oil:
        min_oil = oil[i]
    answer += road[i] * min_oil
    
print(answer)


'''
# Result
풀이 시간: 30분
메모리: 46076 KB
시간: 156 ms
코드 길이: 360 B
'''