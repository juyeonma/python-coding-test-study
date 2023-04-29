import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input().rstrip())

data = list(map(int, input().split()))

# 조합을 통해 모두의 수를 구하면 된다고 생각!
# 하지만, 예제들이 이해되지 않았음
# t = []
# for i, j, k in list(combinations(data, 3)):
#     if i + j > k and j + k > i and i + k > j:
#         t.append((i, j, k))

# print(t)


# 참고 : https://ongveloper.tistory.com/332
# 참고 : https://kau-algorithm.tistory.com/970
# 참고 : https://door-of-tabris.tistory.com/entry/%EB%B0%B1%EC%A4%80-1548%EB%B2%88-%EB%B6%80%EB%B6%84-%EC%82%BC%EA%B0%81-%EC%88%98%EC%97%B4%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 찾아보니 이 문제의 쟁점
# 1. 만약 세 수가 있다면 작은 수 + 그 다음 작은수 > 가장 큰 수의 관계를 만족해야하마
# 2. 가장 긴 부분 삼각 수열의 길이란? 인덱스를 뜻하는 거였다..
# 3. 주어진 수열의 길이가 2이하라면, 항상 삼각 수열
# 4. 즉, 주어진 수열의 길이가 3이상인 경우 결과값의 최솟값은 2임을 의미

# 즉 조합은 필요하지 않았다.

# 메모리 : 31256KB 시간 : 40ms
data.sort()
if n > 2:
    result = 2
    for start in range(n-2):
        end = start + 2
        while True:
            if data[start] + data[start+1] > data[end]:
                result = max(result, end-start+1)
                end += 1
                if end == n:
                    break
            else:
                break
    print(result)
else:
    print(n)


# 고쳐야할점
# 예제도 이해가 가지 않는다면 혼자 생각하지 말고
# 문제 설명은 바로바로 찾아보기!
