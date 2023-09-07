'''
# 프로그래머스_49993_스킬트리. Lv 2. 풀이: 23.09.05

# How to
- 주어진 스킬들을 살피면서, 선행 스킬의 개수와 순서가 맞는지 확인한다.
- 선행 스킬을 만나면, 임시 선행 스킬 목록에 추가한다.
    - 임시 선행 스킬 목록의 개수와 현재 만난 선행 스킬의 인덱스가 같아야 한다.
    - 예: 0번째 선행 스킬이라면, 현재 임시 선행 스킬 목록의 개수도 0이고, 인덱스도 0

# Review
- 풀이 시간: 20분
- 차근차근 풀기에 무난한 구현 문제였다.
'''

# Code
# 1. 구현: 성공
## 합계: 100.0 / 100.0
## 정확성 테스트 5 〉 통과 (0.02ms, 10.2MB)
def solution(skill, skill_trees):
    answer = 0
    pre_skill = set(skill)
    # 스킬 트리 목록을 살피면서
    for word in skill_trees:
        tmp = []
        flag = True
        # 현재 스킬 트리의 스킬들을 살피면서
        for now_skill in word:
            # 현재 스킬이 선행 스킬 트리에 속한다면,
            if now_skill in pre_skill:
                # 선행 스킬 개수가 맞다면, 선행 스킬 목록(tmp)에 추가
                if len(tmp) == skill.index(now_skill):
                    tmp.append(now_skill)
                    
                # 선행 스킬 개수가 안 맞다면, 불가능한 스킬트리 -> flag 표시 및 다음 스킬 트리로 넘어감
                else:
                    flag = False
                    break
                
        # 모든 선행 스킬 순서가 맞다면, 정답 +1
        if flag:
            answer += 1
                    
    return answer

