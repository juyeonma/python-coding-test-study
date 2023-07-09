'''
# 백준_15663_N과 M (9).py. 실버 2. 풀이: 23.07.05

# How to
N과 M (1)과는 다르게 수가 중복해서 주어졌다.
같은 수가 중복해서 들어있는 경우, 각각 다른 수로 취급 된다.
그렇지만 한 수열 안에서는 같은 수가 존재할 수 없다.


# Review
- N과 M (1)에서 각 수가 문자형인 상태에서 join로 출력한걸 따라했는데, 틀렸다.
    - 문자형인 상태로 순열을 구한 후 set으로 중복 제거 후 정렬이 원인이었다.
- 그래서 우선 정수형으로 받고, 순열을 구한 후 set 이후 다시 정렬된 리스트로 만들고, 각각의 수를 문자형으로 바꾸었더니 성공했다.
- 문제는 '백트래킹' 유형인데, 그냥 정렬해서 풀었다는것이다.. 
    - 다른 사람 풀이를 보니, 다들 dfs로 풀었다.
    - 그동안 그래프 탐색에서의 dfs에 익숙했는데, 백트래킹에서의 dfs 코드는 뭔가 어색하다..
    - 백트래킹으로 다시 풀어봐야겠다.
'''

# 1. 실패 Code
from itertools import permutations
n, m = map(int, input().split())
num = input().split()

print('\n'.join(map(' '.join, sorted(set(permutations(num, m))))))


# 2. 성공
from itertools import permutations
n, m = map(int, input().split())
num = map(int, input().split())
answer = map(lambda x: map(str, x), sorted(set(permutations(num, m))))

print('\n'.join(map(' '.join, answer)))

'''
# 만약 asterisk 사용하면: 108 ms
for i in sorted(set(permutations(num, m))):
    print(*i)
'''

# 3. 백트래킹으로 다시 풀어보기

'''
# Result
풀이 시간: 20분
메모리: 35868 KB
시간: 80 ms
코드 길이: 211 B
'''