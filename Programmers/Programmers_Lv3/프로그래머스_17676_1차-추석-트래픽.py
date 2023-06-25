'''
# 프로그래머스_17676_[1차] 추석 트래픽. Lv 3. 풀이: 23.06.25 -> 실패

# How to

## 반례

# Review
- 아이디어가 도저히 떠오르지 않았다.
    - 시간을 어떻게 추출하지? datetime을 이용해봤는데, 계속 실패했다.
    - 처리 구간을 어떻게 구하지? 시작시간과 끝시간을 포함해야하는데, 어떻게 처리하지?
    - 구간이 정해져있지 않고, '1초' 단위인데, 이걸 어떻게 개수를 세지?
- 어떤 유형인지 모르겠다. 정렬? 아님 그냥 구현?
'''

#  실패 Code
# from datetime import datetime
# def solution(lines):
#     answer = 0
    
#     for i in lines:
#         _, response_time, processing_time = i.split()
#         response_time = datetime.strptime(response_time, "%H:%M:%S.%f")
#         # processing_time = datetime.strptime(str(float(processing_time[:-1])), "%S.%f")
#         processing_time = float(processing_time[:-1])
#         print(response_time, processing_time)
#         print(response_time- datetime.strptime(str(processing_time), "%S.%f"))
#         break
#     return answer
# # print(solution(["2016-09-15 01:00:04.001 2s"]))


'''
# Result
풀이 시간:

'''