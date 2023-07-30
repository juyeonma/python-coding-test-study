# 틀린 코드..
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

count = 0
s = []
words = []
basic = ['a', 'c', 'i', 'n', 't']
for _ in range(n):
    word = input().rstrip()
    tmp = ''
    for w in word:
        if w not in basic:
            words.append(w)
            tmp += w
    if tmp == '':
        count += 1
    else:
        s.append(tmp)

if k <= 5:
    print(count)
    sys.exit(0)

teach = []
max_value = 0
def check(str):
    for s in str:
        if s not in teach:
            return False
    return True
def back(start):
    global max_value
    if len(teach) == k - 5:
        cnt = 0
        for i in range(len(s)):
            if check(s[i]):
                cnt += 1
        max_value = max(max_value, cnt)
        return
    
    for w in range(start, len(words)):
        teach.append(words[w])
        back(start+1)
        teach.pop(-1)
back(0)
print(count + max_value)

# 통과 코드
# 참고 : https://resilient-923.tistory.com/324
# 메모리 : 79168	시간 : 3420
from itertools import combinations 
import sys
n, k = map(int, input().split())
answer = 0
# a,n,t,i,c는 반드시 가르쳐야 함

first_word = {'a','n','t','i','c'}

remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word
data = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]

def countReadableWords(data, learned):
    cnt = 0
    for word in data:
        canRead = 1
        for w in word:
            # 안배웠으니까 못읽는다.
            if learned[ord(w)] == 0:
                canRead = 0
                break
        if canRead == 1:
            cnt += 1
    return cnt

if k >= 5:
    learned = [0] * 123
    for x in first_word:
        learned[ord(x)] = 1

    # 남은 알파벳 중에서 k-5개를 선택해본다.
    for teach in list(combinations(remain_alphabet, k-5)):
        for t in teach:
            learned[ord(t)] = 1
    cnt = countReadableWords(data, learned)

    if cnt > answer:
        answer = cnt
    for t in teach:
        learned[ord(t)] = 0
    print(answer)
else:
    print(0)