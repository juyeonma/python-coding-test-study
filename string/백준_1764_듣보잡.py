'''
# 백준_1764_듣보잡. 실버 4. 풀이: 23.06.27

# How to
## 1. 
- set을 사용해서, 먼저 듣도 못한 사람의 명단을 저장한다
- 보도 못한 사람을 입력 받으면서, 이 사람이 듣도 못한 사람일 경우, 정답에 추가한다.
- 정렬 후 출력

## 2. set 교집합 사용
- 정답 명단 = 듣도 못한 사람 set & 보도 못한 사람 set 

# Review
'''

# Code
# 1. 보도 못한 사람 중 듣도 못한 사람 찾기: 성공
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

check = set()
answer = []

# 듣도 못한 사람의 명단
for _ in range(n):
    check.add(input().rstrip())

# 보도 못한 사람이면서 듣도 못한 사람일 경우, 정답에 추가
for _ in range(m):
    name = input().rstrip()
    if name in check:
        answer.append(name)
        
print(len(answer))
for i in sorted(answer):
    print(i)


# 2. set 교집합 사용: 성공
## 44060 KB, 88 ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

no_hear = set(input().rstrip() for _ in range(n))
no_see = set(input().rstrip() for _ in range(m))

# 교집합: 듣도 & 보도 못한 사람
answer = no_hear & no_see

print(len(answer))
for i in sorted(answer):
    print(i)
    
'''
# Result
풀이 시간: 10분
메모리: 37400 KB
시간: 84 ms
코드 길이: 313 B
'''