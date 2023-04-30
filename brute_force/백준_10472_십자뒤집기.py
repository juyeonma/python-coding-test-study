'''
# 백준_10472_십자뒤집기. 실버 2. 풀이: 23.04.27 실패

# 풀이방법
'''
'''
# 보완할 것
- 9079_동전 게임과 거의 유사하다.
- 즉, 이진법, 비트마스킹을 이용해야한다. 덧붙어 백트래킹(BFS)로 풀이해야한다.
- 완전 탐색 문제에서 은근히 비트마스킹이 많이 나오는 듯 하다. 동전과 같이 1과 0으로 표현할 수 있는 경우, 이진법으로 표현 가능하기 때문이다.
- 비트 연산자를 더 공부하자.
- 근데, 실버가 이렇게 어렵다니..
- 다음 스터디날에 발표할 수 있도록 꼭! 이해하자!
'''

# 풀이 기록
# import sys
# input = sys.stdin.readline

# n = 0b111111111
# print(format(n, '#d'))
# print(n)
# print(int('111111111', 2))
# print(2**9)
# print(3<<3)

# t = bin(9 ^ 5).count('1')
# print(9 ^ 5)

# for i in [7,56,448,73,146,292,273,84]:
#     print(f'{i}: {bin(i)}')
# from itertools import product
# for flip_operations in product(range(2), repeat=5):
#     print(flip_operations)
'''
# 결과
메모리:  KB
시간:  ms
코드 길이:  B
'''