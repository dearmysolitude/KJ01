import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input().rstrip())
table = [0] * (N+2)
table[1] = 1
table[2] = 2

for i in range(3, N+1):
    table[i] = (table[i-1]+table[i-2])%15746 # 계산을 안 해주면 수가 엄청나게 커지므로 메모리 초과가 발생한다
print(table[N])

# def sol(intro):
#     if intro == 1:
#         return 1
#     elif intro == 2:
#         return 2
#     elif 2 < intro:
#         if table[intro] == 0:
#             table[intro] = sol(intro-1) + sol(intro-2)
#         return table[intro]
#     else: return
# print(sol(N))