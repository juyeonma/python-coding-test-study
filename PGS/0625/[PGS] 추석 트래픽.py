# 전에 풀었던 강의실 배정? 그문제랑 똑같은 것 같다 비슷한가?
# 테스트 케이스는 통과가 되는데 3번 18번이 통과가 안된다.
# 주석으로 된 로직이 3,18 통과가 안된든 로직인데 왜그럴까?

# 요즘 멘탈이 안좋아서 문제를 잘못 읽어서 그냥 답을 볼까 하다가 다시 알것 같아서 풀어보았다 결국 틀리고 답을보긴했지만
# 접근방식은 동일하게 한 것 같다. 하지만 안되는 이유가 무엇인지 모르겠다. 뭐가 다른걸까?..

# 또 초로 시간을 변환하고 소수점은 그대로 두고 계산을 하면 부동소수점 문제가 생긴다.
# 그러므로 모두 그 소수점 이하시간으로 변환해야한다.
# 시간변환만 제외하고는 강의실배정, 단속카메라랑 같은 것 같다


def solution(lines):
    answer = 1
    times = []
    for line in lines:
        a,b,c=line.split()
        h=int(b[:2])
        m=int(b[3:5])
        s=int(b[6:8])
        ms=int(b[9:])
        
        duration_time = float(c[:-1])
        en_time = (h*60*60 + m*60 + s)*1000 + ms
        st_time = en_time+1-(duration_time*1000)
        
        times.append([st_time,en_time])
    
    # for i in range(len(times)):
    #     temp=0
    #     en = times[i][1]
    #     j=i
    #     while j<len(times) and en+1000>times[j][0]:
    #         temp+=1
    #         j+=1
    #     answer=max(answer,temp)
    for i in range(len(times)):
        en = times[i][1]
        temp=0
        for j in range(i,len(times)):
            if en+1000 > times[j][0]:
                temp+=1
        answer = max(temp,answer)
    return answer