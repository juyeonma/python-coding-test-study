'''
# 백준_1080_행렬. 실버 1. 풀이: 23.05.30 -> 실패

# How to
- n, m이 3보다 작은 경우, 뒤집는 연산 불가능: 예제 3
- 3*3이 가능한 범위 내에서, 모든 좌표의 값이 같은지 비교
    - 다르다면, 뒤집고 숫자 count
- 모든 좌표에서 비교 후 뒤집었으니, 최종적으로 A와 B가 같은지 비교 및 출력

# Review
- 3*3을 어떻게 처리할지 고민이었다.
- 9칸을 모두 뒤집어야하는데, 현재 좌표를 기준으로 어디만큼 3*3을 잡아야할지 몰랐다.
- 결국 구글링 결과, 현재 좌표를 가장 왼쪽 끝점으로 설정하고 가능한 범위만 탐색하더라.
    - 그렇게 탐색하면서 다르면 뒤집기를 반복하다가, 전부 뒤집은 후에 A == B인지만 체크 및 출력.
    - 참고: https://puleugo.tistory.com/39
    
- 이게 왜 그리디인걸까..? 그리디가 정확히 뭔지 헷갈린다.
    - 참고: https://www.acmicpc.net/board/view/13509
    - 그리디란 매 순간 최선의 선택을 해야한다.
    - 따라서 여기에서 최선의 선택이란, 이번에 뒤집을 칸의 뒤집는 횟수를 최소화하기!
'''
 
# 구글링 Code
n, m = map(int, input().split())
arr_a = [list(map(int, list(input()))) for _ in range(n)]
arr_b = [list(map(int, list(input()))) for _ in range(n)]

def flip(x, y):
    # x=n-3. -> n-3, n
    for i in range(x, x+3):
        for j in range(y, y+3):
            # 1->0, 0->1. 바뀌기 전+바뀐 후 = 1
            arr_a[i][j] = 1 - arr_a[i][j]
cnt = 0
for i in range(n-2):
    for j in range(m-2):
        # 다르다면, 뒤집고 횟수 count
        if arr_a[i][j] != arr_b[i][j]:
            flip(i, j)
            cnt += 1

# 전부 뒤집었으니, 같은지 비교
if arr_a == arr_b:
    print(cnt)
else: # (n < 3 or m < 3) and arr_a != arr_b 포함
    print(-1)

'''
# Result
풀이 시간: 실패
메모리:  KB
시간:  ms
코드 길이:  B
'''