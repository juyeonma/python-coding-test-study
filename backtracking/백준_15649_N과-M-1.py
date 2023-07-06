'''
# 백준_15649_N과 M (1). 실버 3. 풀이: 23.07.05

# How to
- 1부터 n까지 자연수 중에서 중복없이 길이가 m인 수열 구하기
- 순열을 이용한다.

# Review
- 단순히 순열 라이브러리를 이용하면 되는 문제였다.
- 다만 다른 사람 풀이를 보니 속도가 배로 빨랐는데, 공백을 join으로 처리했기 때문이다.
    - 즉 처음부터 int가 아닌 str로 변환하여 자연수 목록을 만들고,
    - 각 수열을 join으로 공백을 넣어서 만들고,
    - 그 수열들을 다시 join으로 줄바꿈을 넣어 출력했다.
'''

# 성공 Code
from itertools import permutations
n, m = map(int, input().split())

for i in permutations(range(1, n+1), m):
    print(*i)


# 다른 사람 풀이: 44 ms
from itertools import permutations
N, M = map(int, input().split())
print('\n'.join(list(map(' '.join, permutations(map(str, range(1, N+1)), M)))))


'''
# Result
풀이 시간: 10분
메모리: 31256 KB
시간: 152 ms
코드 길이: 123 B
'''