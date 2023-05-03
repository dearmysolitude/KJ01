# 11279 최대 힙
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
    
# # 아래 코드는 파이썬으로 구현된 최대 힙 예시
# def heapify(li, idx, n):
#     l = idx * 2;
#     r = idx * 2 + 1
#     s_idx = idx
#     if(l <= n and li[s_idx] > li[l]):
#         s_idx = l
#     if r<= n and li[s_idx] > li[r]:
#         s_idx = r
#     if s_idx != idx:
#         li[idx], li[s_idx] = li[s_idx], li[idx]
#         return heapify(li, s_idx, n)
    
# def heap_sort(v):
#     n = len(v)
#     v = [0] + v

#     for i in range(n, 0, -1):
#         heapify(v, i, n)

#     for i in range(n, 0, -1):
#         print(v[1])
#         v[i], v[1] = v[1], v[i]
#         heapify(v, 1, i-1)
# heap_sort([5,3,4,2,1])
