'''
# 프로그래머스_42860_조이스틱. Lv 2. 풀이: 23.06.22 -> 실패

# How to
## 1. 실패
- 알파벳 변경 횟수와 커서 이동 횟수를 각각 기록한다.
- 알파벳: 매번 변경할 문자열의 알파벳에서 정방향 인덱스와 역방향 인덱스 중 최솟값을 정답에 더한다.
- 커서: A가 아닌 인덱스 중에서, 0번 인덱스를 제외하고 처음과 끝 중에서 정방향과 역방향 중 어느것이 더 적은 횟수인지 구한다.

## 다른 사람 풀이, 모범 답안
출처: https://velog.io/@jqdjhy/프로그래머스-파이썬-조이스틱-Greedy


## 반례
"BBBBAAAABA"
답: 12
정방향으로가면 13이지만,
역방향으로 간 후 다시 돌아와서 정방향으로 가면 12


# Review
- 질문게시판을 보니, 커서 이동 시 방향을 바꾸는 경우가 반례였다.
- 즉 나는 한 방향(정방향이든 역방향이든)으로만 이동했는데, 방향을 바꾸는게 더 적은 횟수인 반례가 존재했다.
- 다들 이게 왜 그리디냐고 하던데, 정말 왜 그리디일까..? DFS로 풀어야하나?
'''

# 1. 실패 Code
## 합계: 59.3 / 100.0
def solution(name):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(name)
    answer = 0
    result = []
    
    # 0번 인덱스는 커서를 이동하지 않으므로, 알파벳 변경만 기록
    if name[0] != 'A':
        idx = abc.index(name[0])
        answer += min(idx, 26-idx)
        
    # 알파벳을 변경하면서 인덱스 기록
    for i in range(1, n):
        if name[i] != 'A':
            idx = abc.index(name[i])
            answer += min(idx, 26-idx)
            result.append(i)
            
    # 커서 이동 시, 정방향 or 역방향 중 어느것이 더 빠른지
    if result:
        answer += min(n-result[0], result[-1])

    return answer
#합계: 59.3 / 100.0

'''
# Result
풀이 시간: 실패

'''