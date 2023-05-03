import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[False]*(N+1) for i in range(N+1)] #2차원 배열
visited = [False]*(N+1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = True

# print(visited)
# print(graph)

def dfs(x):
    if visited[x] == False:
        visited[x] = True
        print(x, end=' ')
        for i in range(1, N+1):
            if graph[x][i] == True: #길이 있다면
                dfs(i)
#길이 있다면 재귀로 들어가 갔는지 확인하는 플래그를 true로 바꾼다.

def bfs(x):
    queue = deque([x]) #큐를 사용함: 루트에서 갈 수 있는 모든 노드를 큐에 인큐시킬것이다.
    visited[x] = False
    while queue: # 큐가 있는 경우 계속 실행
        x = queue.popleft() # 큐에서 값을 뽑아서
        print(x, end=' ') #인쇄
        for i in range(1, N+1): 
            if visited[i]==True and graph[x][i] == True: #만약 하위 노드들 중 방문하지 않고 길이 있는 경우
                visited[i]=False # 방문으로 체크하고
                queue.append(i) # 큐에 인큐한다
dfs(V)
print()
bfs(V)