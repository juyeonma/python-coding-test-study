'''
# 백준_2503_숫자 야구. 실버 3. 풀이: 23.04.23

# 풀이방법
- 1~9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수: 9P3 = 504가지
- 정답이 a b c 이고 질문이 aa bb cc 라면,
  aa == a 로 자리별로 같으면: 스트라이크
  aa != a 지만, aa == b 또는 aa == c 면, 볼.
- 경우의 수가 적으므로, 모든 경우의 수에 대해 스트라이크와 볼을 계산 후 비교하여 맞는 것만 찾아내면 된다.

1. 경우의 수 504개의 list를 만든다
2. 조건문으로 스트라이크와 볼을 가린다.
3. 조건에 맞지 않다면, 이번 경우는 실패
'''

# code
from itertools import permutations
import sys
input = sys.stdin.readline

# 1. 경우의 수 504개의 list를 만든다
check = [True] * 504
arr = list(permutations(range(1, 10), 3))

# 질문한 세 자리 수, 스트라이크, 볼
question = [list(map(int, input().split())) for _ in range(int(input()))]

for i in range(504):
    a, b, c = arr[i]

    for num, strike, ball in question:
        tmp_s, tmp_b = 0, 0
        aa, bb, cc = map(int, list(str(num)))
        
        # 2. 조건문으로 스트라이크와 볼을 가린다.
        # if: 스트라이크, elif: 볼
        # 백의 자리 수
        if aa == a:
            tmp_s += 1
        elif aa == b or aa == c:
            tmp_b += 1
        
        # 십의 자리 수
        if bb == b:
            tmp_s += 1
        elif bb == a or bb == c:
            tmp_b += 1
            
        # 일의 자리 수
        if cc == c:
            tmp_s += 1
        elif cc == a or cc == b:
            tmp_b += 1
            
        # 3. 조건에 맞지 않다면, 이번 경우는 실패
        if strike != tmp_s or ball != tmp_b:
            check[i] = False
            break
print(sum(check))

'''
# 만약에, str로 한다면?
arr = list(permutations(list(map(str, range(1, 10))), 3))
question = [input().split() for _ in range(int(input()))]
aa, bb, cc = list(num)
int(strike), int(ball)
'''

'''
# 결과
메모리: 31256 KB
시간: 44 ms
코드 길이: 872 B
'''