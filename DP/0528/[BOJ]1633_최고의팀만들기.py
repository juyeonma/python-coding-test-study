# import sys
# input = sys.stdin.readline

# black = []
# white = []
# same = []
# while True:
#     try:
#         a, b = map(int, input().split())
#         if a < b:
#             black.append(b)
#         elif a == b:
#             same.append(a)
#         else:
#             white.append(a)
#     except:
#         black.sort(reverse=True)
#         white.sort(reverse=True)
#         while len(black) < 15:
#             black.append(same[0])
#             del same[0]
#         while len(white) < 15:
#             white.append(same[0])
#             del same[0]
#         total = 0
#         for i in range(15):
#             total += black[i] + white[i] 
#         print(total)
#         sys.exit(0)

# 35%에서 valueerror 오류...
# dp로 풀지 않아서 그런가보다.. => 길이 관련해서 에러가 생길 수 있음..

# 참고 : https://great-park.tistory.com/129
import sys
input = sys.stdin.readline
dp = [[0] * 16 for _ in range(16)]

while True:
    try:
        white, black = map(int, input().split())
        # w = 백 선수의 수, b = 흑선수의 수
        for w in range(15, -1, -1):
            for b in range(15, -1, -1):
                if w != 0:
                    # 백 선수 영입 x VS 영입 o
                    dp[w][b] = max(dp[w][b], dp[w-1][b] + white)
                if b != 0:
                    # 흑 선수 영입 x VS 영입 o
                    dp[w][b] = max(dp[w][b], dp[w][b-1] + black)
    except:
        print(dp[15][15])
        break