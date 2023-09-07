'''

# 백준_8983_사냥꾼. 골드 4. 풀이: 23.08.21 -> 다시 풀기

# How to

## 반례

# Review
- 풀이 시간:
- 이게 왜 이분탐색이지..?
'''

# Code
# 1.
## 메모리:  KB, 시간:  ms
# 사대 m개, 동물 n마리, 사정거리 l
m, n, l = map(int, input().split())

# 사대의 위치
sadae = list(map(int, input().split()))

# 동물의 위치: x, y
animal = [list(map(int, input().split())) for _ in range(n)]