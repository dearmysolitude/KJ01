# 1074
# 그림을 함께 보는 것이 이해에 도움이 될 것
# https://ggasoon2.tistory.com/11
N, r, c = map(int, input().split())

ans = 0

# 분할정복
while N != 0:
    N -= 1
    # 1사분면
    if r < 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 0

    # 2사분면
    elif r < 2 ** N and c >= 2 ** N:
        ans += (2 ** N) * (2 ** N) * 1
        c -= (2 ** N )
    
    # 3사분면
    elif r >= 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 2
        r -= (2 ** N)

    else:
        ans += (2 ** N) * (2 ** N) * 3
        r -= ( 2 ** N )
        c -= ( 2 ** N )

print(ans)

# 재귀함수
N, r, c = map(int, input().split())
def sol(N, r, c):
    if N == 0:
        return 0
    return 2*(r%2)+(c%2)+ 4*sol(N-1, int(r/2), int(c/2))
print(sol(N, r, c))