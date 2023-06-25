'''
# 프로그래머스_42747_H-Index. Lv 2. 풀이: 23.06.22

# How to
- 내림차순 정렬
- 인용 수 <= 인용된 논문 수인 지점을 찾는다.
- 직전 인용 수와 현재 인용 수 사이의 값을 탐색한다.
    - 직전 인용 수의 논문 수를 고정하고, 
    - 현재 인용 수(H-Index 후보)보다 더 큰 값이 나오면, return
- 만약 아무 값도 찾지 못하면, 입력값의 길이(즉 논문 수)를 return

## 반례
- 입력값에 없어도 정답이 될 수 있다.
[1, 4, 5]
답: 2

[10, 10, 10, 10, 10]
답: 5

# Review
- 처음에 H-Index의 정의를 착각해서 입력값만 생각하는 바람에 반절을 틀렸다. 
- 그러다가 입력값에 없어도 정답이 될 수 있는 반례를 질문게시판에서 보고, 성공.
- 다른 사람 풀이를 보니까 엄청 간단하게 풀었는데, 나중에 이해해야지..
'''

# 1. 성공 Code
def solution(citations):
    n = len(citations)
    answer = n
    # 내림차순 정렬
    citations.sort(reverse=True)
    
    for i, v in enumerate(citations):
        # 인용 수 <= 인용된 논문 수
        if v <= i+1:
            answer = v
            # 반례처럼, 입력값에는 없지만 정답이 될 수 있는 인용 수를 찾아서
            for v2 in range(citations[i-1]-1, v, -1):
                if v2 <= i:
                    return v2
            return answer
    return answer


# 다른 사람 풀이
# 1.
'''
설명
sort로 정렬해서 가장 큰값부터 작은값으로 정렬한후, enumerate로 (index, value)형태로 묶는다. 
그리고 최댓값(start = 1)부터 각 value에 대해 최솟값 value의 값을 min으로 추출하고, 
이 추출된 값은 enumerate가 끝나는 citations 리스트의 크기에 해당하는 갯수가 나온다. 
이들을 map으로 묶으면, 한 value의 입장에서 보는 최솟값 value의 집합이 나온다. 
즉 h값들의 집합이나온다. 
h값중 최대값을 max로 뽑아서 출력하면 된다.

1) min(index,value) 부분은 가능할 수 있는 모든 h-index를 추출하는 부분 
2) max(~) 값은 가능할 수 있는 모든 h-index 중 가장 큰 값을 추출하는 부분으로 생각하시면 됩니다. 
예를들어 [6, 5, 4, 1, 0]의 경우에선 
min~ 부분은 min(1, 6), min(2, 5), min(3, 4), min(4, 1), min(5, 0), 
즉 해당 인용수 이상의 논문개수와 해당 논문의 인용수 중 더 작은 숫자를 고르는 작업을 하고(h-index로 가능한 숫자 추출), 
max~부분은 앞에서 골라진 (1, 2, 3, 1, 0) 중 가장 큰 숫자를 뽑아 실제 h-index를 구하는 방법
'''
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

# 2.
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


'''
# Result
풀이 시간: 30분
테스트 13 〉통과 (0.21ms, 10.2MB)
'''