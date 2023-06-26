'''
# 프로그래머스_42579_베스트앨범. Lv 3. 풀이: 23.06.25

# How to
- 우선순위: 많이 재생된 장르 > 많은 재생 횟수 > 낮은 고유 번호
- 딕셔너리를 만듦
    - 장르별 재생횟수 딕셔너리
    - 장르별 곡당 (재생횟수, 고유번호) 리스트가 담긴 딕셔너리
- 우선순위대로 정렬:
    - 재생 횟수 순으로 장르 정렬
    - 해당 장르에서 많은 재생 횟수, 낮은 고유 번호 순으로 정렬
- 노래 두개만 뽑아서 베스트 앨범에 추가


# Review
- 처음에 테스트 케이스 두개를 틀렸는데, 낮은 고유번호 순으로 정렬을 빼먹어서였다.
- 무난한 딕셔너리 문제였다.
'''

# Code
def solution(genres, plays):
    answer = []
    
    n = len(genres)
    # 장르: 재생횟수
    genres_cnt = dict()
    # 장르: (재생횟수, 고유 번호) 리스트
    genres_songs = dict()
    
    for i in range(n):
        if genres[i] in genres_cnt:
            genres_cnt[genres[i]] += plays[i]
            genres_songs[genres[i]].append((plays[i], i))
        else:
            genres_cnt[genres[i]] = plays[i]
            genres_songs[genres[i]] = [(plays[i], i)]
    # 재생 횟수 순으로 장르 정렬
    for genre, _ in sorted(genres_cnt.items(), key=lambda x: -x[1]):
        # 많은 재생 횟수, 낮은 고유 번호 순으로 정렬 후 노래 두개까지 뽑아서 베스트 앨범에 추가
        for _, num in sorted(genres_songs[genre], key=lambda x: (-x[0], x[1]))[:2]:
            answer.append(num)

    '''
    # 원래 아래 코드였는데, 더 간단히 줄인게 위에 코드
    genres_cnt = dict(sorted(genres_cnt.items(), key=lambda x: -x[1]))
    
    for i in genres_cnt:
        songs = sorted(genres_songs[i], key=lambda x: (-x[0], x[1]))
        for j in range(min(2, len(songs))):
            answer.append(songs[j][1])
    '''
    
    return answer


# 다른 사람 코드
# 1. 이중 lambda(일부 수정)
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
        
         # 이중 lambda 대신에 이렇게 해도 됨:
         # sorted(d.keys(), key= lambda x: sum([t[0] for t in d[x]]), reverse = True):
    for g in sorted(d.keys(), key= lambda x: sum(map(lambda y: y[0], d[x])), reverse = True):
        for _, num in sorted(d[g],key= lambda x: (-x[0], x[1]))[:2]:
            answer.append(num)
        
    return answer


'''
# Result
풀이 시간: 30분
테스트 5 〉	통과 (0.07ms, 10.3MB)
'''