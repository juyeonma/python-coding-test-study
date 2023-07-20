'''
# 백준_15663_N과 M (9).py. 실버 2. 풀이: 23.07.05

# How to
## 2. 라이브러리 사용
N과 M (1)과는 다르게 수가 중복해서 주어졌다.
같은 수가 중복해서 들어있는 경우, 각각 다른 수로 취급 된다.
그렇지만 한 수열 안에서는 같은 수가 존재할 수 없다.

## 3. 직접 구현
- 중복 안됨
    - visited를 사용하여 매번 중복 체크
- 수열 내에서 순서 제약이 없음
    - 매번 0 인덱스부터 탐색
- 수열은 사전 순으로 증가하는 순서로 출력
    - 오름차순 출력
    - 처음에 int 형으로 입력 받아서 sort 후, 다시 str로 변환
=> 순열이긴 한데, 중복된 수가 존재하는 순열.

- 입력으로 똑같은 수가 주어질 수 있음
    - 두 가지 방법 가능
    - 3-1. 매번 정답을 set에 추가 후 중복 제거하여 한꺼번에 출력
    - 3-2. overlap을 활용하여, 한 재귀 내에서 동일한 값이 중복 사용되는걸 방지
        - 출처: https://aigong.tistory.com/484
        
        
# Review
- N과 M (1)에서 각 수가 문자형인 상태에서 join로 출력한걸 따라했는데, 틀렸다.
    - 문자형인 상태로 순열을 구한 후 set으로 중복 제거 후 정렬이 원인이었다.
- 그래서 우선 정수형으로 받고, 순열을 구한 후 set 이후 다시 정렬된 리스트로 만들고, 각각의 수를 문자형으로 바꾸었더니 성공했다.
- 문제는 '백트래킹' 유형인데, 그냥 정렬해서 풀었다는것이다.. 
    - 다른 사람 풀이를 보니, 다들 dfs로 풀었다.
    - 그동안 그래프 탐색에서의 dfs에 익숙했는데, 백트래킹에서의 dfs 코드는 뭔가 어색하다..
    - 백트래킹으로 다시 풀어봐야겠다.
    
- 23.07.14: 직접 순열을 구현해보니, "입력으로 똑같은 수가 주어진다"는 조건이 까다로웠다.
    - 결국 set을 하나 만들어서 해결.(3-1)
    - 그런데 찾아보니 변수를 하나 만들어서 해결하는게 더 빨랐다.(3-2)
        - 출처: https://aigong.tistory.com/484
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

'''
# Result
풀이 시간: 20분
메모리: 35868 KB
시간: 80 ms
코드 길이: 211 B
'''


# 3. 백트래킹으로 다시 풀어보기 23.07.14
# 3-1. answer 이라는 set 사용하여 입력에 중복 값이 들어오는 조건 해결
## 35868 KB 132 ms
n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
visited = [False] * n
answer = set()
def backtracking_permutation(result):
    if len(result) == m:
        # set에 추가
        answer.add(tuple(result))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            backtracking_permutation(result+[nums[i]])
            visited[i] = False
            
backtracking_permutation([])

# 중복을 제거하고, 정렬된 list로 만든 후 오름차순으로 출력
for i in sorted(answer):
    print(*i)


# 3-2. overlap 변수 사용
## 31256 KB 68 ms
n, m = map(int, input().split())
nums = list(map(str, sorted(map(int, input().split()))))
visited = [False] * n

def backtracking_permutation(result):
    if len(result) == m:
        print(' '.join(result))
        return
    
    overlap = 0
    for i in range(n):
        # 이전에 overlap에 담긴 값일 경우, 
        if not visited[i] and overlap != nums[i]:
            visited[i] = True
            # 여기서 overlap에 값을 담아주면, 
            overlap = nums[i]
            backtracking_permutation(result+[nums[i]])
            visited[i] = False
            
backtracking_permutation([])
