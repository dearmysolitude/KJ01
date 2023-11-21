# 2231 분해합

# N의 분해합은 N과 N을 이루는 각 자리수의 합.
# M의 분해합이 N인 경우, M을 N의 생성자라고 한다. 
# 예: 245의 분해합은 256(= 245 + 2 + 4 + 5)
# N이 주어졌을 때 N의 가장 작은 생성자를 구해내는 프로그램을 구하시오.

import sys
input = sys.stdin.readline().rstrip
N = int(input())

# 자릿수
# digit = 0
# for i in range(6, -1, -1):
#     a = N//i
#     if a != 0:
#         digit = i
#         break

# 각 자리숫자 구하는 함수
def get_digit(n):
    return[int(num) for num in str(n)]

# 생성자의 범위
digit = len(get_digit(N))
b = N - 9 * digit
if b < 0:
    b = 0

ans = 0
for i in range(b, N):
    temp = i
    numbers = get_digit(i)
    for j in numbers:
        temp += j
    if temp == N:
        ans = i
        break

print(ans)