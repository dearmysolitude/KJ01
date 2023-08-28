# 자연수 A를 B번 곱한 수를 알고 싶다.
# C로 나눈 나머지를 구하여라
# import sys
# a, b, c = map(int, sys.stdin.readline().split())
# cnt = b
# def mul(before, cnt):
#     if cnt == 0:
#         return before
#     global a
#     global c
#     temp = before * a
#     after = temp % c

#     return mul(after, cnt-1)
# print(mul(a, cnt))
# recursion error

# import sys
# a, b, c = map(int, sys.stdin.readline().split())
# def mul2(a, b, c):
#     remain = a % c
#     number = b % (c-1) #나오는 나머지가 반복되는 단위로 나눈 후 그 나머지
#     print(number) #
#     for i in range(number-2):
#         remain = (remain*a) % c
#         print('repeattime =', i, 'remain =', remain)
#     return remain
# print(mul2(a, b, c))

# remain = a % c
# temp = remain**b
# result = temp % c
# print(result)

import sys
a, b, c = map(int, sys.stdin.readline().split())

def DaC(a, b):
    global c
    if b == 1:
        return a % c
    
    temp = DaC(a, b//2)
    if b %2 == 0:
        return temp * temp % c
    if b % 2 != 0:
        return temp * temp * a % c
    
print(DaC(a, b))