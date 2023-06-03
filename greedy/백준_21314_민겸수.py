'''
# 백준_21314_민겸수. 실버 2. 풀이: 23.05.30

# How to
- 같은 갯수라면, K가 더 큼: MM < MK
- K가 있다면, 붙이자: MM K: 105, MMK: 500
- K가 없다면, 쪼개자: MM: 10, M M: 11

- 최댓값: K는 붙이고, M만 있으면 쪼개자
- 최솟값: K는 쪼개고, M만 있으면 붙이자

- 1. K를 기준으로 분할하여 max와 min을 각각 구함.
- 2. 문자열 길이만큼 for문으로 순차적으로 탐색하며 한꺼번에 max와 min값을 구함


## 반례
- K가 없는경우를 고려해야한다.
MMM
정답:
111
100


# Review
- K로 분할하다보니, M만 존재하거나 수의 마지막이 K가 아닌 경우를 따로 고려해야한다.
- K 여부도 있고 코드도 지저분해서 for문으로 하나씩 탐색하면서 후가해보니, 조금 정리됐다. 시간은 차이 없지만.
- 쉬운 문제인데도 불구하고 깔끔하게 코드 짜려니까 나름 복잡했다.
'''

# 2. 성공 COde
word = input()
start, n = 0, len(word)
max_n, min_n = '', ''

for i in range(n):
    if word[i] == 'K':
        # MK 변환
        max_n += str(5 * 10**(i-start))
        
        # MM 변환 or K만 변환
        if i != start:
            min_n += str(10**(i-start) + 5)
        else:
            min_n += '5'
        start = i+1

# 마지막 K 뒤에 M이 남았다면, 변환
max_n += '1'*(n-start)
if n != start:
    min_n += str(10**(n-start-1))

print(int(max_n), int(min_n), sep='\n')


# 1. 성공 Code
word = input()

if 'K' in word:
    arr = [i for i in range(len(word)) if word[i] == 'K']

    max_n, min_n = '', ''
    start, end = 0, len(word)-1
    for i in arr:
        # MK로 붙여서 변환
        max_n += str(5 * 10**(i-start))
        start = i+1
    # 뒤에 남은 M들을 쪼개서 변환
    max_n += '1'*(end-arr[-1])
        
    start = 0
    for i in arr:
        # 앞에 M이 있을 경우에, MM 붙여서 변환
        if i != start:
            min_n += str(10**(i-start-1))
        # K 변환
        min_n += '5'
        start = i+1
    # 뒤에 남은 M이 있다면, MM 붙여서 변환
    if end != arr[-1]:
        min_n += str(10**(end-arr[-1]-1))

    print(int(max_n), int(min_n), sep='\n')
    
else:
    max_n = '1' * len(word)
    min_n =  10 ** (len(word)-1)
    print(int(max_n), int(min_n), sep='\n')

'''
# Result
풀이 시간: 45분
메모리: 31256 KB
시간: 44 ms
코드 길이: 390 B
'''