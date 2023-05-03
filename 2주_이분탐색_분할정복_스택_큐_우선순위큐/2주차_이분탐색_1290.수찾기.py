# 1920 수 찾기 / 이분탐색
# https://www.acmicpc.net/problem/1920
import sys
N = sys.stdin.readline()
arr1 = list(map(int, input().split()))
M = sys.stdin.readline()
arr2 = list(map(int, input().split()))

def sol(arr1, arr2):
    arr1.sort()
    for i in arr2:
        start = 0
        end = len(arr1) - 1
        left = start
        right = end
        while True:
            mid = (left + right) // 2
            if (arr1[mid] > i):
                right = mid - 1
            elif (arr1[mid] < i):
                left = mid + 1
            else:
                print(1)
                break

            if left > right:
                print(0)
                break
    
sol(arr1, arr2)
