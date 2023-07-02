import sys
input = sys.stdin.readline
left, right = input().split()
s = input().rstrip()

key = [
    ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
    ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
    ["z", "x", "c", "v", "b", "n", "m"]
]

key_left = "qwertasdfgzxcv"

def idx_check(s):
    for i in range(3):
        for j in range(len(key[i])):
            if key[i][j] == s:
                return i, j
left_x, left_y = idx_check(left)
right_x, right_y = idx_check(right)

cnt = 0
for i in s:
    start = i
    cnt += 1
    if start in key_left:
        x, y = idx_check(start)
        cnt += abs(left_x - x) + abs(left_y - y)
        left = start
        left_x = x
        left_y = y
    else:
        x, y = idx_check(start)
        cnt += abs(right_x - x) + abs(right_y - y)
        right = start
        right_x = x
        right_y = y

print(cnt)

# 메모리 : 31256	시간 : 40