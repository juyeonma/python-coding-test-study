# 풀이방법
# 1. *이 하나라고 했으니 *의 위치를 찾는다.
# 2. *의 위치에따라 앞 뒤로 나누어서 맞으면 string과 비교 후 DA 출력 아니라면 NE 출력
# 주의할 점
# s가 비교 데이터보다 길이가 더 길면 안되기 때문에 조건에 넣어주기

# 메모리 : 31256KB
# 시간 : 40MS
import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()
data = list(input().rstrip() for _ in range(n))

index = 0
# 1번
for i in range(len(s)):
    if s[i] == '*':
        index = i
        break

for i in range(len(data)):
    # 2번과 3번
    if data[i][:index] == s[:index] and data[i][::-1][:len(s)-index-1] == s[index+1:][::-1] and len(s) <= len(data):
        print("DA")
    else:
        print("NE")
