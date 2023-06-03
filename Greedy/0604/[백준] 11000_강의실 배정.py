# 진짜 꾸역꾸역 풀었다..
# 이번 문제 중 가장 어려웠던 것 같다.
# 나는 종종 내 방식대로 문제를 풀게 되는 것 같다.. 이것도 좋은 것 같지만 정석대로 풀고 싶다..ㅠㅠ

# 나는 순간순간 경우에서 겹치는 강의의 최대를 구했고
# 검색했을 때 보이는 풀이들은 마지막까지 우선순위큐에 남아있는 요소의 개수로 구했는데 어떻게 이렇게 생각할 수 있는걸까...

# 여러가지 경우들을 그려보면서 풀 수 있는 방법을 찾아봤는데
# 강의 끝나는 시간 기준으로 정렬하여 가장 먼저 끝나는 강의 순으로 시작시간과 끝나는 시간에 가장 빠른 인덱스를 부여한다.
# 그 다음 늦게끝나는 시간에는 그다음 인덱스를 부여한다.
# 이 인덱스는 우선순위 큐에 사용하려고 부여하였다.
# 그 다음 강의 시작시간, 끝나는 시간 구분 없이 오름차순으로 정렬한다.
# for문으로 돌면서 해당 인덱스를 힙큐에 넣고 길이를 잰다
# 같은 인덱스가 들어갈 경우 같은 강의의 끝나는 시간을 의미하므로 힙큐에서 빼준다.
# 다른 인덱스가 들어가면 다른 강의 시간이 겹친다는 뜻이므로 다시 길이를 잰다
# 이렇게 모든 시작시간, 끝나는 시간을 탐색한 후 최대 시간을 출력한다.

# 일반적인 풀이를 봤는데 어떻게 이렇게 생각할 수 있을까 싶었다...

import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[1]) # 끝나는 시간 기준으로 정렬
temp=[]
for i in range(len(arr)):   
    temp.append((arr[i][0],i))  # 시작시간과 우선순위큐에 사용할 인덱스 부여
    temp.append((arr[i][1],i)) # 끝나는 시간과 우선순위큐에 사용할 인덱스 부여
temp.sort() # 시간순으로 정렬
max_room=0
heap=[]
for time,idx in temp:   
    if not len(heap):   # 배열이 비어있을떄, 즉 첫번째 시간이 들어올때
        heapq.heappush(heap,idx)    # 해당시간의 인덱스 넣기
        max_room=max(max_room,len(heap))    # 힙의 크기 == 해당시간에서 필요한 강의실 수
    else:
        if heap[0]==idx:    # 끝나는시간일 때 해당강의의 시작시간의 index는 pop
            heapq.heappop(heap) # 여기서는 pop인 부분이라 어차피최대보다 작을테니 따로 max연산을 안했음
        else:   
            heapq.heappush(heap,idx) # 다른 시작시간이라면 push
            max_room=max(max_room,len(heap))    # 해당시간대에서의 강의실 개수 갱신
print(max_room)


# 메몰 109864kb 시간 684ms
# 걸린시간은 힙큐 공부하다가 제대로 못쟀다.. 오래걸린 건 확실하다..