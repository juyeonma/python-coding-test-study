from collections import Counter
s = list(map(str,input()))
s.sort()
count=Counter(s) #각 문자별 갯수세기
cnt=0
al = ''
answer=''
for i in count:
    if count[i]%2 !=0: #문자별 갯수가 홀수라면
        cnt +=1 #홀수 개인 문자 개수 추가
        al += i
    for _ in range(count[i]//2):
        answer+=i #팰린드롬을 위해 반절만큼만 ans에 저장

if cnt>1: #홀수 개의 문자가 1개 이상이면 팰린드롬이 될 수 없다
    print("I'm Sorry Hansoo")
    
elif cnt==0: #0이면 모두 짝수의 개수를 만드는 것이므로 팰린드롬 가능(answer와 거꾸로answer를 붙이면 됨)
    print(answer+answer[::-1])

else: #cnt가 1인 경우, al에는 1개의 문자만 남겨있고, 그것을 기준으로 팰린드롬이 됨
    print(answer+al+answer[::-1])
    
# 메모리 : 34140 KB
# 시간 : 68 ms
# 코드길이 : 361 B
