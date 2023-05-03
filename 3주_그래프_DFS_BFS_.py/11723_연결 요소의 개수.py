import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
#인접행렬
# graph = [[False]*(N+1)]*(N+1)
graph = [[False for _ in range(N+1)]for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = True

#인접리스트
# graph = [False]*(N+1)
# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append([b])
#     graph[b].append([a])

visited = [False] * (N+1)

# print('Node #, Edge # =', N, M)
# print('graph =', graph)
# print('visited =', visited)

# 그래프 탐색 방법: dfs -> 재귀 or stack/ bfs -> queue/ kruskal / prim

def dfs(i):
    if not visited[i]:
        visited[i] = True
        for j in range(1, N+1):
            if graph[i][j]==True:
                dfs(j)
    return

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
print(cnt)