'''
# 백준_1969_DNA. 실버 4. 풀이: 23.05.04

# 풀이방법
- 방법 1.
    - 자릿수별로 알파벳 dictionary 만들어서, 알파벳 갯수 세기
    - 각 자릿수별로 정렬해서, 가장 많은 알파벳은 정답 문자열에 추가하고, 나머지 알파벳 갯수 더하기

- 방법 2.
    - 방법 1에서는 모든 자릿수 알파벳의 dict을 미리 만들었는데, 이번에는 매번 만들어보자.
    - 우선 문자열을 전부 받아서 list 만들기
    - zip을 활용해서 문자열의 각 자릿수를 묶기.
    - 알파벳: 갯수로 dict 만들기
    - value가 가장 클때의 key값을 구해 정답 문자열에 추가, 나머지 알파벳의 갯수는 더함.
'''

'''
# 보완할 것
- 쉬운 문제였다. 
- 다만.. dictionary의 sort와 max 값에서 key값 작성법을 헷갈렸다. 까먹지 말자!
- 알파벳: 개수가 아니라, 갯수: 알파벳으로 거꾸로 dic을 만들어도 가능하다는걸 잊지말자. 여기서는 시간차이 없었음.
'''

# 방법 1. 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 자릿수별 알파벳 dictionary 만들기
arr = [{'A': 0, 'T': 0, 'G': 0, 'C': 0} for _ in range(m)]
for _ in range(n):
    word = input().rstrip()
    for i in range(m):
        # 단어의 알파벳에 해당되는 key에 +1
        arr[i][word[i]] += 1
        
answer = ''
cnt = 0
for i in arr:
    # 가장 큰 value, 즉 갯수값으로 정렬
    tmp = sorted(i.items(), key=lambda x: (-x[1], x[0]))[0]
    # 알파벳, 개수
    answer += tmp[0] # 알파벳은 정답 문자열에 추가
    cnt += n - tmp[1] # 나머지 알파벳의 갯수
    
print(answer, cnt, sep='\n')


# 방법 2. 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]

answer = ''
cnt = 0

# 각 자릿수별로 묶어서 갯수세기
for i in list(zip(*words)):
    # 알파벳: 갯수 dictionary 만들기
    dic = dict(zip("ACGT", 
                   [i.count('A'), i.count('C'), i.count('G'), i.count('T')]))
    # value가 가장 클때의 key값
    s = max(dic, key=dic.get)
    answer += s # 정답 문자열에 추가
    cnt += n - dic[s] # 나머지 알파벳의 갯수
    
print(answer, cnt, sep='\n')

'''
# for문의 dic을 만들때
지금의 갯수: 알파벳 dic -> value가 가장 클때의 key값을 구하는것 말고,
갯수: 알파벳 dic -> 해서 갯수의 max을 구해서 진행해도 된다.
이때, 동일 갯수로 key 값이 중복될 경우 그 다음 key값에 덮어씌워지기 때문에
ACGT가 아니라 TGCA로 거꾸로 dict에 넣어야한다.

arr = dict(zip([i.count('T'), i.count('G'), i.count('C'), i.count('A')],
                "TGCA"))
max_num = max(arr)
answer += arr[max_num]
cnt += n - max_num
'''

'''
# 결과
메모리: 52 KB -> 44 KB
시간: 31256 ms -> 31256 ms
코드 길이: 409 B -> 374 B
'''