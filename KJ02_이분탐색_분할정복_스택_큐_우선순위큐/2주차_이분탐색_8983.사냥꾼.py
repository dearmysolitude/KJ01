import sys
M, N, L = map(int, input().split())
shoot = list(map(int, sys.stdin.readline().split()))
animal = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shoot.sort()
cnt = 0
for i in range(len(animal)):
    if animal[i][1] > L: ##
        continue
    else:
        inRange = L - animal[i][1]
        left = 0
        right = len(shoot) - 1
        least = animal[i][0] - inRange
        most = animal[i][0] + inRange
        while left <= right: 
            mid = (left + right) // 2
            if least<= shoot[mid] <= most: #범위를 이진탐색에 사용할 수 있다. ##
                cnt += 1
                break
            elif shoot[mid] < least:
                left = mid + 1
            elif shoot[mid] > most:
                right = mid - 1
print(cnt)