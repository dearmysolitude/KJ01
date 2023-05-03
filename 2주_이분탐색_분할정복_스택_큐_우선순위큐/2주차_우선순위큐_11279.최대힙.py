# 최대 힙
# a[i]
# 부모 노드 = (i-1) //2 
#자식 노드 = (i*2) +1 왼쪽
# import sys
# from collections import deque
# N = int(input())
# arr = deque()

# 예제 코드
# def down_heap(a, left, right):
#     temp = a[left]
#     parent = left

#     while parent<(right+1) // 2:
#         cl = parent * 2 +1
#         cr = cl + 1
#         child = cr if cr <=right and a[cr] > a[cl] else cl
#         if temp >= a[child]:
#             break
#         a[parent] = a[child]
#         parent = child
#     a[parent] = temp


#append될 때 삽입된 노드만 down힙으로 위치 찾도록 하자
#부모 노드 #
from collections import deque
import sys
N = int(input())
# b = [int(sys.stdin.readline().strip()) for _ in range(N)]
def function(nums):
    a = deque()
    for i in range(N):
        nums = int(input())
        if nums == 0: # 0이 들어와서
            if len(a) == 0: # 갯수가 0개 라면
                print(0)
            elif len(a) == 1: # 갯수가 1개 라면
                print(a.pop())
            else: #갯수가 그 외라면
                print(a[0])
                a[0] = a.pop() # 0번째 있는 원소(가장 큼)을 가장 끝 노드와 바꾼다
                down_heap(a) ## 루트를 삭제한 힙의 정렬
        else:
            if len(a) == 0: # 길이가 0이라면
                a.append(nums) #그냥 그 수를 붙인다
            else: # 그 외에는
                a.append(a[0]) # 맨 마지막에 루트 노드를 덧붙이고
                a[0] = nums # 루트노드에 최근 입력 수를 넣는다
                down_heap(a) #루트 제거된 힙을 다시 정렬한다.

def down_heap(a): # 루트노드 제거되었을 때 아래녀석 가져와서 내리는 함수
    end = len(a) - 1 # 맨 마지막 노드까지
    parent = 0 # 0번째 노드를 부모로 하여 최대힙 만든다
    temp = a[parent] #맨 아래에서 가져온 아이를-함수 밖에서 교환 됐다- temp로 두고 놓을 자리를 탐색한다
    print('array size =', len(a))
    print('array =', a)
    print('trying to position =', temp)
    print('while=============================')
    while parent < (end+1 //2): #리프 내려갈 때까지 반복한다
        cl = parent*2 +1 # 자식 1
        cr = cl + 1 # 자식 2
        child = cr if cr <= end and a[cr] > a[cl] else cl #둘 중 하나 선택
        print('now camparing index of =', parent, 'with child index =', child)
        if temp > a[child]: #여기다 싶으면 반복 중지 혹은 리프노드에 도달한 경우
            print(temp, ' is larger than ', a[child])
            break
        a[parent] = a[child] # 아니라면 계속 아래로 내려간다(이젠 니가 부모야)
        parent = child
    a[parent] = temp #여기가 너-바뀐 a[0]-의 위치임
    print('while end=========================')
    print('position =', parent, 'maximum value(root node) =', a[parent])

function(N)
    

# 이렇게 해도 무방할 것이다: 들어오는 족족 정렬되어 있을테니
# def down_heap_up(a): #노드가 추가되었을 때 아래 있는 녀석을 올리는 함수
#     child = len(a) - 1
#     while True:
#         parent = (child-1) // 2 #
#         if parent < 0 or a[child] <= a[parent]:
#             break
#         a[child], a[parent] = a[parent], a[child]
#         child = parent
