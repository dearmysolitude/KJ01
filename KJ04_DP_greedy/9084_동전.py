import sys
input = sys.stdin.readline

N = int(input().rstrip()) # test case

for _ in range(N):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    table = [0] *(m+1)
    table[0] = 1

    for coin in coins:
        for i in range(m+1):
            if i>= coin:
                table[i]+=table[i-coin]

    print(table[m])