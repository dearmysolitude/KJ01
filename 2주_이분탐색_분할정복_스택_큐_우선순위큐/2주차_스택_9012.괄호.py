# 9012 괄호
# import sys
# T = int(input())
# def VPS(number):
#     for _ in range(number): #줄 변경
#         flag = 0 # 스택이 0인 상태에서 )가 들어왔을 때 표시
#         line = list(map(str, sys.stdin.readline().strip())) #strip()개행문자 제거
#         #print(line)
#         a = len(line)
#         psStack = []
#         for i in range(a): #글자 변경
#             #print(line[i])
#             if line[i] == '(':
#                 psStack.append(1)
#                 #print(i, ": ",psStack)
#             elif line[i] == ')': #
#                 if len(psStack) == 0: #이미 (가 다 빠져나간 경우 무조건 NO출력
#                     flag = 1
#                     #print(i, ': ', psStack)
#                     break
#                 else: psStack.pop()
#                 #print(i, ': ', psStack)
#         if len(psStack) == 0 and flag == 0:
#             print('YES')
#         elif len(psStack) != 0 or flag == 1:
#             print('NO')
#     return
# VPS(T)
# 혹은
import sys
T = int(input())
def VPS(lines):
    for line in lines: #줄 변경
        flag = 0 # 스택이 0인 상태에서 )가 들어왔을 때 표시
        #print(line)
        a = len(line)
        psStack = []
        for i in range(a): #글자 변경
            #print(line[i])
            if line[i] == '(':
                psStack.append(1)
                #print(i, ": ",psStack)
            elif line[i] == ')': #
                if len(psStack) == 0: #이미 (가 다 빠져나간 경우 무조건 NO출력
                    flag = 1
                    #print(i, ': ', psStack)
                    break
                else: psStack.pop()
                #print(i, ': ', psStack)
        if len(psStack) == 0 and flag == 0:
            print('YES')
        elif len(psStack) != 0 or flag == 1:
            print('NO')
    return

# lines = [list(map(str, sys.stdin.readline().strip())) for _ in range(T)] #strip()개행문자 제거
# VPS(lines) #이번엔 입력즉시 출력되는게 아니라 입력 후 스트링 덩어리를 넘겨줬다
