import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


# BFS
computer = int(input())
connection = int(input())
#인접 리스트
edge = [[] for _ in range(computer+1)]
visited = [None] * (computer+1)
for i in range(1, connection+1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

# print(edge)
cnt = 0
def bfs(i):
    global cnt
    q = deque(edge[i]) # 주의
    visited[i] = True
    while q:
        x = q.popleft()
        if not visited[x]:
            visited[x] = True
            cnt += 1
            for k in edge[x]:
                q.append(k)
bfs(1)
print(cnt)