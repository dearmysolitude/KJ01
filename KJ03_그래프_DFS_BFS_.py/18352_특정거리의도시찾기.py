import sys
from collections import deque
input = sys.stdin.readline

city, edge, distance, fromwhere= map(int, input().split())
visited = [False] * (city+1)

edges = [[] for _ in range(city+1)]
for i in range(edge):
    a, b = map(int, input().split())
    edges[a].append(b)
distances = [0] * (city+1)


def bfs(start, k):
    visited[start] = True
    q = deque([start])
    distances[start] = 0
    ans = [] #여기에 None을 넣으면 값없이 하나의 인덱스 차지
    while q:
        now = q.popleft()
        for i in edges[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                distances[i] = distances[now] + 1
                if distances[i] == k:
                    ans.append(i)
    if len(ans) == 0:
        return [-1] ##
    else:
        ans.sort()
        return ans

Answer = bfs(fromwhere, distance)
print(*Answer, sep='\n')

# 디버깅 로그
# 처음에는 depth를 cnt로 하였으나 queue에서 pop할때마다 cnt가 늘어나 depth 측정 불가능
# 다른 답안 참고하여 구조를 고쳣으나 변수명이 겹쳐 오답 발생
# 입력 매개변수인 distance와 시작점으로부터의 거리를 나타내는 distances가 같은 이름이었음
# 여러 부분의 debugging결과 둘 중 하나의 이름을 바꾸어 해결함