# import sys
# from collections import deque
# input = lambda: sys.stdin.readline().rstrip()
        
# caseNum = int(input())
# for i in range(caseNum): #테스트케이스마다 각각 print Yes/No 실행
    
#     node, edge = map(int, input().split())

#     visited = [False]*(node+1)
#     adjList = [None]*(node+1)
#     color = [0] *(node+1)

#     def bfs(x):
#         q = deque()
#         q.append(x)
#         visited[x] = True
#         while q:
#             a = q.popleft()
#             color[a] = num
#             for i in range(1, node+1):
#                 if not visited[i] and (i in adjList[a]):
#                     visited[i] = True
#                     bfs(i)
    
#     for _ in range(edge):
#         #인접 리스트
#         a, b = map(int, input().split())
#         adjList[a].append(b)
#         adjList[b].append(a)
    
#     num = 0
#     for j in range(1, node+1):
#         if not visited[j]:
#             bfs(j)
#             num += 1

#     b = len(set(color))
#     if len(b) == 2:
#         print('YES')
#     else:
#         print('NO')

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
test_num = int(input())

isValied = True

def dfs(start):
    global isValied
    visited[start] = True
    for i in adjacent[start]:
        if not visited[i]:
            team[i] = (team[start]+1)%2
            dfs(i)
        elif team[start] == team[i]:
            isValied = False

for _ in range(test_num):
    isValied = True
    v, e = map(int, input().split())
    visited = [False] * (v+1)
    adjacent = [[] for  _ in range(v+1)]
    team = [0] * (v+1) #T집합 또는 F집합
    for _ in range(e):
        p, q = map(int, input().split())
        adjacent[p].append(q)
        adjacent[q].appned(p)
    