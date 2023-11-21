# 로또
# 1~49 의 숫자 중 k개의 숫자를 골라 그 숫자 중에서
# 6 개의 숫자를 순서와 관계 없이 뽑는 가짓 수를 구하여라

import sys
input = sys.stdin.readline


def dfs(depth, idx):
    if depth == 6:
        print(*result)
        return
    
    for i in range(idx, k):
        result.append(S[i])
        dfs(depth + 1, i + 1)
        result.pop()


while True:
    testCase = list(map(int, input().rstrip().split()))
    k = testCase[0]
    S = testCase[1:]
    result = []

    dfs(0, 0)
    if k == 0:
        exit()

    print()