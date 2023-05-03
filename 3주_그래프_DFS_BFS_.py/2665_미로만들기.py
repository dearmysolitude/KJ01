# 미로만들기

# import sys
# import heapq
# input = sys.stdin.readline

# N = int(input().rstrip())
# maze = [list(map(int, input().strip())) for _ in range(N)]

# # idea
# # 모든 방향으로 이동함. 이동하면서 표식을 남기는데, 내가 지나가는 때 내가 남기는 표식이 다른 표식보다 작다면 작은 것으로 바꾸어 준다.

# changed = [[0] * (N+1) for _ in range(N+1)] ##

# def dijkstra(N):
#     x = 0
#     y = 0
#     changed[x][y] = 0

#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
    
#     q = []
#     heapq.heappush(q, (changed[x][y], x, y)) # ans와 뭘 넣어야 할까?
#     while q:
#         changedNum, nowX, nowY = heapq.heappop(q) # ans가 가장 적은 녀석을 뽑아낸다
#         changed[nowX][nowY] = changedNum
#         if nowX == N-1 and nowY == N-1:
#             print(changedNum)
#             break
#         for i in range(4):
#             nx = nowX + dx[i]
#             ny = nowY + dy[i]
#             # print('nx, ny',nx, ny, 'changed[nx][ny]',changed[nx][ny], 'changedNum',changedNum)
#             if 0 <= nx < N and 0 <= ny < N and changed[nx][ny] >= changedNum:
#                 # print(maze[nx][ny])
#                 if maze[nx][ny] == 0:
#                     # if  changed[nowX][nowY] <= changedNum:
#                     #     continue
#                     changed[nx][ny] = min(changed[nx][ny],changedNum + 1)
#                 else:
#                     changed[nx][ny] = min(changed[nx][ny],changedNum)
#                     # print(changed[nx][ny])
#                     heapq.heappush(q, (changed[nx][ny], nx, ny))
# dijkstra(N)


import sys
import heapq

input = sys.stdin.readline

N = int(input())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
# [[False] * N] * N와 같은 형태로 초기화하면 모든 행이
# 동일한 객체를 참조하므로, 특정 행의 값을 바꾸면 다른 
# 모든 행의 값도 함께 바뀌게 됩니다. 

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        changed, x, y = heapq.heappop(q)
        if x == N-1 and y == N-1:
            print(changed)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                if maze[nx][ny] == 0: #까만 방이라면
                    heapq.heappush(q, (changed+1, nx, ny))
                else:
                    heapq.heappush(q, (changed, nx, ny))
dijkstra()