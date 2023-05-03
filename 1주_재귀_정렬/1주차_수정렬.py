# def bubble24_2(nums): # 좋은 예시**
#     #개선: 버블 단계 중 다음 리스트들이 정렬이 완료되어 있으면 더이상 그 부분은 정렬하지 않도록
#     n = len(nums)
#     k = 0
#     while k < n-1:
#         last = n - 1
#         for i in range(n-1, k, -1):
#             if nums[i] < nums[i-1]:
#                 nums[i], nums[i-1] = nums[i-1], nums[i]
#                 last = i
#         k = last
#     printArray(nums)

def bubble(nums):
    n = len(nums)
    k = 0
    while k < n-1:
        for i in range(n-1,k, -1):
            if nums[i] < nums[i-1]:
                nums[i],nums[i-1] = nums[i-1], nums[i]
                last =i
        k = last
    printArray(nums)
