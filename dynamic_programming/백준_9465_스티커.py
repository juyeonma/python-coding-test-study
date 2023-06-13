# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s=[]
#     for i in range(2):
#         s.append(list(map(int, input().split())))
    
#     #이 식을 뺴니까 안됐다.. 왜인거지
#     s[0][1]=s[1][0]+s[0][1]
#     s[1][1]=s[0][0]+s[1][1]
#     for i in range(2,n):
#         s[0][i]=s[0][i]+max(s[1][i-1],s[1][i-2]) #
#         s[1][i]=s[1][i]+max(s[0][i-1],s[0][i-2])
#     print(max(s[0][-1],s[1][-1]))
    

t = int(input())

for _ in range(t):
    n = int(input())
    s=[]
    for i in range(2):
        s.append(list(map(int, input().split())))
    
    
    for i in range(1,n):
        if i==1:
            s[0][1]=s[1][0]+s[0][1]
            s[1][1]=s[0][0]+s[1][1]
        else:
            s[0][i]=s[0][i]+max(s[1][i-1],s[1][i-2]) #현재 위치에서 대각선 한칸 왼쪽, 대각선 두칸 왼쪽을 비교하면 된다.
            s[1][i]=s[1][i]+max(s[0][i-1],s[0][i-2])
    print(max(s[0][-1],s[1][-1]))
    
# 코드길이 : 453 B
# 시간 : 760 ms
# 메모리 : 40168 KB