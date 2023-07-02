key=['qwertyuiop','asdfghjkl','zxcvbnm']
mo='yuiophjklbnm'
l,r = map(str,input().split())
string = input()

xl,yl,xr,yr=None,None,None,None

time=0
for i in range(len(key)):
    if l in key[i]:
        xl = i
        yl=key[i].index(l)
    if r in key[i]:
        xr = i
        yr = key[i].index(r)
    #print(xl,yl,xr,yr)
    
for s in string:
    time+=1
    if s in mo:
        for i in range(len(key)):
            if s in key[i]:
                nx=i
                ny=key[i].index(s)
                time+=abs(nx-xr)+abs(ny-yr)
                xr,yr=nx,ny
                #print(xr,yr,time)
                break
    else:
        for i in range(len(key)):
            if s in key[i]:
                nx=i
                ny=key[i].index(s)
                time+=abs(nx-xl)+abs(ny-yl)
                xl,yl=nx,ny
                #print(xl,yl,time)
                break
print(time)
# 메모리 : 31256 KB
# 시간 : 40 ms
# 코드길이 : 889 B