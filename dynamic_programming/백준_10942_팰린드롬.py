# 다시 풀어보기,, 어렵다
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
d = [[0]*n for _ in range(n)]

for nn in range(n):
    for start in range(n-nn):
        end = start+nn
        if start==end: #문자열 시작과 끝 위치가 같으면 1개 뿐이니까 팰린드롬
            d[start][end]=1
        elif num[start]==num[end]: #문자열의 시작과 끝 값이 같으면
            if start+1==end: #두글자 문자열이라는 뜻
                d[start][end]=1 # 두글자 문자열의 시작과 끝이 같은 값이므로 팰린드롬
            elif d[start+1][end-1]==1: #가운데 문자열이 팰린드롬이라면(시작과 끝값 제외하고)
                d[start][end]=1 #무조건 팰린드롬임
                
for _ in range(m):
    s,e=map(int, input().split())
    print(d[s-1][e-1])
    
# 코드길이 : 864 B
# 시간 : 2340 ms
# 메모리 : 61956 KB