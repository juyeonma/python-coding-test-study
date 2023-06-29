'''
# 백준_1713_후보 추천하기. 실버 1. 풀이: 23.06.29

# How to
- 사진 번호: [추천 횟수, 사진 인덱스] 딕셔너리를 만든다.
- 이미 게시된 경우, 추천 +1
- 게시되지 않은 경우,
    - 비어있는 사진 틀이 없는 경우, 가장 추천이 적고 오래된 사진을 삭제한다.
    - 사진 번호: [1, 인덱스] 형태로 딕셔너리에 담는다.
    
- 모든 작업이 완료된 후, key만 정렬된 상태로 출력한다.

# Review
- 딕셔너리 key 삭제가 기억이 안나서 검색했다.. del과 pop이 가능한데, 이번에는 pop을 사용해봤다.
- 딕셔너리 정렬에서 자꾸 에러가 나서 헤맸다.
    - dic.items()로 정렬할 경우, value값은 인덱스 1이 되기 때문에, value가 list인 경우 그 안에서 다시 인덱스를 적어줘야했다.
'''

# 성공 Code
# 사진틀 n개, 총 추천 횟수 m번
n = int(input())
m = int(input())
# 추천받은 학생들
num = map(int, input().split())

dic = {}

for idx, v in enumerate(num):
    # 이미 게시된 사진일 경우, 
    if v in dic:
        dic[v][0] += 1
    
    # 아직 게시되지 않았을 경우,
    else:
        # 비어있는 사진틀이 없는 경우, 가장 추천이 적고 오래된 사진 삭제
        if len(dic) == n:
            k = min(dic.items(), key=lambda x: x[1])[0]
            dic.pop(k, None)
            
        # 새로운 사진 게시
        dic[v] = [1, idx]

print(*sorted(dic))

'''
# Result
풀이 시간: 20분
메모리: 31256 KB
시간: 44 ms
코드 길이: 485 B
'''