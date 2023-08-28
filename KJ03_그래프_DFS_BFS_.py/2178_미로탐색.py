import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(input()))

maze[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = [[0,0]]
while queue:
    x, y = queue[0][0], queue[0][1]

    del queue[0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            if maze[nx][ny] == "1":
                queue.append([nx, ny])
                maze[nx][ny] = maze[x][y] + 1
    
print(maze[N-1][M-1])
