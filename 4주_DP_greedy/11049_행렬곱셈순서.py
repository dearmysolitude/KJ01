# import sys
# input = sys.stdin.readline

# N = int(input())
# matrice = [[list(map(int, input().split()))] for _ in range(N)]

# dp = [[0] * (N+1) for _ in range(N+1)]
# # 대각선 아랫쪽은 사용하지 않습니다. 대각선 부분은 모두 0이고 계단식으로 올라가면서 표를 채워나가게 된다.
# # 현재 dp의 좌표는 마지막으로 계산하는 행렬의 순번이다.

# for i in range(1, N+1):
#     for j in range(i, N+1):

#         dp[i][j] = min(dp[1][i]+dp[i][j]+matrice[i][0]*matrice[][1]*matrice[j+1][0])

##################################################
import sys
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N+1)]

for i in range(2, N+1): # i는 글자 수
    for j in range(N-i+1):
        dp[i][j] = 2**32
        for k in range(1, i):
            dp[i][j] = min(dp[i][j], dp[i-k][j]+dp[k][j+i-k] + mat[j][0]*mat[j+i-k][0]*mat[j+i-1][1])
            # 계단형으로 올라가는 배열 구현
print(dp[-1][0])