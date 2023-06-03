'''
# 백준_2212_센서. 골드 5. 풀이: 23.06.01 -> 실패

# How to
- k개의 집중국을 세우는 것은 k-1개의 집단으로 묶는것과 같다.
- 가장 떨어져 있는 센서를 집단의 경계로 하면, 수신 가능영역이 줄어든다.
- 즉 각 집중국별 차이값을 구한 후, 가장 차이값이 큰 k-1개를 제거한 나머지의 합이 곧 정답.

# Review
- 차이값을 이용해야한다고는 생각했는데, 집단을 묶는 것은 생각하지 못했다.
- 아니 쉬운데..왜..어려울까.
'''

# 모범 답안 Code : 32276 KB 48 ms
# 센서 n개, 집중국 k개
n = int(input())
k = int(input())
arr = sorted(map(int, input().split()))
# 집중국이 센서 수보다 많다면, 모든 센서에 집중국을 세운다.
if n <= k:
    print(0)
else:
    # 집중국간의 차이값
    check = [arr[i+1] - arr[i] for i in range(n-1)]
    check.sort()

    # 가장 큰 차이값을 k-1개 제외한 나머지의 합 출력
    # 즉, 차이값 n-1 개 에서 k-1개를 뺸, 즉 n-k개의 원소만 더함
    print(sum(check[:n-k]))


'''
# Result
풀이 시간:
메모리:  KB
시간:  ms
코드 길이:  B
'''