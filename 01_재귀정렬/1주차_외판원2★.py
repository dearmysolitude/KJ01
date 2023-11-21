# https://www.acmicpc.net/problem/10971
# 행렬로 입력이 주어진다
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 외판원이 순회하는 최소 거리를 구하는 문제는 어느 한 지점에서만 탐색해도 나오게 되는 결과는 동일하다.
# ㄴ한붓그리기 한 순환에서 어느 한 점에서 탐색하던 같은 결과를 얻을것이기 때문이다.

# 나중에는 이 방법으로 작성할것
# 모든 경로를 점검하게되면 너무나도 많으므로 조금 다른 방법을 써 보도록 하자
# 동적 게획법: 특정 도시들을 방문한 상태일 때 최소 비용을 저장해 놓고 이를 사용
# 비트마스크: 특정 도시를 방문한 상태를 저장 /2진수표시

# backtracking
# permutation은 시간초과

import sys
def dfs(start, now, value, cnt):
    global ans
    if cnt == N:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return
    if value > ans:
        return
    
    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i, value +a[now][i], cnt +1)
            visited[i] = 0

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize
visited = [0] * N
for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
    print(ans)

# def seq(num, arr, gone, idx, cost, minimum):
#     if idx == 0:
#         if minimum > cost:
#             minimum = cost
#             print('minimum=',minimum)
#         return
#     elif idx > 0:
#         for i in range(N):
#             if gone[i] == 1:
#                 continue
#             if arr[num][i] == 0:
#                 continue
#             cost += arr[num][i]
#             gone[num] = 1
#             idx -= 1
#             print('idx', idx)
#             seq2(i, arr, gone, idx, cost, minimum)

# def seq2(num, arr, gone, idx, cost, minimum):
#     if idx == 0:
#         if minimum > cost:
#             minimum = cost
#             print('minimum=',minimum)
#         return
#     elif idx > 0:
#         for i in range(N):
#             if gone[i] == 1:
#                 continue
#             if arr[num][i] == 0:
#                 continue
#             cost += arr[i][num]
#             gone[num] = 1
#             idx -= 1
#             print('idx', idx)
#             seq(i, arr, gone, idx, cost, minimum)

# def sol(N, arr):
#     minimum = 1000
#     cost = 0
#     gone = [0]*N #갔던 도시
#     for i in range(N):
#         idx = N-2
#         gone[i] = 1
#         seq(i, arr, gone, idx, cost, minimum)
# #====================================================================================
# sol(N, arr)

# def solution(arr, n):
#     depth = 1
#     minimum = []
#     flag = [0]*n
#     for i in range(n):
#         cost = 0
#         flag[i] = 1
#         seq(i, arr, n, depth, cost, minimum, flag)
#     minimum.sort()
#     print(minimum[0])

# def seq(num, arr, n, depth, cost, minimum, flag):
#     if depth == N: # depth 다 내려오면 코스트를 비교할 미니멈 리스트에 붙이고 종료
#         minimum.append(cost)
#         return
#     for i in range(N):
#         if flag[i] == 1: # flag가 있는 경우 depth내려가는 것 중단
#             continue
#         if arr[num][i]==0: # arr 값이 0인 경우 depth 내려가는 것 중단
#             continue
#         cost += arr[num][i]
#         flag[i] = 1
#         seq(i, arr, n, depth, cost, minimum, flag) # 출발지와 도착지는 어떻게? 함수 2개?
    
    
    


