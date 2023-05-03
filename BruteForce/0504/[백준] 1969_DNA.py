# 문자열의 길이가 50이고 문자열의 각 문자의 위치에는 4개의 문자가 올 수 있으므로 4^50으로 풀 수있다.
# 하지만 시간복잡도가 너무 많이 나와서 시간초과가 나오는건 자명하다
# 다른알파벳의 개수를 구하는것이고, 모든 문자열은 M으로 길이가 같다 
# 그러므로 첫번째 인덱스부터 모든 문자열의 종류를 구분한다.
# 그래서 빈도수가 가장 높으면서 사전순으로 정렬한다.
# 해당 문자를 출력하기 위해 저장하고 해당 문자열과 다른 문자열의 개수를 세서 카운팅한다.
# 모든 문자열을 다 돌고나서 출력한다.

# 그냥 구현해서 풀 수도 있었지만, Counter모듈이랑 most_commom을 사용했던 기억이 있어서 해당 메서드를 검색해서 풀었다.
# Counter를 사용해서 most_common을 하면 빈도수로 무작위 정렬되므로 미리 sort를 한 후 Counter를 사용해야한다.

from collections import Counter

N,M =map(int,input().split())
DNA_list =[input() for _ in range(N)]

answer="" #사전순으로 가장 앞선 문자열
count=0   # DNA중에서 다른 글자의 개수
for i in range(M):  #인덱스 for문
    temp=[]

    for j in range(N):   # dna for문
        temp.append(DNA_list[j][i]) # temp에 첫번째 문자열부터 차례대로 넣기

    temp=sorted(temp) # 정렬
    ans = Counter(temp).most_common() #빈도수순으로 정렬
    answer+=ans[0][0]     # 가장 빈도수 높은 것 문자열을 정답으로 채택
    count+=N-ans[0][1]    # 정답인 문자열과 다른 문자들의 개수 카운팅

print(answer)
print(count)