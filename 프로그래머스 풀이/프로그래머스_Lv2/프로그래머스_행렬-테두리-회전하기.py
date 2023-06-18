'''
# 프로그래머스_행렬 테두리 회전하기.py. Lv 2. 풀이: 23.06.14

# How to
## 1.
- 움직일 좌표들을 4 종류로 나눈다: 위, 오른쪽, 아래, 왼쪽
    - 위와 오른쪽은 정방향으로, 아래와 왼쪽은 역방향으로 구해서 좌표와 값들을 각각 1차원 list에 저장
- 값 list에서 최솟값을 구해 answer에 주가
- 값 list에서 마지막 값을 첫번째로 옮긴 후, 좌표 list에 값을 대응하여 집어넣음(=회전)
- 변화한 배열을 return
    - 단, 마지막 쿼리일 때는 배열 return 안함.

## 2.
- 1번과 같은 로직인데, 두가지 차이점
    - 처음에 직전값을 저장해두고, 매번 현재 좌표와 직전값을 갱신
    - 매번 최솟값 갱신

# Review
- 1번과 2번 모두 비슷한 시간이 소요 됐지만, 2번이 더 마음에 든다. 뭔가 좀 더 깔끔한 느낌..?
- 코드가 이게 최선일까? 싶다가도, 완전탐색이니까 어쩔 수 없다 싶다..
'''

# 1. 좌표, 값 별도 저장: 성공 Code
## 테스트 7 〉통과 (321.17ms, 12MB)
def rotate(answer, arr, x1, y1, x2, y2, last=False):
    result, value = [], []
    # 위
    for y in range(y1, y2+1):
        result.append([x1, y])
        value.append(arr[x1][y])
    # 오른쪽
    for x in range(x1+1, x2):
        result.append([x, y2])
        value.append(arr[x][y2])
    # 아래
    for y in range(y2, y1-1, -1):
        result.append([x2, y])
        value.append(arr[x2][y])        
    # 왼쪽
    for x in range(x2-1, x1, -1):
        result.append([x, y1])
        value.append(arr[x][y1])                
            
    # 최솟값 구하기
    answer.append(min(value))
   
    # 마지막이면, 배열 회전하지 말고 그대로 return
    if last:
        return
        
    # 시계방향으로 회전 및 값을 집어넣음
    value = [value[-1]] + value[:-1]
    for (x, y), v in zip(result, value):
        arr[x][y] = v

    return arr

def solution(rows, columns, queries):
    answer = []
    
    # 배열 생성
    arr = []
    i, j = 1, columns+1
    for _ in range(rows):
        arr.append(list(range(i, j)))
        i, j = j, j+columns

    # 마지막 이전까지는 최솟값을 찾고 배열도 회전해야함
    for x1, y1, x2, y2 in queries[:-1]:
        arr = rotate(answer, arr, x1-1, y1-1, x2-1, y2-1)
    
    # 마지막에는 최솟값만 찾으면 되므로,
    x1, y1, x2, y2 = queries[-1]
    rotate(answer, arr, x1-1, y1-1, x2-1, y2-1, last=True)
    
    return answer


# 2. 그때그때 좌표 갱신: 성공
## 테스트 3 〉통과 (363.40ms, 11.6MB)
def rotate(answer, arr, x1, y1, x2, y2):
    before = arr[x1+1][y1] # 직전값
    value = 10001 # 최솟값으로 갱신할 것
    # 위
    for y in range(y1, y2+1):
        value = min(value,arr[x1][y])
        arr[x1][y], before = before, arr[x1][y]
    # 오른쪽
    for x in range(x1+1, x2):
        value = min(value,arr[x][y2])
        arr[x][y2], before = before, arr[x][y2]
    # 아래
    for y in range(y2, y1-1, -1):
        value = min(value,arr[x2][y])
        arr[x2][y], before = before, arr[x2][y]
    # 왼쪽
    for x in range(x2-1, x1, -1):
        value = min(value,arr[x][y1])
        arr[x][y1], before = before, arr[x][y1]
        
    # 최솟값 구하기
    answer.append(value)   
    
    return arr, answer

def solution(rows, columns, queries):
    answer = []
    
    # 배열 생성
    arr = []
    i, j = 1, columns+1
    for _ in range(rows):
        arr.append(list(range(i, j)))
        i, j = j, j+columns

    # 회전한 배열, 정답 리스트 구하기
    for x1, y1, x2, y2 in queries:
        arr, answer = rotate(answer, arr, x1-1, y1-1, x2-1, y2-1)

    return answer


'''
# Result
풀이 시간: 1시간 30분
테스트 7 〉통과 (321.17ms, 12MB)
'''