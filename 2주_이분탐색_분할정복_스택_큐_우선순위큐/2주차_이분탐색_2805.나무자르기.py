# 2805 나무자르기 / 이분탐색
# https://www.acmicpc.net/problem/2805
# 높이 H 지정. 톱날이 H미터 위로 올라감. 한 줄 연속한 나무를 모두 절단
# 큰 나무는 잘리고 아니면 안 잘림
# 나무는 필요한 만큼만 가져가려고 한다: M미터 가져가려면 몇미터로 설정해야하나
#잘못된 풀이. 자를 수 있는 범위 중 찾는 수만 판단기준으로 삼으면 되는거였다
# a, b = map(int, input().split())
# trees = list(map(int, input().split()))

# def sol2(M, arr):
#     while True:    
#         left = 0
#         right = len(arr) -1
#         cut = (left + right) // 2
#         total = 0
#         for i in range(cut, len(arr)):
#             total += arr[i] - arr[cut]

#         if total > M:
#             left = cut + 1
#         if total < M:
#             right = cut -1
#         else:
#             print(arr[cut])
#             return
#         if left > right: return -1

# trees.sort()
# sol2(b, trees)
# 옳은 풀이
a, b = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 0, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    
    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    
    #벌목 높이를 이분탐색
    if log >= b:
        start = mid + 1
    else:
        end = mid - 1
print(end)
