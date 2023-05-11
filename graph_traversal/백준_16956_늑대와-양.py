'''
# 백준_16956_늑대와 양. 실버 3. 풀이: 23.05.09

# 풀이방법
- 스페셜 저지이므로, 답이 여러 가지가 될 수 있다!
- 노트: 이 문제는 설치해야 하는 울타리의 최소 개수를 구하는 문제가 아니다.
- 양: 이동 불가, 늑대: 상하좌우로 이동 가능
- 목표: 울타리를 설치하여, 늑대가 양이 있는 칸으로 이동 못하게 하자.

## 1번 풀이
- 양의 상하좌우에 다 울타리를 치자.
- 만약 양이 늑대와 바로 붙어있다면, 바로 실패.

## 2번 풀이: 맞힌 사람 풀이 참고
- 1번에서는 양과 늑대가 붙어있으면 바로 실패했는데, 이번에는 처음부터 체크해보자.
    - 맞힌 사람 풀이를 보니, 이 아이디어가 있어서 바로 풀이를 참고하였다.
- 원래 배열과 90도 회전한 배열(즉 열->행으로 변경한)에서 양과 늑대가 붙어있으면, 바로 실패.
- 실패하지 않았다면, 모든 빈칸을 울타리로 바꿔서 전부 출력.
- 이때, 90도 회전한 배열을 tuple이 아니라 string으로 바꾸어야 양과 늑대가 붙어있는것을 찾을 수 있음.
- 무려 5배나 더 빨라졌다.

# 보완할 것
- 문제에서 울타리의 최소 개수를 구하는 것이었다면 문제가 더 어려웠을 것이다.
- 이게 왜 DFS BFS지..? 그냥 구현같다.
'''

# 1번 풀이 기록
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

arr = []
sheep = []

for i in range(r):
    tmp = list(input().rstrip())
    arr.append(tmp)
    for j in range(c):
        # . 빈칸, S 양, W 늑대
        if tmp[j] == 'S':
            sheep.append((i, j))
        
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for x, y in sheep:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if arr[nx][ny] == 'W':
                print(0)
                sys.exit(0)
            elif arr[nx][ny] == '.':
                arr[nx][ny] = 'D'

print(1)
for i in arr:
    print(''.join(i))


# 2번 풀이 기록: 5배나 더 빠름!
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [input().rstrip() for _ in range(r)]

def check_arr(arr):
    for i in arr:
        if i.count('WS') or i.count('SW'):
            print(0)
            sys.exit(0)

check_arr(arr)
check_arr(map(lambda x: ''.join(x), zip(*arr)))

print(1)
for i in arr:
    print(i.replace('.', 'D'))


'''
# 결과
메모리: 38184 KB -> 31256 KB
시간: 220 ms -> 48 ms
코드 길이: 664 B -> 351 B
'''