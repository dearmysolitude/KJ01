
def quick_sort(array, start, end):
    if start >= end: return
    pivot = start
    left, right = start +1, end

    while left <= right:
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈리지 않은 경우
            array[right], array[left] = array[left], array[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right +1 , end)

# 비효율적이지만 직관적으로 이해하기 쉬운 버전
def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1: return array

    pivot, tail = array[0], array[1:]

    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]

    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)