# import sys
# input = sys.stdin.readline

# # dfs 오답입니다
# # 쓸데없이 visited를 사용해서 메모리만 더 차지하는거 같은데?
# # 그냥 재귀 끝나면 count +1 하는 편이 간단하다.
# N, M = map(int, input().split()) #방 바닥의 세로 크기 / 방 바악의 가로 크기

# floor = []
# for i in range(N):
#     floor.append(list(map(str, input().rstrip())))

# def dfsP(x, y):
#     global count
#     if y == N-1:
#         count+=1     
#     ny = y + 1
#     if ny < N:
#         if floor[x][y] == floor[x][ny]:
#             floor[x][y] = 1
#             dfsP(x, ny)
#         elif floor[x][y] != floor[x][ny]: #재귀 탈출
#             count += 1
#     return

# def dfsH(x, y):
#     global count
#     if x == M-1:
#         floor[x][y] = 1
#         count+=1
#     nx = x + 1
#     if nx < M:
#         if floor[x][y] == floor[nx][y]:
#             floor[x][y] = 1
#             dfsP(nx, y)
#         elif floor[x][y] != floor[nx][y]: #재귀 탈출
#             count += 1
#     return
# def sol():
#     global count
#     for i in range(M):
#         for j in range(N):
#             if floor[i][j]!=1 and floor[i][j] == '-':
#                 dfsH(i, j)
#             elif floor[i][j]!=1 and floor[i][j] == '|':
#                 dfsP(i, j)
#     print(count)

# sol()

# ## 


# ## 오류가 하도 나서 찾아본 답안
# def dfs(x,y):
#     if graph[x][y] == '-':
#         graph[x][y] = 1	   
#         for _y in [1,-1]:   
#             Y = y + _y
#             if (Y > 0 and Y < m) and graph[x][Y] == '-':
#                 dfs(x,Y)
#     if graph[x][y] == '|':
#         graph[x][y] = 1	    
#         for _x in [1,-1]: 
#             X = x + _x  
#             if (X > 0 and X < n) and graph[X][y] == '|':
#                 dfs(X,y)
 
# n,m = map(int, input().split()) 
# graph = [] 
# for _ in range(n):
#     graph.append(list(input()))
 
# count = 0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == '-' or graph[i][j] == '|':
#             dfs(i,j)   
#             count += 1
 
# print(count)


import sys
input = sys.stdin.readline

# dfs 오답입니다
# 쓸데없이 visited를 사용해서 메모리만 더 차지하는거 같은데?
# 그냥 재귀 끝나면 count +1 하는 편이 간단하다.
N, M = map(int, input().split()) #방 바닥의 세로 크기 / 방 바악의 가로 크기

floor = []
for i in range(N):
    floor.append(list(map(str, input().rstrip())))
# for j in range(N):
#     print(floor[j])

count = 0
def dfsP(x, y):
    ny = y + 1
    floor[y][x] = '1'
    if ny < N and floor[ny][x] == '|' :
        dfsP(x, ny)

def dfsH(x, y):
    nx = x + 1
    floor[y][x] = '1'
    if nx < M and floor[y][nx] == '-':
        dfsH(nx, y)

def sol():
    global count
    for i in range(M):
        for j in range(N):
            if floor[j][i] == '-':
                dfsH(i, j)
                count += 1
            elif floor[j][i] == '|':
                dfsP(i, j)
                count += 1
    print(count)

sol()
