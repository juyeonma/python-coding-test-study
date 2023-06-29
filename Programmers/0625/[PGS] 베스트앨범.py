# 너무 생각할수록 복잡해졌던 문제..
# 인터넷 참고 풀이
# defaultdict 처음 알았다..
from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genres_order = defaultdict(int)
    genres_plays = defaultdict(list)
    
    for i, (genre, v) in enumerate(zip(genres, plays)):
        genres_order[genre] += v
        genres_plays[genre].append((i, v))
        
    for genre, _ in sorted(genres_order.items(), key = lambda x: x[1], reverse = True):
        for i, v in sorted(genres_plays[genre], key = lambda x: x[1], reverse = True)[:2]:
            answer.append(i)
    
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])