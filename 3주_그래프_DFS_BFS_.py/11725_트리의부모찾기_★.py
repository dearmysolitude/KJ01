
# edges = [[] for _ in range(1, node+1)]
# for _ in range(node-2):
#     A, B = map(int, input().split())
#     edges[A].append(B)
#     edges[B].append(A)
# visited = [False] * node+1
# # print(edges)
# print(visited)

# parent = [i for i in range(node+1)]

# def get_parent(x):
#     if parent[x] == x:
#         return x
#     parent[x] = get_parent(parent[x]) #get_parent거슬러 올라가면서 parent[x]값도 갱신
#     return parent[x]

# def union_parent(a, b):
#     a = get_parent(a)
#     b = get_parent(b)

#     if a < b: #작은 쪽이 부모가 된다.(한 집합관계라 부모가 따로 있지 않음)
#         parent[b] = a
#     else:
#         parent[a] = b

# def same_parent(a, b):
#     return get_parent(a) == get_parent(b)

# def dfs(i):
#     if not visited[i]:
#         visited[i] == True
#         for j in edges[i]:
#             if not visited[j]:
#                 dfs(j)

# parent[1] = 1
# for k in range(1, len(node) + 1):
#     for l in edges[k]:
#         if not visited[l]:
#             union_parent(k, l)

# 크루스칼을 사용하기보다,
# bfs나 dfs를 따라 트리를 내려가되, 부모를 저장하게 하여 각 트리에서 부모를 출력하게 하자(부분연결을 해봤으니)

# import sys
# node = int(sys.stdin.readline().rstrip())

# graph = [[False]*(node+1) for i in range(node+1)] #2차원 배열
# visited = [False]*(node+1)

# for i in range(node-1):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a][b] = graph[b][a] = True

# print(visited)
# print(graph)
# parent = [0]*(node+1)
# def dfs(x: int, y: int):
#     if visited[x] == False:
#         visited[x] = True
#         parent[x] = y
#         print(y)
#         for i in range(1, node+1):
#             if graph[x][i] == True: #길이 있다면
#                 dfs(i, y)

# for i in range(node+1):
#     if not visited[i]:
#         dfs(i, i)
# print(visited)
# for i in range(2, node+1): print(parent[i])

# 문제를 잘못 읽었다
import sys
from collections import deque
input = sys.stdin.readline

def solution(N,tree):
	q = deque([1])
	parent = [0] * (N+1)
	while q:
		now = q.popleft()
		for i in tree[now]:
			if parent[i] == 0 and i != 1:
				parent[i] = now
				q.append(i)
	for i in range(2,N+1):
		print(parent[i])

if __name__ == "__main__":
	N = int(input())
	tree = dict()
	for i in range(1,N+1):
		tree[i] = []
	for _ in range(N-1): # 인접 리스트
		n1,n2 = map(int,input().split())
		tree[n1].append(n2)
		tree[n2].append(n1)
	solution(N,tree)