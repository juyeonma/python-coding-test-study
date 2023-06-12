# 이게 왜 3단계일까? 오만한 생각인걸까...
# 오만한 것 같다 쉽다 생각했으면 5분컷했어야지..

# 첫번째와 마지막은 위에 있는 숫자를 그대로 더하면 되고
# 가운데 있는값은 바로 위의 같은 인덱스값과 그 이전인덱스값의 최대값을 구한 뒤 현재 인덱스 값을 더하면 된다.
def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        triangle[i][0]+=triangle[i-1][0]

        for j in range(1,len(triangle[i])-1):
            triangle[i][j]+=max(triangle[i-1][j-1:j+1])

        triangle[i][-1]+=triangle[i-1][-1]
        # answer=max(answer,*triangle[i]) 
        # 이렇게 안하고 마지막에서만 최댓값 구해주면 될 것 같다 결국 최대값은 마지막줄에서 나오기 때문
    answer=max(triangle[-1]) # 평균적으로 10ms 정도 차이가 나는 것 같긴하다 
    return answer

# 12분