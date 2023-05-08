'''
# 백준_3085_사탕 게임. 실버 2. 풀이: 23.05.04 -> 실패

# 풀이방법
- 경우의 수
교체 0번
교체 1번
교체 2번 -> 갱신 후, 교체 1번.

- 풀이
    - 행별 list, 열별 list와 알파벳, 행, 열별로 for문을 돌린다
    - 맞는 알파벳일때와 다른 알파벳일때, 교체 가능 여부, 이미 교체했는지 여부의 if문으로 나눈다.
    - 이전 길이, 지금 길이, 교체 여부를 표시한다.
    - 그리고 갱신.

# 반례
6
CCYYCC
YYCCYY
CCYYCC
YYCCYY
CCYYCC
YYCCYY

3
'''

'''
# 보완할 것
- 풀릴듯 안 풀릴듯 미치겠다. 질문게시판의 모든 반례를 통과해도 70%에서 틀린다.
- 그래서 다시 코드를 정비했으나, 이번에는 30%에서 틀린다.
- 설령 이 코드로 맞는다고 하더라도, 4중 for문과 난잡한 if문으로.. 코드가 이쁘지 않다.
'''

# 풀이 기록
# C, P, Z, Y
n = int(input())

arr_row = [list(input()) for _ in range(n)]
arr_col = list(map(list, zip(*arr_row)))

answer = 0
for arr in [arr_row, arr_col]:
    for a in ['C', 'P', 'Z', 'Y']:
        for i in range(n):
            # 이전 길이, 지금 길이
            before, now, flag = 0, 0, False
            for j in range(n):
                # 맞는 알파벳일 때
                if arr[i][j] == a:
                    now += 1
                    
                # 다른 알파벳 일 때
                else:
                    # 교체 가능하다면,
                    if (i-1 >=0 and arr[i-1][j] == a) or (i+1 < n and arr[i+1][j] == a):
                        # 갱신할 길이가 있다면, 즉 이미 한번 교체 했다면,
                        # 갱신 후 다시 시작.
                        if flag:
                            answer = max(answer, before+1+now)
                            
                        # 갱신할 길이가 없다면, 즉 교체한적 없다면,
                        # 계속 진행
                        before = now
                        flag = True


                    # 교체 불가능 하다면, 갱신 및 초기화.
                    else:
                        if flag:
                            answer = max(answer, before+1+now)
                        else:
                            answer = max(answer, now)
                        before = 0

                    now = 0

            answer = max(answer, now)  
              
print(answer)

'''
# 결과
메모리:  KB
시간:  ms
코드 길이:  B
'''