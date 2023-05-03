import sys
input = sys.stdin.readline
# DP로 작성한 knapsack 함수
# def knapsack2(i, W, w, p):
#     if (i <= 0 or W <= 0):
#         return 0
#     if (w[i] > W):
#         value = knapsack2(i - 1, W, w, p)
#         print(i - 1, W, value)
#         return value
#     else: # w[i] <= W
#         left = knapsack2(i - 1, W, w, p)
#         print(i - 1, W, left)
#         right = knapsack2(i - 1, W - w[i], w, p)
#         print(i - 1, W - w[i], right)
#         return max(left, p[i] + right)

# 12865 정답 코드 DP를 이용한 
n, k = map(int, input().split()) # n: 물품의 갯수, k: 한도 무게

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]
print(d)
# N,K 까지의 최대 가치를 저장한 리스트(Bottom-up DP)

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1): # 담을 물건의 index
    for j in range(1, k+1): #현재 가방 허용 용량
        w = thing[i][0]
        v = thing[i][1]

        if j < w: # 넣을 물건의 무게w보다 허용 무게j를 넘어가면 넣지 않는다
            d[i][j] = d[i-1][j]
        else: # 넘어가지 않는다면 
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v) 
        # 허용 무게를 넘어간다면: 현재 가방에 들어있는 최대 가치 vs 
        # 마지막 무게에서 지금 물건의 무게를 뺀 후 현재 가치를 추가한 경우를 비교한다
        # d[i-1][j-w]에는 해당 무게를 뺀 가방의 최대가치가 들어있음, 만약 값이 0이라면 존재할 수 없는 무게의 가치이고, 자연스레 선택되지 않을 것.

print(d[n][k])

# backtracking으로 작성하려 한 코드
# N, K = map(int, input().split()) # N: 물품의 수, K: 최대 무게
# p = [0] * (N+1) # 가치
# w = [0] * (N+1) # 무게
# x = [0] * (N+1) # 물건을 포함시켰는지 포함 안 시켰는지
# for i in range(N):
#     w[i], p[i] = map(int, input().split())

# def knapsack01(i, size):
#     if i >= N or size <= 0: # 바닥 조건
#         print(x)
#         return
    