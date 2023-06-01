import sys
input = sys.stdin.readline
n = int(input())
color = input().rstrip()
# 그냥 split()만 했을 때 빈문자열 생김
# 생기는 이유 : https://www.acmicpc.net/board/view/89882
# 빈 문자열 제거 방법 : https://jinmay.github.io/2019/06/30/python/python-how-to-delete-empty-string-in-list/
blue = ' '.join(color.split('R')).split()
red = ' '.join(color.split('B')).split()

print(min(len(blue), len(red))+1)

# 메모리 : 44084KB, 시간 : 84ms

# 훨씬 간단한 방법(주연님 풀이 참고..!)
# count('RB'), count('BR') 비교 => 전에 봤었던 방법이었다...