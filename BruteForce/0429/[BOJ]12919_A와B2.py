import sys
input = sys.stdin.readline

s = str(input().rstrip())
t = str(input().rstrip())


# 1. 나눠서 함수를 해야하나 생각해봄
# 2. 근데 그러면 재귀가 이상해져서 해결하지 못함

# 처음 생각한 답안
# def solve1(s, t):
#     if len(s) == len(t):
#         return False
#     else:
#         s += 'A'
#         if t == s:
#             print(1)
#             sys.exit(0)
#         solve1(s, t)
#         s = s[:-1]
#         solve2(s, t)


# def solve2(s, t):
#     if len(s) == len(t):
#         return False
#     else:
#         s += 'B'
#         s = s[::-1]
#         if t == s:
#             print(1)
#             sys.exit(0)
#         solve1(s, t)
#         s = s[::-1]
#         s = s[:-1]
#         solve2(s, t)


# solve1(s, t)
# solve2(s, t)

# print(0)

# 참고 : https://bio-info.tistory.com/161

# 핵심 : s를 t로 바꾸는게 아니라, t를 s로 바꾸는 것

# 메모리 :31256KB 시간 : 40ms
def dfs(t):
    # t와 s가 같다면 1 출력 후 종료
    if t == s:
        print(1)
        sys.exit()
    # t 리스트에서 문자열을 재귀적으로 제거하다가 모두 제거된 경우로 return 0을 통해 해당 함수 종료
    if len(t) == 0:
        return 0
    # 마지막이 'A'라면 'A' 제거 후 재귀 호출
    if t[-1] == 'A':
        dfs(t[:-1])
    # 첫번째가 'B'라면, 이를 제외하고 뒤집어서 재귀 호출
    if t[0] == 'B':
        dfs(t[1:][::-1])


dfs(t)
print(0)
