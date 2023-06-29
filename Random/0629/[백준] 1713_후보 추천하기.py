#1시간 넘게 푼 것 같다
# 배열로만 풀지 배열 딕셔너리로 풀지 하나의 변수를 더 설정할지 계속 고민하다가
# 그냥 배열과 딕셔너리로만 풀었다.
# 그런데 풀고나니 굳이 배열이 필요업어서 다시 딕셔너리로만 풀었다.
# 또 딕셔너리 item지우는 법을 몰라서 찾아보았다..
# 지우는 작업은 안해봐서 모르고있었다.
# 딕셔너리에 차례대로 넣다가 딕셔너리에 추천 학생이 없고 n명이 꽉차있으면 딕셔너리 확인후 가장 
# 오래된것을 삭제하고 새로운 학생을 추가한다

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
check_dict={}
for i,num in enumerate(nums):
    if num in check_dict:
        check_dict[num][0]+=1
    else:
        if len(check_dict)==n:
            min_v=sorted(check_dict.items(),key=lambda x:(x[1][0],x[1][1]))[0]
            del check_dict[min_v[0]]
        check_dict[num]=[1,i]

result=sorted(check_dict.items(),key=lambda x:x[0])

print(*list(map(lambda x:x[0], result)))

# 메모리 31256kb 시간40ms