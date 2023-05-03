# 2110 공유기 설치
# 이분 탐색 & 매개변수 탐색
# 매개변수 탐색
a, b = map(int, input().split())
houses = list(int(input()) for _ in range(a))
ans = 0

def sol3(house, N, arr): #house: 집의 수, N: 공유기 수, arr: 집의
    global ans
    arr.sort()
    right = arr[-1] - arr[0] # 길이의 최대값
    # 길이를 모두 구해서 판단하려 하면 너무 복잡하다
    # 
    # length = [] 
    # for i in range(len(arr) - 1):
    #     length.append(arr[i+1] - arr[i])
    left = 1 # 길이의 최소값: 허용 가능함
    while left <= right:
        mid = (left + right) // 2 # 근접값을 이 값으로 설정했을 때 모두 배치할 수 있는가?(조건 만족시킬 수 있는가?)
        # 최대한 멀리 설치해야 한다 -> 첫번째 집에는 무조건 설치해야 한다.
        installed = arr[0]
        count = 1
        for i in range(1, house):
            if arr[i] - installed >= mid:
                installed = arr[i]
                count += 1
                if count == N: break
        if count == N: #**
            left = mid + 1
            ans = mid
        elif count < N:
            right = mid - 1
sol3(a, b, houses)
print(ans)

# 진우 코드
# import sys
# input = sys.stdin.readline

# house, wifi = map(int, input().split())
# houselist = []
# for i in range(house):
#     houselist.append(int(input()))
# houselist.sort()

# count = 1
# left = 1  # 가능한 최소 거리
# right = houselist[-1] - houselist[0]  # 가능한 최대 거리

# while left <= right:
#     mid = (left + right) // 2
#     installed = houselist[0]  # 첫 번째 집에는 무조건 공유기 설치
#     count = 1
    
#     for i in range(1,   house):
#         if houselist[i] - installed >= mid:
#             installed = houselist[i]
#             count += 1
        
#         if count == wifi:  # 공유기를 다 설치한 경우
#             break
    
#     if count == wifi:  # 공유기를 다 설치한 경우
#         left = mid + 1  # 최소 거리 증가
#         answer = mid   # 현재의 최대 거리 저장
#     else:
#         right = mid - 1  # 최대 거리 감소

# print(answer)
