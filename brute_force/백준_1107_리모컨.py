'''
# 백준_1107_리모컨. 골드 5. 풀이: 23.05.05 -> 실패

# 풀이방법
- 100번에서 시작.
- 숫자 버튼이 고장날 수도, 고장나지 않을 수도 있다.
- 채널은 무한대 만큼 있다.

# 풀이
- 눌러야 할 버튼의 숫자를 기준으로 더 낮은 수와 더 높은 수를 선택해서 입력수를 센다.
- index 이용
: list.index(x, start, end)
기본적으로 start=0, end=len(list)
start:end 까지의 범위에서 x를 탐색하여 index 반환
- 고장난 버튼이 없거나, 이동할 곳이 100번이거나, 누를 버튼이 전부 고장나지 않은 경우는 조건문으로 처리하여 바로 출력

# 반례
14
2
1 5
- 1이 고장났네? -> 더 낮은 숫자: (0)9 입력(1번 누름) -> + 입력(5번 누름) => 정답: 6
- 1이 고장났네? -> 더 높은 숫자: 20 입력(2번 누름) -> - 입력(6번 누름) => 정답: 8
-> 최솟값: 6
'''

'''
# 보완할 것
- 진짜.. 이 문제만 몇시간을 쏟았는지 모른다. 만만히 봤는데, 자꾸 틀린다.
- 예제를 통과해도, 반례를 찾아서 통과해도, 이것저것 넣어봐도 ValueError가 뜬다..
- 무언가 빠트린 조건이 있다는건데, 뭘까?
- 설령 이 코드에서 더 조건을 빈틈없이 추가한다 하더라도, 너무 지저분하다. 더 좋은 아이디어를 찾아보자.
'''

# 풀이 기록
# 이동하고자 하는 채널
n = input()
len_n = len(n)
num = int(n)

# 고장난 버튼의 개수
m = int(input())

# 고장난 버튼이 없으면
if m == 0:
    print(min(len_n, abs(num-100)))
    
else:
    no_buttons = list(map(int, input().split()))
    
    # 현재 100번이므로, 이동할 필요가 없음
    if n == '100':
        print(0)
        
    else:    
        buttons = [True] * 10
        for i in no_buttons:
            buttons[i] = False
  
        buttons_reverse = list(reversed(buttons))
        
        # 0123456789, 0~9
        # 9876543210, -10~-1

        cnt_100 = abs(num-100)

        check = True
        for i in range(len(n)):
            if not buttons[int(n[i])]:
                check = False
                break
  
        # 버튼을 눌러서 바로 이동 가능하다면,
        if check:
            print(min(len_n, cnt_100))
                  
        else:
            # 남은 눌러야할 수
            if i == 0:
                tmp = n
            else:
                tmp = n[:i]
                
            # 남은 눌러야할 버튼 수
            remain_len = len_n - i
            # 현재 몇번째 누를 수인가
            idx = int(n[i])

            # 더 낮은 수
            # 더 낮은 버튼이 있다면
            if True in buttons[:idx]:
                tmp_l = tmp + str(9-buttons_reverse.index(True, -idx))
                tmp_l += str(9-buttons_reverse.index(True)) * (remain_len-1)
                            
            else:
                tmp_l = tmp + str(buttons.index(True)) * remain_len
            if tmp_l[0] == '0' and len(tmp_l) > 1:
                tmp_l = tmp_l[1:]
                
            cnt_l = len(tmp_l) + abs(num - int(tmp_l))
            
            # 더 높은 수
            # 더 낮은 버튼이 있다면
            if True in buttons[idx+1:]:
                tmp_h = str(buttons.index(True, idx+1))  
                tmp_h += str(buttons.index(True)) * (remain_len-1)
                
            else:
                # 현재 누를게 9인데, 가장 앞의 자리 수라면.
                if i == 0:
                    tmp_h = '10'
                    tmp_h += str(buttons.index(True)) * (remain_len-1)
                tmp_h = tmp + str(9-buttons_reverse.index(True)) * remain_len
                
            cnt_h = len(tmp_h) + abs(int(tmp_h) - num)
            
            # 최솟값 찾기
            answer = min(cnt_100, cnt_l, cnt_h)

            print(answer)
            

'''
# 결과
메모리:  KB
시간:  ms
코드 길이:  B
'''