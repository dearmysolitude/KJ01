
# 힙을 이용한 다익스트라 알고리즘 - 속도는 NlogN으로 줄어든다.

n, m = map(int, input().split())
k = int(input())
INF = 1e8

graph = [[] for _ in range(n+1)] # 1번 노드부터 시작하므로 하나 더 추가

distance = [INF] *(n+1) # 현재 가장 작은 값을 저장할 곳

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 우선순위대로 push된다.
    distance[start] = 0 # 시작점의 거리는 0으로 지정, 가장 작은 값들을 저장

    while q:
        dist, now = heapq.heapop(q) # 최소 heap에서 거리와 지점을 꺼낸다

        if distance[now] < dist: # 이미 입력되어 있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드
            continue # 다음으로 넘어간다.

        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, dist+i[1], i[0])

dijkstra(k)
print(distance)

#다익스트라 알고리즘 - 기본
# n,m=map(int,input().split())
# start = int(input())
# graph = [[] for _ in range(n+1)]

# visited=[False]*(n+1)
# distance=[int(1e9)]*(n+1)

# for _ in range(m):
#     a,b,c = map(int, input().split())
#     # a번 노드에서 b번 노드로가는 비용이 c인 입력
#     graph[a].append((b,c))
#     graph[b].append((a,c))  # 양방향일경우 반대방향도 저장 주의

# def get_smallest_node():
#     min_value=int(1e9)
#     index=0
#     for i in range(1,n+1):
#         if distance[i]<min_value and not visited[i]:
#             min_value = distance[i]
#             index=i
#     return index

# def dijkstra(start):
#     # 출발 기록
#     distance[start]=0
#     visited[start]=True
#     for j in graph[start]:
#         distance[j[0]]=j[1]
        
#     # start 제외한 노드 수 만큼 반복
#     for i in range(n-1):
#         # 최단 거리 노드 추출
#         now=get_smallest_node()
#         # 방문처리
#         visited[now]=True
        
#         for j in graph[now]:
#             # 현재 노드에서 갈 수 있는 다른 노드 cost 계산
#             cost = distance[now]+j[1]
#             # 기존 것 보다 더 짧은 경우 갱신
#             if cost < distance[j[0]]:
#                 distance[j[0]]=cost
    
# dijkstra(start)
                
# for i in range(1,n+1):
#     if distance[i]==int(1e9):
#         print("INFINITY")
#     else:
#         print(distance[i])