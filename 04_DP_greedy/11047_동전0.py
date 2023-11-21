import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []

for i in range(N):
    coins.append(int(input()))
coins.reverse()
ans = 0
for i in coins:
    num = K//i
    K = K - i*(num)
    ans += num
print(ans)