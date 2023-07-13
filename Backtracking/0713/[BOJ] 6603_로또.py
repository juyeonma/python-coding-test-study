import sys
input = sys.stdin.readline

def back(n, depth):
    if depth == 6:
        if arr[0] < arr[1] < arr[2] < arr[3] < arr[4] < arr[5]:
            print(' '.join(map(str, arr)))
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            arr[depth] = data[i]
            back(n, depth+1)
            visit[i] = False
while True:
    data = list(map(int, input().split()))
    if not data[0]:
        sys.exit(0)
    
    data = data[1:]
    n = len(data)
    visit = [False] * n
    arr = [0] * 6

    back(n, 0)
    print()
# # 속도 356ms

# 다른 사람 풀이 참고

def solve(a, index, lotto):
    if len(lotto) == 6:
        print(' '.join(map(str,lotto)))
        return
    if index == len(a):
        return
    
    # 이렇게 백트래킹을 두갈래로 나뉘어서 하는게 내 기준에는 아직 어렵게 느껴지는 것 같다..
    solve(a, index+1, lotto+[a[index]])
    solve(a, index+1, lotto)

while True:
    n, *a = list(map(int, input().split()))
    # 이렇게 숫자와 리스트를 따로 선언할 수 있다는 것을 새롭게 알았다..
    if n == 0:
        break
    solve(a, 0, [])
    print()

# 속도 40ms