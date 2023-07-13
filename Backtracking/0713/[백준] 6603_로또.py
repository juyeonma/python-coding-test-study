# n과 m 시리즈와 같은 문제였다.

def func(n):
    if len(arr)==6: # 길이가 6이되면
        print(*arr) # 출력
    
    for i in range(n,k):
        arr.append(s[i]) # 배열에 넣기
        func(i+1) # 한단계 들어가서 그다음 인덱스를 배열에 넣기 위한 재귀
        arr.pop() # 윗윗줄에서 넣은 요소 빼고 다음 인덱스를 그 자리에 넣기

while True:
    k,*s = map(int,input().split()) # 하나는 k에 넣고 나머지는 s넣기
    if k==0: 
        break
    arr = []

    func(0)
    print()

#걸린시간 10분
# 메모리 31256kb 시간 48ms