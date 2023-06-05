# sort 의 시간복잡도가 logN인줄 알았는데 NlogN이었다...
# 그래서 미뤄뒀던 힙큐를 공부하고 힙큐로 바꿔서 풀었다.
# 풀다가 힙큐공부하느라 시간을 멈춰버렸다...
# 가장 작은 두개의 파일을 합쳐서 갱신후에 다시 최소 파일 두개를 더하는 방식으로 풀면 된다.

# import heapq

# t = int(input())

# def case():
#     input()
#     files =list(map(int,input().split()))
#     result=0
#     while len(files)>1:
#         files.sort(reverse=True)
#         a=files.pop()
#         b=files.pop()
#         files.append(a+b)
#         result+=a+b
#     return result

# for _ in range(t):
#     print(case())

import heapq

t = int(input())

def case():
    input()
    files =list(map(int,input().split()))
    result=0
    heapq.heapify(files)
    while len(files)>1:
        a=heapq.heappop(files)
        b=heapq.heappop(files)
        heapq.heappush(files,a+b)
        result+=a+b
    return result

for _ in range(t):
    print(case())

#메모리 152744kb 시간 5388ms
# 걸린시간 ?? 30분이상??