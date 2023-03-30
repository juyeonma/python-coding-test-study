n, m, r = map(int, input().split())
array = list(input().split() for _ in range(n))
temp = []

while r:
    for i in range(min(n, m) // 2):
        x, y = i, i
        temp = array[x][y]

        for j in range(i+1, n - i):  # 좌
            x = j
            prev_value = array[x][y]
            array[x][y] = temp
            temp = prev_value

        for j in range(i+1, m-i):  # 하
            y = j
            prev_value = array[x][y]
            array[x][y] = temp
            temp = prev_value

        for j in range(i+1, n-i):  # 우
            x = n - j - 1
            prev_value = array[x][y]
            array[x][y] = temp
            temp = prev_value

        for j in range(i+1, m - i):  # 상
            y = m - j - 1
            prev_value = array[x][y]
            array[x][y] = temp
            temp = prev_value
    r -= 1
for i in array:
    print(' '.join(i))
