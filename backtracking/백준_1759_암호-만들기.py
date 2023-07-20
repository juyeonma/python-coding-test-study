'''
# 백준_1759_암호 만들기. 골드 5. 풀이: 23.07.16

# How to
- 각 암호내에서 증가하는 순서, 즉 오름차순 배열
- 암호는 서로 다른 알파벳으로 이루어짐, 즉 중복 불가
- => 조합

- dfs로 매번 다음 인덱스부터 탐색.
- 이때 모음과 자음인지 체크하여 개수를 조절하고, 재귀로 들어간다.
- 암호가 정해진 길이가 되었는데 모음과 자음 조건에 맞다면, 출력


# Review
- 풀이 시간: 10분
- 모음 & 자음은 영어로 vowel & consonant 였다.
- 매번 모음과 자음을 체크하는 부분을 더 깔끔하게 만들 순 없을까?
'''


# Code
# 1. 직접 구현: 성공
## 메모리: 31256 KB, 시간: 52 ms
l, c = map(int, input().split())
# 알파벳을 오름차순 정렬
alphabet = sorted(input().split())
visited = [False] * c
mother, son = 0, 0
mothers = 'aeiou'
answer = []
def dfs(idx, result):
    global mother, son
    # 암호가 정해진 길이가 되었다면, return
    if len(result) == l:
        # 이때 모음이 1개 이상, 자음이 2개 이상이면, 출력
        if mother >= 1 and son >= 2:
            print(result)
        return
    
    # 다음 인덱스부터 탐색.
    # 매번 모음 자음을 체크하여, 개수를 조절하고 재귀로 들어감.
    for i in range(idx+1, c):
        if alphabet[i] in mothers:
            mother += 1
        else:
            son += 1
            
        dfs(i, result+alphabet[i])

        if alphabet[i] in mothers:
            mother -= 1
        else:
            son -= 1
            
# 인덱스 0부터 탐색하기 위하여, -1을 넣어줌
dfs(-1, '')


# 2. 조합 라이브러리 사용: 성공
## 메모리: 31256 KB, 시간: 44 ms
from itertools import combinations
l, c = map(int, input().split())
# 알파벳을 오름차순 정렬
alphabet = sorted(input().split())
mothers = 'aeiou'

for password in combinations(alphabet, l):
    mother, son = 0, 0
    # 모음, 자음 개수를 셈
    for j in password:
        if j in mothers:
            mother += 1
        else:
            son += 1
            
    # 이때 모음이 1개 이상, 자음이 2개 이상이면, 출력
    if mother >= 1 and son >= 2:
        print(''.join(password))
        