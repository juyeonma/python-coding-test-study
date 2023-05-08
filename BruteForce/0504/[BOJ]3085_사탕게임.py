# 풀이방법
# 1. 인접한 부분에 색이 다르다면 교환
# 2. 갯수를 세는 함수
# 3. 원래 배열로 교환

# 시간초과! => pypy에서만 돌아감
# count함수가 더 간단했어야 했다..! => for문을 너무 많이 활용함
import sys
input = sys.stdin.readline
n = int(input())

candy = []
for _ in range(n):
    candy.append(list(input().rstrip()))
max_value = 0


def count(f):
    temp = []
    global max_value
    for i in range(n):
        temp.append(candy[i])
    for i in range(n):
        t = []
        for j in range(n):
            t.append(candy[j][i])
        temp.append(t)
    for i in temp:
        cnt = 1
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                cnt += 1
            else:
                cnt = 1
            max_value = max(max_value, cnt)
    return max_value


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for x in range(n):
    for y in range(n):
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if candy[x][y] != candy[nx][ny]:
                    candy[x][y], candy[nx][ny] = candy[nx][ny], candy[x][y]
                    count(candy)
                    candy[nx][ny], candy[x][y] = candy[x][y], candy[nx][ny]
print(max_value)


# 참고 : https://enhjh.tistory.com/43
# 더 빠른 코드
# 시간 : 1940ms
def check(arr):
    n = len(arr)
    answer = 1
    for i in range(n):
        # 열 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르다면 다시 1로 초기화
                cnt = 1
            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt
        # 행 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르다면 다시 1로 초기화
                cnt = 1
            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

    return answer


n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n:
            # 인점한 것과 바꾸기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            # check는 arrd에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp = check(arr)
            if temp > answer:
                answer = temp
            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        # 행 바꾸기
        if i+1 < n:
            # 인점한 것과 바꾸기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            # check는 arrd에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp = check(arr)
            if temp > answer:
                answer = temp
            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(answer)
