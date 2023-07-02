# 처음 생각한 풀이 : 시간초과
# 슬라이싱의 시간복잡도때문에..

# 두번째 풀이 : 투 포인터 사용
# 실패.. => 제대로 된 투 포인터 구현 실패
# 투 포인터 알고리즘 사용까지 알았는데 구현에서 못해서 너무 아쉽다..

import sys
input = sys.stdin.readline

t = int(input())
string = [input().rstrip() for _ in range(t)]

def check(s):
    n = len(s)
    if s == s[::-1]:
        return print(0)

    left = 0
    right = n-1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue
        # ------------- 여기까지 구현
        # 참고 : https://ryu-e.tistory.com/45
        if left <= right - 1:
            temp = s[:right] + s[right+1:]
            if temp[:] == temp[::-1]:
                return print(1)
        if left + 1 <= right:
            temp = s[:left] + s[left+1:]
            if temp[:] == temp[::-1]:
                return print(1)
            
        return print(2)

for i in string:
    check(i)

# 메모리 : 34084KB 시간 : 104ms	