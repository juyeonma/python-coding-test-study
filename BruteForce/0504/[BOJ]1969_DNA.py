# 풀이방법
# 1. A, C, G, T 배열을 만듦(문자열 길이만큼)
# 2. 제일 많은 문자 뽑기
# 3. 제일 많은 문자 초기화 후 다른 문자 더하기

# 메모리 : 31256KB
# 시간 : 60MS
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# 1번
dna = [[0, 0, 0, 0] for _ in range(m)]  # A, C, G, T

s = list(input() for _ in range(n))
# 2번
for i in range(n):
    for j in range(m):
        if s[i][j] == 'A':
            dna[j][0] += 1
        if s[i][j] == 'C':
            dna[j][1] += 1
        if s[i][j] == 'G':
            dna[j][2] += 1
        if s[i][j] == 'T':
            dna[j][3] += 1
# 3번
result = ''
value = 0
for i in range(m):
    if dna[i].index(max(dna[i])) == 0:
        result += 'A'
        dna[i][0] = 0
    elif dna[i].index(max(dna[i])) == 1:
        result += 'C'
        dna[i][1] = 0
    elif dna[i].index(max(dna[i])) == 2:
        result += 'G'
        dna[i][2] = 0
    elif dna[i].index(max(dna[i])) == 3:
        result += 'T'
        dna[i][3] = 0
    value += sum(dna[i])

print(result)
print(value)


# 다른 풀이들을 보고 느낀 점!
# ! 딕셔너리를 썼다면 더 빨랐을 것 같다!
