# 어떻게 풀어야할지 몰라서...
# n이 15개로 적으니깐.. 진짜 다 대입해볼까.. 생각했었음..ㅎㅎ...
# 근데 너무 많아져서 포기..
# def solution(n):
#     answer = []
#     if n == 1:
#         answer.append([1, 3])
#     if n == 2:
#         answer = [[1, 2], [1, 3], [2, 3]]
#     if n == 3:
#         answer = [[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]]
#     return answer


# 하노이 탑에 대해서 검색..
# 참고 : https://gusdnd852.tistory.com/96
def hanoi(n, f, b, t, answer):
    if n == 1:
        answer.append([f, t])
    else:
        hanoi(n - 1, f, t, b, answer)
        answer.append([f, t])
        hanoi(n - 1, b, f, t, answer)


def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer


# 규칙을 찾을 수 있었을 것 같은데.. 파악하지 못해서 너무 아쉬웠다
# 다시 풀 문제
