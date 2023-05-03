import sys
input = sys.stdin.readline

N, M = map(int, input().split())

floor = []
for i in range(N):
    floor.append(list(map(str, input().rstrip())))

visited = []
for i in range(M):
    visited.append([False for _ in range(N)])

count = 0

def dfsP(x, y):
    global count
    if y == N-1:
        visited[x][y] = True
        count += 1
    ny = y + 1
    if ny < N:
        if floor[x][y] == floor[x][ny]:
            visited[x][y] = True
            dfsP(x, ny)
        elif floor[x][y] != floor[x][ny]:
            count += 1
    return

def dfsH(x, y):
    global count
    if x == M-1:
        visited[x][y] = True
        count += 1
    nx = x + 1
    if nx < M:
        if floor[x][y] == floor[nx][y]:
            visited[x][y] = True
            dfsH(nx, y)
        elif floor[x][y] != floor[nx][y]:
            count += 1
    return

def sol():
    global count
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and floor[j][i] == '-':
                dfsH(j, i)
            elif not visited[i][j] and floor[j][i] == '|':
                dfsP(j, i)
    print(count)

sol()