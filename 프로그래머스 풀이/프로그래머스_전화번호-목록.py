'''
# 프로그래머스_전화번호 목록.py. Lv 2. 풀이: 23.06.07

# How to
- 입력 list를 오름차순 정렬하면,
    - 동일한 문자열 순서로 이루어진 두 값은 연속될 수 밖에 없다.
    - 즉, 연속된 두 값만 비교하면 된다.

## 반례
- 중간에 문자열이 있는 경우!    
    - 따라서, 단순히 a in b 로는 접두사임을 구분할 수 없다.
["123", "3123"]
답: true

# Review
- 처음에 a in b로 풀었는데, 틀려서 당황했다. 다시 문제를 보니.. '접두사' 였다. 
즉 단순히 포함으로는 안되고, 문자열의 시작을 살펴봐야했다.
- 그 다음에는 startswith로 푸는데, 자꾸 효율성 테스트 3, 4번에서 시간초과가 떴다.
    - 질문게시판을 보니, sort 정렬의 기본을 참고하라고 해서, 성공!
'''

# Code
def solution(phone_book):
    # 오름차순 정렬
    phone_book.sort()
    
    # i+1과 i를 비교해야하므로, i의 범위는 n-2까지만.
    for i in range(len(phone_book)-1):
        # i+1번째 원소가 i번째 원소로 시작한다면, 즉 접두사 관계라면
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        
    # 접두사 관계가 없다면,
    return True
'''
# Result
풀이 시간: 30분

## 정확성 테스트
테스트 20 〉통과 (1.20ms, 10.3MB)

## 효율성 테스트
테스트 3 〉통과 (165.15ms, 30.6MB)
'''