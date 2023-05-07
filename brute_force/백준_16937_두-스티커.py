'''
# 백준_16937_두 스티커. 실버 3. 풀이: 23.04.23

# 풀이방법
- 색종이를 넓이 순으로 정렬해서, 가장 넓은 것부터 겹쳐보자.
- 색종이 두개를 멀리 떨어트려서 붙여보자(대각선 모서리)
- 색종이가 겹치거나 모눈종이를 벗어나면 안된다.

- 2개씩 조합 or 그냥 for문으로 해도 됨.
- 조건문: A면에서 두 변의 길이가 같거나 작고, B면의 길이를 초과하지 않는다면, 최댓값 갱신.

# 반례
input:
2 2
2
100 1
1 1

output:
0

input:
10 10
2
5 5
10 10
    
output:
0
'''

# code
from itertools import combinations
import sys
input = sys.stdin.readline

# 모눈종이 크기 h, w
h, w = map(int, input().split())

stickers = [list(map(int, input().split())) for _ in range(int(input()))]
arr = list(combinations(stickers, 2))

result = 0
for a, b in arr:
    x1, y1 = a
    x2, y2 = b
    
    if (x1+x2 <= h and max(y1, y2) <= w) or (x1+x2 <= w and max(y1, y2) <= h) \
        or (x1+y2 <= h and max(x2, y1) <= w) or (x1+y2 <= w and max(x2, y1) <= h) \
            or (x2+y1 <= h and max(x1, y2) <= w) or (x2+y1 <= w and max(x1, y2) <= h) \
                or (y1+y2 <= h and max(x1, x2) <= w) or (y1+y2 <= w and max(x1, x2) <= h): 
        result = max(result, (x1 * y1) + (x2 * y2))
    
print(result)    

'''
# 만약, 조합 대신에 for문으로 한다면?
- n개의 색종이를 이중 for문으로 조합하면 된다.
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = stickers[i]
        x2, y2 = stickers[j]
'''

'''
# 결과
메모리: 31256 KB
시간: 48 ms
코드 길이: 737 B
'''