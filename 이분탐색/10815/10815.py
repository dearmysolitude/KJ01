import sys
input = sys.stdin.readline

sangNum = int(input().rstrip())
sangCards = list(map(int, input().rstrip().split(" ")))
sangCards = sorted(sangCards)

compareNum = int(input().rstrip())
comapareCards = list(map(int, input().rstrip().split(" ")))

ans = list()

def binary(nums, target, left, right, ans):
    while True:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            ans.append(1)  #target 이 mid에 있는 경우
            return

        if left > right:
            ans.append(0)
            return

for compareCard in comapareCards:
    binary(sangCards, compareCard, 0, len(sangCards)-1, ans)

for answer in ans:
    print(answer, end=" ")