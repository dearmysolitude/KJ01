
# # 그래프 이론 # 그래프 탐색 # 너비 우선 탐색
# # 좌표로 이동하며, 경계 조건만 맞춰주면된다. bfs로 진행, depth별로 분리하여 visited를 체크하는 방식?

# 입력에서 map(int, input().split()) 부분이 정상적으로 동작하지 않아 3차원 배열 tomatos가 제대로 생성되지 않았습니다. 따라서 입력 부분을 수정해주어야 합니다.

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().rstrip().split())

# 이 입력도 가능
# tomatos = []
# for h in range(H):
#     tomatos.append([])
#     for n in range(N):
#         tomatos[h].append(list(map(int, input().split())))

tomatos = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
for h in range(H):
    for n in range(N):
        tomatos[h][n] = list(map(int, input().split()))
for i in range(H):
    print(tomatos[i])

 
def bfs():
    q = deque()

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatos[h][n][m] == 1:
                    q.append([m, n, h])

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]        

# 토마토 익히기
    while q:
        
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if (0 <= nz < H and 0 <= ny < N and 0 <= nx < M and
                tomatos[nz][ny][nx] == 0):
                tomatos[nz][ny][nx] = tomatos[z][y][x]+1 #
                q.append([nx, ny, nz])
    day = 0
    for i in tomatos:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    return #
            day = max(day, max(j))
    print(day-1)
bfs()
# # 토마토 익었는지 확인하기





