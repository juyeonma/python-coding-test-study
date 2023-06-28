#시간초과
import sys
input=sys.stdin.readline()
# n,m = map(int, input().split())
# hear=[]

# ans = []
# for _ in range(n):
#     hear.append(input())

# for _ in range(m):
#     see=input()
#     if see in hear:
#         ans.append(see)

# print(len(ans))
# for i in ans:
#     print(i)

#set,list활용
n,m = map(int, input().split())
hear=set()
see = set()
for _ in range(n):
    hear.add(input())

for _ in range(m):
    see.add(input())

ans = sorted(list(hear&see))   #교집합을 의미함
print(len(ans))
for i in ans:
    print(i)
    
# 메모리 : 44060 KB
# 시간 : 4104 ms
# 코드길이 : 212 B
