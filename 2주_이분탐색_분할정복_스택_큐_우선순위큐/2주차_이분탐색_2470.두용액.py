# 2470 두 용액 / 이분 탐색, 투 포인트, 정렬 ★
import sys
N = int(input())
solution = list(map(int, sys.stdin.readline().split()))
def sol4(arr):
    left = 0
    right = len(arr)-1
    arr.sort()
    smallest = [0, 0]
    now = 10000000000000000
    if arr[-1] < 0: #이 부분도 구현하지 않았었다
        smallest=[arr[-2], arr[-1]]
        print(smallest[0], smallest[1])
        return
    elif arr[0] > 0:
        smallest=[arr[0], arr[1]]
        print(smallest[0], smallest[1])
        return

    while left < right:
        toZero = abs(arr[left]+arr[right])
        if toZero < now:
             now = toZero
             smallest = [arr[left], arr[right]]
        if now == 0:
            break
        if arr[left] + arr[right] > 0:
            right = right - 1
        elif arr[left] + arr[right] < 0:
            left = left + 1
    # 기존에 써 있던 코드는 비효율적이어서 알아보기도 힘들고 시간 초과가 떴음
    # if로 갈라진 후 각 케이스에 대해 처리를 했지만 지금 코드는 if로는 
    # 포인터 변화만 주었음 + 변수명을 좀 더 알기 쉽게 만들자

    print(smallest[0], smallest[1])
sol4(solution)
