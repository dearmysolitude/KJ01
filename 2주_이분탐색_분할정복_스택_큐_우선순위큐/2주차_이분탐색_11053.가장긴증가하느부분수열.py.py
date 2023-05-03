# 11053 가장 긴 증가하는 부분 수열 LIS(Longest Increasing Subsequence)문제
# 다이나믹 프로그래밍에서 유명한 문제이다

# 틀림:모든 케이스를 포함하지 못하므로 오답이다
# import sys
# a = int(input())
# nums = list(sys.stdin.readline())
# tmp = []
# def sol5(arr,start):
#     global tmp
#     cnt = 0
#     for i in range(start, len(arr) - 1):
#         if arr[i+1] > arr[i]:
#             if i == 0:
#                 cnt = 1
#             cnt += 1
#         elif arr[i+1] < arr[i]:
#             sol5(arr, i+1)
#     tmp.append(cnt)
#     return
# sol5(nums, 0)
# ans = max(tmp)
# print(ans)

# 동적 프로그래밍과 이진탐색을 사용한 알고리즘 << 나무위키 참고
# import sys
# a = int(input())
# nums = list(map(int, sys.stdin.readline().split()))
# def sol5(arr):
#     subseqLen = [0]
#     minvalOfSubseq = [0]
#     arr.insert(0, 0) # 인덱스가 1인 부분부터 생각하자
#     for i in range(1, len(arr)):
#         if arr[i-1] < arr[i]:
#             subseqLen.append(subseqLen[i-1] + 1)
#             minvalOfSubseq.append(i+1, arr[i])
#         else: #이진 탐색
#             left = 0
#             right = len(minvalOfSubseq) - 1
#             pivot = (left + right) // 2
#             #이진탐색에서 타겟이 포함된 범위를 찾고 싶을 때에는? *****
#             while right - left != 1: #이진탐색 경계조건 확실히! minvalueofseq에 D값을 
#                 if pivot < arr[i]: 
#                     left = pivot
#                 elif pivot > arr[i]:
#                     right = pivot
#                 else:
#                     break
#             subseqLen[i] = left
#             minvalOfSubseq[left] = arr[i]
#     print(max(subseqLen))
# sol5(nums)

# import sys
# a = int(input())
# nums = list(map(int, sys.stdin.readline().split()))
# def sol(A):
#     D = [0] ## 길이
#     X = [A[0]] ## 해당 길이의 부분 수열의 맨 마지막 수
#     for i in range(1, len(A)):
#         left = 0
#         right = len(D) - 1
#         if A[i] > A[i-1]:
#             X.append(A[i])
#             D.append(D[-1] + 1) ## i-1이 아닌 마지막 원소에다 덧붙이기
#         else:
#             target = A[i]
#             while left <= right:
#                 mid = (left + right) // 2
#                 if target < mid:
#                     right = mid - 1
#                 elif target > mid:
#                     left = mid + 1
#                 else: break
#             if target == mid:
#                 X[mid] = A[i]
#             else:
#                 X[right] = A[i] ##
#     print(len(D))
# sol(nums)
