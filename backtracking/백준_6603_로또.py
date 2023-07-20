'''
# 백준_6603_로또. 실버 2. 풀이: 23.07.12

# How to
- kC6 구하기
- 조합 라이브러리를 사용하거나, 백트래킹으로 구현하기.

# Review
- 풀이 시간: 30분
- itertools 라이브러리가 제일 간편하고 편하다.
- 그런데 명색이 백트래킹 유형이니까, 직접 구현해봤다. 
    - 조합인 만큼 중복을 방지하기 위해 다음 인덱스부터 탐색하는게 포인트였다.
'''

# Code
# 1. itertools 라이브러리 사용: 성공
## 메모리: ms31256 KB, 시간: 44 ms
from itertools import combinations
import sys
input = sys.stdin.readline
while True:
    k, *s = map(int, input().split())
    if k == 0:
        break
    
    for i in combinations(s, 6):
        print(*i)
    print()

'''
# 만약 문자열로 하면,
k, *s = input().rstrip().split()
print(' '.join(i))
'''


# 2. 직접 조합 구현하기: 성공
# 원래 visited로 매번 체크했는데, 어짜피 다음 인덱스 부터 탐색하기 때문에 빼도 성공.
import sys
input = sys.stdin.readline

def backtracking_combi(combi, idx):
    # 6개 조합 다 구했으면, 출력 후 return
    if len(combi) == 6:
        print(*combi)
        return
    
    # 조합이므로, 중복을 방지하기 위해 다음 인덱스부터 탐색
    # 만약 순열이었다면, 매번 인덱스 0부터 시작해야함.
    for i in range(idx+1, k):
        backtracking_combi(combi+[s[i]], i)

while True:
    k, *s = map(int, input().split())
    
    if k == 0:
        break

    # 인덱스 0부터 시작하기 위해서, -1을 넣어줌
    backtracking_combi([], -1)
    print()