# 시간 복잡도 : queries의 행의 개수(회전의 개수)는 1 이상 10,000 이하 => O(N^2)..?
# 알고리즘 : 구현..? => 전에 백준에서 배열 돌리기 문제가 생각났다
# 풀이 시간 : 30분
# 돌리기
from collections import deque
def rotate(arr, x1, y1, x2, y2):
    dq = deque()
    # 윗면 복사
    for i in range(y1, y2+1):
        dq.append(arr[x1][i])
    # 오른면 복사
    for i in range(x1+1, x2+1):
        dq.append(arr[i][y2])
    # 아랫면
    for i in range(y2-1, y1-1, -1):
        dq.append(arr[x2][i])
    # 왼쪽면
    for i in range(x2-1, x1, -1):
        dq.append(arr[i][y1])
    
    # deque.rotate(num): 데크를 num만큼 회전 (양수면 오른쪽, 음수면 왼쪽)
    dq.rotate(1)
    
    # 수정된 부분 변경해주기 and 작은 값 찾기
    min_value = 10001
    for i in range(y1, y2+1):
        arr[x1][i] = dq.popleft()
        min_value = min(min_value, arr[x1][i])
    for i in range(x1+1, x2+1):
        arr[i][y2] = dq.popleft()
        min_value = min(min_value, arr[i][y2])
    for i in range(y2-1, y1-1, -1):
        arr[x2][i] = dq.popleft()
        min_value = min(min_value, arr[x2][i])
    for i in range(x2-1, x1, -1):
        arr[i][y1] = dq.popleft()
        min_value = min(min_value, arr[i][y1])
    
    return min_value
    
def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    start = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = start
            start += 1
    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        answer.append(rotate(arr, x1, y1, x2, y2))
    return answer

solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])

# 시간
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (360.99ms, 11.8MB)

# 다른 사람들의 풀이 보고 보완할 점
# min_value = min()이 아닌
# min(dq) 가능!