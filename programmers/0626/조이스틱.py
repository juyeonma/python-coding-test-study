#문제부터 이해가 부족,, 다시 보기!
def solution(name):
    answer = 0
    l = len(name)-1
    
    for i,c in enumerate(name):
        answer+=min(ord(c)-ord('A'), ord('Z')-ord(c)+1) #현재 알파벳 변경 최솟값
        
        next = i+1 #다음글자로 넘어감
        #무슨 뜻이지,,
        while next<len(name) and name[next]=='A':
            next+=1
        l = min([l, 2*i+len(name)-next, i+2*(len(name)-next)])
        
    answer+=l
    return answer