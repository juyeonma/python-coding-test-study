'''
# 백준_20365_블로그2. 실버 3. 풀이: 23.05.29

# How to
- 각각 몇개의 덩어리로 구분되는가? 
- 가장 덩어리가 많은 색으로 다 칠하고, 나머지 부분 덧칠.

1. R과 B의 덩어리 중 최솟값 구하기 -> 가장 오래 걸리는 code
- split으로 나누어서 list의 길이 count

여기서부턴 실험
2. 첫글자의 덩어리만 구하기: 문자열의 첫글자 덩어리수 >= 나머지 글자 덩어리수 이므로.

3. 경계만 세기: RB or BR로 경계만 count -> 가장 빠르고 간단한 code
- R 또는 B만 남는 경우가 생기므로, 경계 갯수의 최댓값을 구해아함.

4. 2번과 비슷하게, 첫글자가 R이면 RB, B이면 BR의 경계만 세자.


## 예제
R B RR BB R
덩어리: B 2개, R 3개
경계: RB 2개, BR 2개
정답: 3번

R B RR BB
덩어리: B 2개, R 2개
경계: RB 2개, BR 1개
정답: 3번

# Review
- 이것저것 실험해보니까, 굳이 첫글자만 구할 필요 없이 그냥 바로 경계만 세는게 제일 빠르고 간단하다.
- 여기서 split을 하면 빈 문자열이 생긴다! Why?
    - 참고: https://www.acmicpc.net/board/view/89882
    - If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings 
        (for example, '1,,2'.split(',') returns ['1', '', '2']). 
    - The sep argument may consist of multiple characters 
        (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). 
    - Splitting an empty string with a specified separator returns [''].
    
- list의 빈 문자열 없애기
    - 참고: https://jinmay.github.io/2019/06/30/python/python-how-to-delete-empty-string-in-list/
    1. list comprehension : arr = [i for i in arr if i]
    2. join()과 split() : arr = ' '.join(arr).split() 
    3. filter() : arr = list(filter(None, arr))
'''

# 성공 Code
# 1. R과 B의 덩어리 중 최솟값 구하기: 44728 KB 84 ms -> 가장 오래 걸리는 code
n = int(input())
neighbor = input()
# 앞 뒤에 해당 문자열이 있으면 빈 문자열로 나오므로, 제거해서 list에 담음
r = [i for i in neighbor.split('R') if i != '']
b = [i for i in neighbor.split('B') if i != '']
print(min(len(r), len(b))+1)

# 실험..
# 2. 첫글자의 덩어리만 구하기: 39664 KB 60 ms
n = int(input())
neighbor = input()
arr = [i for i in neighbor.split(neighbor[0]) if i != '']
print(len(arr)+1)

# 3. 경계만 세기: 32236 KB 48 ms -> 가장 빠르고 간단한 code
n = int(input())
neighbor = input()
print(max(neighbor.count('RB'), neighbor.count('BR')) + 1)

# 4. 첫글자의 경계만 세기: 32236 KB 48 ms
n = int(input())
neighbor = input()
if neighbor[0] == 'R':
    print(neighbor.count('RB') + 1)
else:
    print(neighbor.count('BR') + 1)


# 시간초과 Code
# 문자열이 중복해서 count 되는 문제가 발생하므로, 시간초과 & 실패
n = int(input())
neighbor = input()
b = [0] * n
r = [0] * n

for i in range(1, n+1):
    b[i-1] = neighbor.count('B'*i)
    r[i-1] = neighbor.count('R'*i)

print(min(sum(b), sum(r)) + 1)


'''
# Result
풀이 시간: 20분 -> 실험
메모리: 44728 KB -> 32236 KB
시간: 84 ms -> 48 ms
코드 길이: 160 B -> 94 B
'''