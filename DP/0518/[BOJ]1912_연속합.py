# 1. 구간 합을 구해서 풀이에 이용하면 될 것 같았다.
# 헷갈렸던 부분 : 한 구간만 선택하는 부분 때문에 첫번째 수만 선택하는 경우를 위해서 앞에 0을 추가해주었다.
# 하지만, 시간 초과로 실패..
# 시간 : 1초이기 때문에 이중 포문 불가능
# 1초일 때 입력의 최대 크기
# O(M) : 약 1억
# O(N^2) : 약 1만
# O(N^^3) : 약 500
# 현재 문제의 최대값은 십만이었기때문에 O(N)으로만 해결하기

# import sys
# from itertools import combinations
# input = sys.stdin.readline
# n = int(input())
# data = [0]
# data += list(map(int, input().rstrip().split()))

# s = [0]*(n+1)
# s[0] = 0
# s[1] = data[1]
# # 구간 합 리스트 만들기
# for i in range(2, n+1):
#     s[i] = s[i-1] + data[i]

# max_value = -1000

# for i, j in combinations(list(range(n+1)), 2):
#     max_value = max(s[j]-s[i], max_value)

# print(max_value)

# 다시 풀어보았을 때
# 공식 세워놓고 아닌 것 같아서 답 찾아봤는데 맞았다....
# 의심을 하지 말고 해봐야겠다..
# 시간 : 92ms
# 메모리 : 38964KB
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().rstrip().split()))
for i in range(1, n):
    data[i] = max(data[i], data[i-1]+data[i])

print(max(data))