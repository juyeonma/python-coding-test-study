# 참고 : https://puleugo.tistory.com/39
# 배열 문제에 많이 약한것같다..
# 블로그에 정말 설명이 잘되어있었다

n, m = map(int, input().split())
list_a = []
for _ in range(n):
    list_a.append(list(map(int, list(input()))))

list_b = []
for _ in range(n):
    list_b.append(list(map(int, list(input()))))

def check(i, j): #뒤집기 함수
    for x in range(i, i+3):
        for y in range(j, j+3):
            if list_a[x][y] == 0:
                list_a[x][y] = 1
            else:
                list_a[x][y] = 0

cnt = 0 #카운트
if (n < 3 or m < 3) and list_a != list_b:
    # 예외1 : 리스트가 작을 때
    cnt -= 1
else:
    for r in range(n-2):
        for c in range(m-2):
            if list_a[r][c] != list_b[r][c]:
                cnt += 1
                check(r, c)

if cnt != -1:
    if list_a != list_b: # a와 b가 같은지 확인
        cnt = -1
print(cnt)


# 다음에 다시 풀기!!