#다시 풀기
n,m,k = map(int,input().split())
fire=[]
for _ in range(m):
    fire.append(list(map(int,input().split())))

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
gragh=[[[] for _ in range(n)] for _ in range(n)]
for _ in range(k):
    while fire:
        cr,cc,cm,cs,cd=fire.pop(0)
        nr = (cr+cs * dx[cd])%n
        nc=(cc+cs * dy[cd])%n
        gragh[nr][nc].append([cm,cs,cd])
        
    for i in range(n):
        for j in range(n):
            if len(gragh[i][j])>1:
                sum_m,sum_s,cnt_odd,cnt_even,cnt=0,0,0,0,len(gragh[i][j])
                while gragh[i][j]:
                    mm,ss,dd=gragh[i][j].pop(0)
                    sum_m += mm
                    sum_s += ss
                    
                    if dd%2:
                        cnt_odd+=1
                    else:
                        cnt_even+=1
                print(sum_m,sum_s, cnt_even,cnt_odd)
                if cnt_odd==cnt or cnt_even==cnt:
                    nd=[0,2,4,6]
                else:
                    nd=[1,3,5,7]
                if sum_m//5:
                    for d in nd:
                        fire.append([i,j,sum_s//5,sum_s//cnt,d])
                print(sum_s,sum_s//5)
            if len(gragh[i][j])==1:
                fire.append([i,j]+gragh[i][j].pop())
    print(fire)
print(sum([f[2] for f in fire]))