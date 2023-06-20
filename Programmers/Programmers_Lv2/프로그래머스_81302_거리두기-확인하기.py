'''
# 프로그래머스_81302_거리두기 확인하기. Lv 2. 풀이: 23.06.13

# How to
## 1. 거리가 1인 경우와 2인 경우를 나눔
- 거리별로 거리두기를 실패한 경우를 나눔
- 가로뿐 아니라 새로, 대각선도 살펴봐야 하므로 열끼리 묶어서 새로운 배열을 만든다.
- 하나라도 거리두기가 실패하는 경우가 존재하면, answer에 0을 담는다.

- 거리 1 -> 무조건 거리두기 실패
PP  P
    P
    
- 거리 2: 대각선 또는 동일 행/열 -> O가 존재하면, 거리두기 실패
PO  PO  POP
OP  XP

- 거리3~ -> 칸막이와 상관없이 무조건 거리두기 성공


## 2. 다른 사람 풀이: 현재 좌표를 기준으로 상하좌우의 P의 개수를 센다.
- 참고:
https://school.programmers.co.kr/questions/27106
https://school.programmers.co.kr/questions/21304

- 거리두기 실패하는 경우는,
    - O의 상하좌우에 P가 2개 이상이라면, 거리가 2인데 칸막이가 없으므로 거리두기 실패
    - P의 상하좌우 P가 존재한다면(1개 이상), 거리가 1이므로 거리두기 실패


## 반례
- 대각선 P인데, 하나만 X인 경우
PO
XP


# Review
- 다른 사람 풀이를 보니,
    - 입력값이 매우 작은 만큼(대기실 5개, 행과 열 각각 5줄) 나처럼 경우의 수를 나눠서 쌩구현한게 많았다.
    - BFS도 있었는데, 돌려보니 시간이 다소 소요됐다.
- 예전에 늑대와 양 울타리치기였나? 그 문제와 비슷해보여서 풀었는데, 이게 맞는지 모르겠다.
- 처음 푼 코드는 성공하긴 했지만, 너무 지저분하다.
'''

# 1. 성공 Code
# 거리 1인 경우, 실패
def check_one(arr):
    for i in arr:
        if 'PP' in i:
            return True
    return False

# 거리 2인 경우
def check_two(arr):
    # 동일 행 또는 열인 경우, X가 없으면(=POP), 실패
    for i in arr:
        if 'POP' in i:
            return True
        
    # 대각선에 앉아있는 경우
    for i in range(4):
        for j in range(4):
            tmp = arr[i][j:j+2] + arr[i+1][j:j+2]
            # O가 존재하면, 거리두기 실패
            if tmp.count('P') == 2 and 'O' in tmp:
                return True
    return False    
    
def solution(places):
    answer = []
    for arr1 in places:
        # 열끼리 묶어서 새로운 arr 만듦
        arr2 = list(map(''.join, zip(*arr1)))
        # 하나라도 거리두기를 지키고 있지 않다면, 실패 -> 정답에 0을 담음
        if check_one(arr1) or check_two(arr1) or check_one(arr2) or check_two(arr2):
            answer.append(0)
        else:
            answer.append(1)

    return answer


# 2. 다른 사람 아이디어를 바탕으로 구현
## 테스트 1 〉통과 (0.18ms, 10.2MB)
# 현재 좌표를 기준으로 상하좌우에서 P의 개수 세기
def cnt_p(arr, x, y):
    if arr[x][y] == 'X':
        return False
    
    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        # 범위 체크하고, P라면 +1
        if 0 <= nx < 5 and 0 <= ny < 5 and arr[nx][ny] == 'P':
            result += 1
    
    # O의 상하좌우에 P가 2개 이상이거나 P의 상하좌우 P가 존재한다면,
    if 2 <= result or (arr[x][y] == 'P' and result):
        return True

def check(arr):
    for i in range(5):
        for j in range(5):
            # 거리두기 실패라면,
            if cnt_p(arr, i, j):
                return True
    return False    
    
def solution(places):
    answer = []
    for arr in places:
        # 하나라도 거리두기를 지키고 있지 않다면, 실패 -> 정답에 0을 담음
        if check(arr):
            answer.append(0)
        else:
            answer.append(1)

    return answer

'''
# Result
풀이 시간: 40분
테스트 16 〉통과 (0.14ms, 10.2MB)
'''