def bisearch(nums, target, left, right):
    while True:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else: return mid  #target 이 mid에 있는 경우
        if left > right: return -1


