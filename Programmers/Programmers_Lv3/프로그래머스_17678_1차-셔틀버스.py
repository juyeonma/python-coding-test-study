'''
# 프로그래머스_17678_ [1차] 셔틀버스. Lv 3. 풀이: 23.09.05

# How to
- 버스 막차에 마지막 좌석에 탑승하는게 목표
- 방법:
1. 셔틀버스 도착 시간을 모두 구한다.
2. 셔틀버스 도착시간을 탐색하면서, 탑승객의 도착시간을 비교한다.
    - 버스보다 탑승객 도착시간이 빠르다면, 탑승 하고 마지막 탑승객의 도착시간을 갱신
    - 대기줄에 사람이 없거나 만차인 경우, 버스 출발
    - 버스가 출발하고, 남은 좌석 기록
3. 막차에 탑승하기
    - 좌석이 남았다면, 마지막 좌석 탑승
    - 만차라면, 마지막 탑승객보다 1분 더 빨리타기


## 반례
- 뭘까..?


# Review
- 풀이 시간: 1시간 30분
    - 처음에 문제를 바로 이해하지 못해서, 20분간 붙잡다가 다른 문제로 넘어갔다.
    - 다른 문제를 모두 푼 이후에 다시 돌아왔지만, 여전히 이해와 구상에 오래걸렸다..
    - 결국 제한된 시간내에 모두 풀지 못하고, 반례에서 실패.
- 문자열 parsing은 늘 어렵다.
    - 단순히 문자열을 나누는것 보다는 코드가 너무 지저분해져서 어렵다.
- 반례가 뭘까?
    - 매우 지저분하지만, 어찌어찌 풀었다고 했는데 반례를 다 틀렸다.
'''

# Code
# 1. 실패
## 합계: 79.2 / 100.0 -> 테스트 5, 13, 21, 22, 24 실패
## 메모리:  KB, 시간:  ms
def trans_time(now, answer_time, minus_time=0):
    # str라면 -> 시간, 즉 int로 변환
    if type(now) == str:
        now = int(answer_time[-1][:2]) * 60 + int(answer_time[-1][3:])
    # 원하는 만큼 시간을 빼고,
    now -= minus_time
    # 00:00 형식의 str로 반환
    return ("0"+str(now//60))[-2:] + ":" + ("0"+str(now%60))[-2:]

def solution(n, t, m, timetable):
    # 셔틀버스 도착 시간 리스트
    now = 540
    arival_time = ["09:00"]
    for _ in range(1, n):
        now += t
        arival_time.append(trans_time(now, []))
    
    # 대기인원 오름차순 정렬
    timetable.sort()
    
    # 셔틀버스 도착시간별 남은 좌석 리스트
    answer_cnt = [0] * n
    answer_time = [0] * n
    
    start = 0
    for idx, arive in enumerate(arival_time):
        cnt = m
        for i in range(start, len(timetable)):
            # 탑승
            if timetable[i] <= arive:
                cnt -= 1
                # 마지막 탑승객 기록 갱신
                answer_time[idx] = timetable[i]
                
            # 대기줄에 사람이 없거나 만차인 경우, 버스 출발
            if timetable[i] > arive or cnt == 0:
                start = i
                break
                
        # 남은 좌석 기록        
        answer_cnt[idx] = cnt
        
    # 막차에 좌석이 남았다면, 막차 타기
    if answer_cnt[-1]: 
        return arival_time[-1]
    
    # 막차에 만차라면, 마지막 탑승객보다 1분 더 빨리타기
    else: 
        return trans_time(answer_time[-1], answer_time, 1)
        