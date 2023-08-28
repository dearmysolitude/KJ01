# # 위상 정렬 알고리즘
# from collections import deque
# import sys
# input = sys.stdin.readline

# v, e = map(int, input().split()) # vertices / node
# indegree = [0]*(v+1) # 노드의 연결된 진입 차수
# graph = [[] for i in range(v+1)] # 

# # 방향 그래프에서 모든 간선 정보 받아오기
# for _ in range(e):
#     a, b = map(int, input().split())
#     graph[a].append(b) # 정점 A에서 B로 이동 가능
#     indegree[b] += 1

# def topologySort():
#     result = [] # 큐에서 꺼낸 결과를 입력하는 리스트
#     q = deque() # 진입 차수가 0인 노드를 가져오는 큐

#     for i in range(1, v+1):
#         if indegree[i] == 0:
#             q.append(i)
    
#     while q:
#         #큐에서 꺼내서 결과에 붙여 넣기
#         now = q.popleft()
#         result.append(now)
#         #해당 원소와 연결된 노드들의 진입차수 -1
#         for i in graph[now]:
#             indegree[i] -= 1
#             #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
#             if indegree[i] == 0:
#                 q.append(i)
#     #결과 출력
#     for i in result:
#         print(i, end = '')

# topologySort()

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split()) # N은 사람의 수, M은 간선의 수
graph = [[] for _ in range(N+1) ] #인접 인덱스
indegree = [0 for _ in range(N+1)]
q = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) #a->b
    indegree[b] += 1

def topologySort():
    result = []    
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result

result = topologySort()
for i in result:
    print(i, end=' ')
print()