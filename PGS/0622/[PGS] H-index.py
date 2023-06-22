# 시간 복잡도가 넉넉해서 2중 for문으로 돌렸는데 별로 좋은 풀이는 아닌 것 같다.
# O(n) 으로 끝내는 풀이가 잇을 것 같은데 생각을 못했다

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations),-1,-1):
        a=0
        b=0
        for n in citations:
            if i<n:
                a+=1
            elif i==n:
                b+=1
            else:
                break
        if i-a<=b:
            answer=i
            break
    return answer



 # O(n) 풀이
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0



# O(n)풀이, 미친 풀이
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer