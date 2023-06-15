# 시간 복잡도 : O(nlogn)
# 어떤 알고리즘? Greedy
# 풀이 시간 : 25분

# 가장 많이 나온 숫자만큼 빼주기 => Greedy라고 생각
def solution(k, tangerine):
    answer = []
    size = {}
    for t in tangerine:
        if t in size:
            size[t] += 1
        else:
            size[t] = 1
    
    size = sorted(size.items(), key = lambda x : -x[1])
    for i, j in size:
        if k <= j:
            answer.append(i)
            break
        else:
            k -= j
            answer.append(i)
    # print(answer)
    return len(answer)

# 시간(제일 빠른 시간, 제일 느린 시간만 가져옴)
# 테스트 12 〉	통과 (0.00ms, 10.3MB)
# 테스트 27 〉	통과 (47.24ms, 26.3MB)


# 짧은 풀이 : Counter 함수의 응용..
# Counter => 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지 저장된 객체를 얻음
# Counter 자세한 설명 : https://www.daleseo.com/python-collections-counter/
# 함수 응용 잘하기!
import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer
