# 모든 순열

# N이 주어졌을 때, 1 부터 N까지

# 방법 1

# import sys
# import itertools

# input = sys.stdin.readline

# N = int(input().rstrip())
# Array = []
# for i in range(N):
#     Array.append(i+1)

# nPr = itertools.permutations(Array, N)

# for i in nPr:
#     for j in i:
#         print(j, end= ' ')
#     print()

# 방법 2

import sys

input = sys.stdin.readline

N = int(input().rstrip())
Array = []

def dfs(depth):
    if depth == N:
        print(*Array)
        return
    for i in range(1, N+1):
        if i not in Array:
            Array.append(i)
            dfs(depth + 1)
            Array.pop()

dfs(0)   
