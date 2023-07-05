# 앞에서부터 이동, 뒤에서부터 이동
# 같은지 확인 >> 다 같으면 0
# 다르면 각 경우의 요소를 뺐을 때 같은지를 확인하면 된다

t = int(input())
for _ in range(t):
    s=input()
    st=0
    en=len(s)-1
    while st<=en:
        if s[st]==s[en]:
            st+=1
            en-=1
        else:
            break
    else:
        print(0) # 회문이라면 0
        continue
    
    temp1=s[:st]+s[st+1:] # st 요소 삭제했을 때 같은지
    temp2=s[:en]+s[en+1:] # en 요소 삭제했을 때 같은지
    
    if temp1==temp1[::-1] or temp2==temp2[::-1]: # 두 경우 중 하나가 같다면 유사회문 
        print(1)
    else: # 삭제해도 같지 않다면 아무것도 아니다
        print(2) 


# 18분
# 31448kb 272ms

