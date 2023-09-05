#구현만 하겠다는 생각으로 짜서 코드가 난잡해요
#이런식으로 하면 bfs로 풀 수 있겠구나라는 느낌만 가져가주세요

from collections import deque

def solution(begin, target, words):
    answer = 0
    words_set = set(words)
    words_dict = dict()
    queue = deque()
    if target in words_set:
        for word in words:
            words_dict[word]=0
        
        words_dict[begin]=0
        queue.append(begin)
        while queue:
            str = queue.popleft()
            for word in words:
                if words_dict[word]:
                    continue
                cnt=0    
                for i in range(len(str)):
                    if str[i]==word[i]:
                        cnt+=1
                if cnt==len(str)-1:
                    queue.append(word)
                    words_dict[word]=words_dict[str]+1
                    if target == word:
                        return words_dict[target]
    return answer