# 숫자의 합

import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(input().rstrip())

ans = 0
for i in nums:
    ans += int(i)
print(ans)