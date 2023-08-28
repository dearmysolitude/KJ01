import sys
input = sys.stdin.readline

# intro = int(input())
# table = [0 for _ in range(92)]
# table[2] = 1
# table[1] = 1
# def fibo(n) -> int:
#     if n == 2:
#         return 1
#     elif n>2 and table[n-1] != 0 and table[n-2] != 0:
#         return table[n-1] + table[n-2]
#     elif n > 2:
#         table[n-1] = fibo(n-1)
#         table[n-2] = fibo(n-2)
#         ans = fibo(n-1) + fibo(n-2)
#         return ans
# print(fibo(intro))

NMax = 91
intro = int(input().rstrip())
table = [0] * (NMax+1)
table[0] = 0
table[1] = 1

def fibo(n):
    if n == 1: # table[1] = 0이므로 아래 if문에 걸리지 않도록
        return table[1]
    elif 2 <= n <= NMax:
        if table[n] == 0:
            table[n] = fibo(n-1) + fibo(n-2)
        return table[n]
        # else:
        #     return fibo(n-1) +fibo(n-2)
    else:
        return 0
print(fibo(intro)) # 첫번째 숫자는 피보나치 1번째 숫자가 아니라 0번째 숫자임