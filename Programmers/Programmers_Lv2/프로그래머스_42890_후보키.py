'''
# 프로그래머스_42890_후보키. Lv 2. 풀이: 23.06.21

# How to

## 1.
- combinations을 이용해서 columns의 가능한 조합을 찾는다.
    - 점차 개수를 늘려가면서 조합을 구한다.
- 최소성(기존 후보키가 포함되지 않았는지)과 유일성(원래 배열의 개수가 같은지)을 확인한다.
    - 후보키라면, 정답 +1, 후보키에 추가

## 2.
- 1번과 같은 방법인데, 다만 유일성과 최소성을 별도의 함수로 만들었다.


# Review
- 처음에 column들의 중복을 어떻게 확인할지 고민했다. 또한 set 만들 때, list로 했더니 오류가 나서 tuple로 바꾸니까 잘 되었다. 왜지?
- 결국 set을 이용해서, 차집합으로 풀어냈다.
- 다른 사람 풀이를 보니,
    - 비트연산을 사용한 사람이 있었다. 나중에 이해해야지..
    - 차집합 대신에 issubset으로 부분집합인지 판단하길래, 이 함수를 이용해봤다. 
    유일성과 최소성도 별도의 함수로 만들어보니, 훨씬 깔끔한 코드가 되었다.
- 집합을 잘 사용하는게 중요한 문제였다.
'''

# 1. 성공 Code
## 합계: 46.4 / 100.0 -> 차집합 추가 후: 테스트 22 〉통과 (3.32ms, 10.2MB)
from itertools import combinations
def combi(relation, n, idx):
    arr = set(tuple(i[j] for j in idx) for i in relation)
    # 유일성 확인
    if len(arr) == n:
        return True
    return False

def solution(relation):
    answer = 0
    n, m = len(relation), len(relation[0])
    check = set()
    for i in range(1, m+1):
        idx_list = combinations(range(m), i)
        for idx in idx_list:
            for j in check:
                # 최소성 확인 -> 후보키가 포함되어 있다면, break
                if not (set(j) - set(idx)):
                    break
            # 후보키가 포함안 된 index들이라면, 후보키 찾기 시작
            else:
                # 유일성 확인 -> 후보키라면, 정답 +1, 후보키에 추가
                if combi(relation, n, idx):
                    answer += 1
                    check.add(idx)
    return answer


# 2. 성공
## 테스트 21 〉통과 (5.72ms, 10.5MB)
from itertools import combinations

# 유일성 확인
def uniqueness(relation, n, idx):
    if len(set(tuple(i[j] for j in idx) for i in relation)) == n:
        return True
    return False

# 최소성 확인
def minimality(candidate_key, idx):
    for i in candidate_key:
        if set(i).issubset(set(idx)):
            return False
    return True

def solution(relation):
    answer = 0
    n, m = len(relation), len(relation[0])
    candidate_key = set()
    for i in range(1, m+1):
        for idx in combinations(range(m), i):
            # 유일성과 최소성을 만족한다면, 즉 후보키라면 정답 +1, 후보키에 추가
            if uniqueness(relation, n, idx) and minimality(candidate_key, idx):
                answer += 1
                candidate_key.add(idx)

    return answer


# 다른 사람 풀이
# 1. 비트연산 활용
def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)


'''
# Result
풀이 시간: 1시간
테스트 22 〉통과 (3.32ms, 10.2MB)
'''