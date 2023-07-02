t = int(input())
# 문자 앞 뒤에서 탐색하다가 다른 문자가 나왔을 때, 그것을 제거하고 다시 탐색하기 위한 것
def check(s,l,r):
    while l<r:
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            return False
    return True

for _ in range(t):
    s = input()
    l=0
    r=len(s)-1
    ans=0
    while l<r:
        if s[l]==s[r]: #앞뒤가 같으면 다음 문자를 탐색
            l+=1
            r-=1
        else: #앞 뒤 문자가 달랐을때 그 문자를 제거하고 다시 탐색
            ll=check(s,l+1,r)
            rr=check(s,l,r-1)
            if (ll or rr): #ll,rr 모두 true라는 뜻으로 유사 회문
                ans=1
            else: #또 다시 다른 문자가 나왔다면 그것은 유사 회문도 아님
                ans=2
            break
    print(ans)
    
# 메모리 : 31256 KB
# 시간 : 304 ms
# 코드길이 : 498 B