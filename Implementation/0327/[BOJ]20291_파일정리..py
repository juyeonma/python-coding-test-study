# .으로 확장자 구분
# 딕셔너리 사용?!
import sys
input = sys.stdin.readline
n = int(input())
dic = {}
for i in range(n):
    s = input().rstrip().split('.')
    if s[-1] in dic.keys():
        dic[s[-1]] += 1
    else:
        dic[s[-1]] = 1
dic = sorted(dic.items())
for i, j in dic:
    print(i, j)
