'''
# 백준_2629_양팔저울. 골드 3. 풀이: 23.07.27 -> 성공 -> 다시 풀기

# How to
- 저울은 한번만 사용 가능

- 저울에서 무게를 재는 방법은 두가지
    - 한쪽엔 추, 한쪽엔 구슬
    - 한쪽엔 추, 한쪽엔 구슬+추

## 1. DP는 아니지만, 성공
- 먼저 추의 조합을 모든 추의 합을 길이로 하여 리스트로 만든다.
- dfs를 써서, 추의 조합을 리스트에 담는다. 
    - 조합의 원소들(즉 사용된 추 리스트) 집합, 비교 가능(True)로 기록
- 구슬을 탐색한다.
    - 구슬이 모든 추의 합을 넘는다면, N
    - 구슬과 같은 무게의 추가 존재한다면, Y 
    - 추 조합 리스트에서 하나씩 원소를 꺼내면서, 구슬과 더해본다.
        - 즉 추(i) == 구슬+추(target+i) 인지 비교한다.
        - 추와 구슬+추가 존재하고(즉, 추 조합 리스트에서 True이고), 양쪽에 사용된 구슬이 중복되지 않는다면, Y

## 2. DP
- 

# 예제
4
20 35 47 3
1
5
- 추의 합: 3, 20, 23, 35, 38, 47, 50, 55, 58, 70, 85, 105
- 정답: 5 + 47 + 3 = 20 + 35 => Y

# Review
- 풀이 시간: 2시간
- 인덱스 에러를 많이 범했는데, 자꾸 value를 index로 착각한.. 사소한 오류에 시간을 많이 쏟아서 당황스럽다..ㅎ
- 1번 풀이는 성공했지만, dp가 아니다. 맞힌 사람 풀이를 보니, 내가 괜히 중복을 피한답시고 코드를 복잡하게 만들었다는걸 깨달았다.
    - 나는 우선 추를 더하는 조합만 기록하고, 매번 구슬을 비교했다.
    - 그런데 다른 사람들의 코드를 보니, 가능한 무게를 모두 기록한 다음에 입력된 무게를 판별하는게 더 간단한 풀이였다.
- 다시 DP로 풀어야겠다.
'''

# Code
# 1. DP는 아니지만, 성공
## 메모리: 35348 KB, 시간: 464 ms
# 추 n개, 추 list: 오름차순. 중복 가능
n = int(input())
weight_list = list(map(int, input().split()))

# 구슬 m개, 구슬 list.
m = int(input())
target_list = list(map(int, input().split()))

# 추 무게의 합 리스트: 사용된 추 집합, 비교 가능 여부
max_target = sum(weight_list)
result = [[set(), False] for _ in range(max_target+1)]

# 추의 무게 조합을 기록
def combination(idx, combi):
    global result

    # 범위를 넘었다면, return
    if idx == n:
        return
    
    # 저장한 적 없다면, 
    if not result[sum(combi)][1]:
        result[sum(combi)] = [set(combi), True]
    
    # 같은 무게의 추가 중복으로 주어질 수 있으므로, 중복 거르기
    overlap = 0
    for i in range(idx+1, n):
        if overlap != weight_list[i]:
            overlap = weight_list[i]
            combination(i, combi+[weight_list[i]])

# 각각의 추를 처음으로 포함하여 조합 구하기
for idx in range(n):
    combination(idx, [weight_list[idx]])

def solve(target):
    # 저울로 구할 수 없는 무게라면,
    if target > max_target:
        return 'N'
    
    # 구슬 = 추라면, return
    if result[target][1]:
        return 'Y'
    
    # 구슬 + 추의 값이 추 무게의 합의 최댓값을 넘으면 안되므로,
    for i in range(1, max_target+1-target):
        # 추(i) == 구슬+추(target+i) 인지 비교
        # 추가 존재하고, 구슬 + 추가 존재하고, 사용된 추가 겹치지 않는다면,
        if result[i][1] and result[target + i][1] and not (result[i][0] & result[target + i][0]):
            return 'Y'
        
    # 저울로 구할 수 없는 구슬일 경우,
    return 'N'

answer = []
for target in target_list:
    answer.append(solve(target))
    
print(*answer)
