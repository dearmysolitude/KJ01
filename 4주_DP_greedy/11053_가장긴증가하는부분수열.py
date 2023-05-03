import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1) # 현재 dp값과 이전의 큰 수의 dp값을 비교

print(max(dp))
