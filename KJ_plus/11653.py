# 소인수분해
import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 주어진 숫자를 소인수분해 하시오...
a = N
while a != 1:
    for i in range(2, a+1):
        if a%i == 0:    
            a = int(a/i)
            # if a != 1:
            print(i)
            break
        else:
            continue
    