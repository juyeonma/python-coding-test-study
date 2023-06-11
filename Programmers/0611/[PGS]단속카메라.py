# 풀이 참고 : https://wwlee94.github.io/category/algorithm/greedy/speed-enforcement-camera/
def solution(routes):
    answer = 0
    # 진출 지점 기준으로 오름 차순 정렬합니다. (routes[1] 기준)
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.
    
    # routes 배열을 반복하면서 카메라가 진입 지점(route[0])보다 작은지 확인합니다.
    for route in routes:
        if camera < route[0]:
            # 작다면, 현재 카메라 위치로 해당 차량을 만나지 못했다는 의미이니
            # 4-1. 카메라를 추가로 세우고
            # 4-2. 가장 최근 카메라의 위치(route[1])를 갱신합니다.
            answer += 1
            camera = route[1]
    return answer

# greedy 문제였다..
# 다음주에 그리디 복습이랑 dp 복습을 철저히 해야겠다..ㅠㅠ..