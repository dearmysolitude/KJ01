# 9935 문자열 폭발
# 첫째 줄에는 전체 문자열이, 둘째 줄에는 폭발 문자열이 입력된다.
# 폭발 문자열이 주어진 문자열에서 폭발 후, 남겨지는 문자열에 다시 폭발 문자열이 포함될 수 있다.
# 폭발 후 결과 문자열에 남아있는 문자가 없는 경우 FRULA라고 출력한다.

# 시간 초과
# import sys
# input = sys.stdin.readline

# init = input().rstrip()
# target = input().rstrip()
# compare = 'init'
# while True:
#     compare = init.replace(target,'')
#     if compare == init:
#         break
#     init = compare
    
# if init == '':
#     print('FRULA')
# else:
#     print(init)

# 2차 시도 ========================================

# temp  = []
# temp2 = []
# j = 0

# for i in range(len(init)):
#     if init[i] == target[j]:
#         temp2.append(init[i])
#         if j == len(target):
#             temp2 = []
#             j = 0
#             continue
#         j = +1
#     elif init[i] != target[j] and 0 < j < len(target):
#         temp = temp + temp2
#         j = 0
#         continue
#     elif init[i] != target[j]:
#         temp.append(init[i])
#너무 복잡하다!!

# ================================================

import sys
input = sys.stdin.readline
init = input().rstrip()
target = input().rstrip()

temp = []
for i in range(len(init)):
    temp.append(init[i])
    if ''.join(temp[-len(target):]) == target:
        for _ in range(len(target)):
            temp.pop()

if temp:
    print(''.join(temp))
else:
    print('FRULA')

