# 8진수, 10진수, 16진수

import sys
input = sys.stdin.readline

X = list(input().rstrip())
indicator = X[0]
second_indi = X[1]

ans = 0
X.reverse()
if indicator == '0':
    if second_indi == 'x': # 16 진수
        # print('16진수')
        for i in range(len(X)-2):
            if X[i] == 'a':
                ans += 10 * pow(16, i)
            elif X[i] == 'b':
                ans += 11 * pow(16, i)
            elif X[i] == 'c':
                ans += 12 * pow(16, i)
            elif X[i] == 'd':
                ans += 13 * pow(16, i)
            elif X[i] == 'e':
                ans += 14 * pow(16, i)
            elif X[i] == 'f':
                ans += 15 * pow(16, i)
            else:
                ans += int(X[i]) * pow(16, i)
        print(ans)
    else: # 8 진수
        # print("8진수")
        for i in range(len(X)-1):
            ans += int(X[i]) * pow(8, i)
        print(ans)
else: # 10진수
    # print("10진수")
    X.reverse()
    for i in range(len(X)):
        print(X[i], end='')