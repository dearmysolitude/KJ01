# top을 가지고 너무 많은 일을 하려다 꼬여서 오답을 토해냄
import sys
N = int(input())
def stack(N):
    stack = []
    top = 0
    for i in range(N):
        user_input= sys.stdin.readline().split()
        if user_input[0] == 'push':
            stack.append(int(user_input[1]))
            top += 1
        elif user_input[0] == 'pop':
            if len(stack) != 0:
                print(stack.pop())
                top -= 1
            else: print(-1)
        elif user_input[0] == 'size':
            print(len(stack))
        elif user_input[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif user_input[0] == 'top':
            if len(stack) != 0:
                print(stack[top-1])
            else: print(-1)
stack(N)
# import sys
# n = int(sys.stdin.readline())

# stack=[]
# for i in range(n):
#     command = sys.stdin.readline().split()

#     if command[0]=='push':
#         stack.append(command[1])
#     elif command[0]=='pop':
#         if len(stack)==0:
#             print(-1)
#         else:
#             print(stack.pop())
#     elif command[0] == 'size':
#         print(len(stack))
#     elif command[0] == 'empty':
#         if len(stack)==0:
#             print(1)
#         else:
#             print(0)
#     elif command[0] == 'top':
#         if len(stack)==0:
#             print(-1)
#         else:
#             print(stack[-1])