#quick sort
# https://www.acmicpc.net/problem/2751

def QuickSort(array, start, end):
    if start >= end: return
    pivot = start
    left , right = start + 1, end # <<

    while left <= right:
        while left <= end and array[left] < array[pivot]: left += 1
        while right>= end and array[right] >= array[pivot]: right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else: 
            array[right], array[left] = array[left], array[right]
    
    QuickSort(array, start, right+1)
    QuickSort(array, right+1, end)




