'''
# 백준_14500_테트로미노. 골드 4. 풀이: 23.04.29 -> 실패

# 풀이방법
- 도형은 5개, 그러나 모든 경우의 수는 19가지.
    - 직선: 2가지
    - 네모: 1가지
    - 니은자: 8가지
    - 지그재그: 4가지
    - 우자: 4가지
- 행 대칭, 열 대칭, 시계방향 90도 회전 -> 경우의 수 8가지.
- 모든 좌표에서 도형별, 대칭/회전별 모든 경우의 수 탐색하며 최댓값 찾기.

- nieun 대칭 및 회전 예시
1. 원본
0 1 2 2
0 0 0 1

2. 90도
0 0 0 1
0 -1 -2 -2

3. 행 대칭
0 -1 -2 -2
0 0 0 1

4. 90도 후 열 대칭
0 0 0 1
0 1 2 2

5. 열 대칭
0 1 2 2
0 0 0 -1

6. 행 대칭 후 열 대칭
0 -1 -2 -2
0 0 0 -1

7. 90도 후 행 대칭
0 0 0 -1
0 -1 -2 -2

8. 90도 후 행 대칭 열 대칭
0 0 0 -1
0 1 2 2
'''

'''
# 피드백
- 도형에 엄청 약한지라, 대칭/회전 모양 생각하는데 가장 애를 먹었다.
- 테스트 케이스를 넣었더니, 다음에서 실패.
4 4
0 0 0 0
0 0 1 0
0 0 2 3
0 0 4 0
4 4
0 0 0 0
0 0 0 0
0 0 1 0
0 2 3 4
- 디버깅을 해보니, 도형별 모든 대칭/회전이 이루어지지 않고 한개씩만 계산되는걸 발견.
- 왜..? 코드 어디에 문제 있는지 모르겠음 ㅠㅠ
'''
# code

import sys
input = sys.stdin.readline

# 행 대칭, 열 대칭, 시계방향 90도 회전 -> 경우의 수 8가지.
eight_n = [(0, 0, 0), (0, 0, 1), (1, 0, 0), (0, 1, 1), \
    (0, 1, 0), (1, 1, 0), (1, 0, 1), (1, 1, 1)]

# 도형은 5개, 그러나 모든 경우의 수는 19가지.
line_x = [0, 0, 0, 0]
line_y = [0, 1, 2, 3]
line_n = 2

square_x = [0, 0, 1, 1]
square_y = [0, 1, 0, 1]
square_n = 1

nieun_x = [0, 1, 2, 2]
nieun_y = [0, 0, 0, 1]
nieun_n = 8

zigzag_x = [0, 1, 1, 2]
zigzag_y = [0, 0, 1, 1]
zigzag_n = 4

woo_x = [0, 0, 0, 1]
woo_y = [0, 1, 2, 1]
woo_n = 4

txs = [line_x, square_x, nieun_x, zigzag_x, woo_x]
tys = [line_y, square_y, nieun_y, zigzag_y, woo_y]
tns = [line_n, square_n, nieun_n, zigzag_n, woo_n]

# 대칭, 회전하기
def eight_2(row, col, rotate, t_x, t_y):
    add_x, add_y = t_x, t_y
    if rotate:
        add_x, add_y = -1 * add_y, -1 * add_x
        
    if row: 
        add_y *= -1
        
    if col:
        add_x *= -1
        
    return add_x, add_y  

# 해당 좌표의 넓이 최댓값 구하기
def sum_tetromino(n, m, arr, x, y, tetromino_x, tetromino_y, tetromino_n):
    result = 0
    for row, col, rotate in eight_n[:tetromino_n]:
        sum_tmp = 0
        for i in range(4):
            add_x, add_y =  eight_2(row, col, rotate, tetromino_x[i], tetromino_y[i])
            nx = x + add_x
            ny = y + add_y
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                sum_tmp = 0
                break
            sum_tmp += arr[nx][ny]
        else:
            result = max(result, sum_tmp)

    return result   

def solve():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for x in range(n):
        for y in range(m):
            for tetromino_x, tetromino_y, tetromino_n in zip(txs, tys, tns):
                answer = max(answer, sum_tetromino(n, m, arr, x, y, tetromino_x, tetromino_y, tetromino_n))
                
    print(answer)
    
solve()

'''
# 결과
메모리:  KB
시간:  ms
코드 길이:  B
'''