# arr =[]


# def binary(i):
#     if arr[i] > arr[i+1]: #왼쪽 자식 노드가 없음
#         print(arr[i])

#         return
#     if arr[i] < arr[i+1]: 
#         binary(i+1)

# from collections import deque
# order = deque()
# for i in range(len(arr)-1):
#     while arr[i-1]<arr[i]:
#         order.append(arr[i-1])
#     if arr[i-1] > arr[i]:
#         print(order.pop())
##########################################################
#index 입력

import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except: 
        break

def sol(start, end):
    if start > end:
        return
    
    mid = end + 1
    for i in range(start+1, end+1): # start는 판단 기준이 된다.
        if arr[start] < arr[i]:
            mid = i
            break

    sol(start+1, mid-1)
    sol(mid, end)
    print(arr[start])

sol(0, len(arr)-1)
 