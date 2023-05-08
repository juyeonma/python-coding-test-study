'''
# 백준_14889_스타트와 링크. 실버 2. 풀이: 23.04.26

# 풀이방법
- 백트래킹(DFS를 이용), 조합 두가지 방법이 존재.
- 여기서는 조합을 이용
    - 1) 조합을 이용할 때, 팀 구성 조합을 탐색하며 매번 능력치를 더해서 최솟값 갱신하는 방법과
    - 2) 미리 행과 열의 합을 구해놓고 조합대로 최솟값 갱신하여 훨씬 빠른 방법이 존재.

- 1)번 조합
    - 1. 가능한 팀 구성의 조합을 list로 구한다.
    - 2. i번째 팀의 여집합 = -i-1번째 팀 (한 팀이 정해지면 나머지 팀은 자동임)
    - 3. 같은 팀 내에서도 2명씩 조합해서 능력치를 구한다.

- 2)번 조합
    - 아이디어: 동일 index는 행과 열 각각 덧셈을 해야함. 
S: 스타트팀 능력치 -> 스타트팀 행과 열의 합 = S + S + R
L: 링크팀 능력치 -> 링크팀 행과 열의 합 = L + L + R
R: 나머지 능력치

T: 전체 능력치 = S + L + R

따라서,
전체 능력치 - 스타트팀 행렬 덧셈 
= (S + L + R) - (S + S + R)
= L - S
= 링크팀 능력치와 스타트팀 능력치의 차이

    - 1. 행끼리 합과 열끼리 합을 각각 list로 구한다
    - 2. 전체 합
    - 3. 동일 index의 행과 열의 합을 구한다. (= 팀원별 능력치의 합)
    - 4. 팀 구성 조합을 구하고, 하나씩 탐색한다.
    - 5. 전체 합 - 팀원 능력치 합
'''


# 1)번 조합 code
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]

# 1. 가능한 팀 구성의 조합을 list로 구한다.
comb = list(combinations(range(n), n//2))

answer = 1e9
    
# 3. 같은 팀 내에서도 2명씩 조합해서 능력치를 구한다.
# i와 j의 능력치 = i행 j열의 능력치 + j행 i열의 능력치
def sum_power(idx):
    result = 0
    for a, b in list(combinations(comb[idx], 2)):
        result += power[a][b] + power[b][a]
    return result

# 2. i번째 팀의 여집합 = -i-1번째 팀 -> 따라서 1번 조합의 반절만 탐색한다.
for i in range(len(comb)//2):
    answer = min(answer, abs(sum_power(i) - sum_power(-i-1)))

print(answer)


# 2)번 조합 code
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]

# 1. 행끼리 합과 열끼리 합을 각각 list로 구한다
sum_row = [sum(i) for i in power]
sum_col = [sum(i) for i in zip(*power)]

# 2. 전체 합
sum_total = sum(sum_row)

# 3. 동일 index의 행과 열의 합을 구한다. (= 팀원별 능력치의 합)
# 어짜피 행과 열을 모두 더해야하므로, 미리 더해놓는것.
# 이때 list의 길이는 n과 같다.
sum_same_index = [i+j for i, j in zip(sum_row, sum_col)]

answer = 1e9
# 4. 팀 구성 조합을 구하고, 하나씩 탐색한다.
# 한 팀이 결정되면, 나머지 팀은 자동으로 결정됨. 따라서 n의 반절만 탐색해도 된다.
for i in combinations(sum_same_index, n//2):
    # 5. 전체 합 - 팀원 능력치 합
    # min이 더 코드가 짧지만, if로 크기 비교 후 answer 갱신이 쪼끔 더 빠르다!
    # answer = min(answer, abs(sum_total - sum(i)))
    tmp = abs(sum_total - sum(i))
    if tmp < answer:
        answer = tmp
    
print(answer)

'''
# 결과: 1)번 코드 -> 2)번 코드 개선
메모리: 56392 KB -> 31256 KB
시간: 1124 ms -> 116 ms
코드 길이: 467 B -> 599 B
'''