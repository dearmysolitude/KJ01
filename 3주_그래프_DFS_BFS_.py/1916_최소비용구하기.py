# 다익스트라 알고리즘을 사용합니다 - 자료구조는 우선순위 큐(최소힙)

import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

distance = [1e9] * (N+1)
graph = [[] for _ in range (N+1)]  #
for _ in range(M):
    initial, destination, cost = map(int, input().split())
    graph[initial].append((destination, cost))

# print(graph)

start, end = map(int, input().split())

def dijkstra(begin):
    q = []
    heapq.heappush(q, (0, begin)) # 거리 / city 위치 쌍으로 입력된다
    distance[begin] = 0

    while q:
        dist, now = heapq.heappop(q) # dist가 가장 적은 녀석을 pop한다
        
        if distance[now] < dist: # 지금 팝으로 뽑아낸 
            continue

        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
dijkstra(start)
print(distance[end])
