import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input().rstrip()))

left = 1
right = sum(lines)
answer = 0

while left <= right:
    mid = (left + right) // 2
    temp = 0

    for line in lines:
        temp += line//mid

    if temp < N:
        right = mid - 1
    elif temp >= N:
        left = mid + 1
        answer = mid

print(answer)