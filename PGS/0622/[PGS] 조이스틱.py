# 알파벳 이동 위치는 커서를 어떻게 이동하든 최솟값은 동일하다
# 중요한건 커서를 어떻게 이동하느냐이다
# 그냥 쭉 지나가면서 알파벳을 바꾸면 A가 연속일때 비효율적인 결과가 나올 수 있다.
# 

def solution(name):
    answer = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    temp=0
    for s in name:
        idx=alphabet.index(s)
        temp += min(idx,26-idx) 
    i=0
    answer = len(name)-1
    
    while i<len(name):
        next=i+1
        while next < len(name) and name[next]=="A":
            next+=1
        answer = min(answer,2*i + len(name)-next , i+2*(len(name)-next))
        i=next
    return answer+temp