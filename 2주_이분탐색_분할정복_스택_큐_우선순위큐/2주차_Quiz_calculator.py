# 2. 스택을 활용해 사칙 연산이 가능한 계산기를 구현하는 것과 관련된 퀴즈를 드리겠습니다.
# 계산기에 관한 내용은 해당 책에 없으나 중요한 부분이므로 알고 가시면 좋을 거 같습니다.

# 스택을 이용한 계산기 구현에 대해 이해하시고 난 후, calculator.py 파일로 특정 식을 처리할 때
# convert_to_postfix 함수의 answer와 opStack의 상태와 calculate 함수의 stack의 상태를 표시하는 퀴즈를 드리려고 합니다.
# 식의 숫자는 한 자리 수만 입력되는 경우를 가정합니다! 아래는 3 + 1을 처리할 때의 예시입니다.

# ex) 3 + 1
# # convert_to_postfix 함수
# answer: 3, opStack: 
# answer: 3, opStack: +
# answer: 31, opStack: +
# postfix : 31+
# # calculate 함수
# stack : 3
# stack : 3 1
# stack : 4
# result : 4

import sys

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def join_array(ints):
    str_list = list(map(str, ints))
    return " ".join(str_list)

class ArrayStack:
    def __init__(self):
        self.data = []
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return self.size() == 0
    def push(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1]
    def serialize(self):
        return join_array(self.data)
def convert_to_postfix(S):
    opStack = ArrayStack()
    answer = ''
    
    for w in S :
        if w in prec :
            if opStack.isEmpty() :
                opStack.push(w)
            else :
                if w == '(' :
                    opStack.push(w)
                else :
                    while prec.get(w) <= prec.get(opStack.peek()) :
                        answer += opStack.pop()
                        if opStack.isEmpty() : break
                    opStack.push(w)
        elif w == ')' :
            while opStack.peek() != '(' :
                answer += opStack.pop()
            opStack.pop()
        else :
            answer += w
        
    while not opStack.isEmpty() :
        answer += opStack.pop()
    
    return answer
def calculate(tokens):
    stack = ArrayStack()
    for token in tokens:
        if token == '+':
            stack.push(stack.pop()+stack.pop())
        elif token == '-':
            stack.push(-(stack.pop()-stack.pop()))
        elif token == '*':
            stack.push(stack.pop()*stack.pop())
        elif token == '/':
            rv = stack.pop()
            stack.push(stack.pop()//rv)
        else:
            stack.push(int(token))
        
    return stack.pop()
# infix 수식에서 공백 제거
infix = sys.stdin.readline().replace("\n", "").replace(" ", "")
postfix = convert_to_postfix(infix)
print(f"postfix : {postfix}")
result = calculate(postfix)
print(f"result : {result}")


#직접 구현을 해 보자

# instr = list(input())
# def toPost(arr):
    
#     opstack = []
#     outstack = []

# def calculator(arr):



# 민지 님 코드############################################################
# import sys


# def infix_to_postfix (arr) :
#     outstack = []
#     opstack = []
    
#     for i in range(0, len(arr)) :
#         if arr[i] == "*" :
#             if len(opstack) == 0  :
#                  opstack.append(arr[i])
                 
#             else :
#                 for j in range(len(opstack)-1, -1, -1) :
#                     if opstack[j] == '/' :
#                         outstack.append(opstack.pop())
#                     else :
#                         opstack.append(arr[i])
#                         break
#         elif arr[i] == "/" :
#             if len(opstack) == 0  :
#                  opstack.append(arr[i])
                 
#             else :
#                 for j in range(len(opstack)-1, -1, -1) :
#                     if opstack[j] == '*' :
#                         outstack.append(opstack.pop())
#                     else :
#                         opstack.append(arr[i])
#                         break
#         elif arr[i] == '+' :
#             if len(opstack) == 0  :
#                  opstack.append(arr[i])
                 
#             else :
#                 for j in range(len(opstack)-1, -1, -1) :
#                     if opstack[j] == '*' or opstack[j] == '/' or opstack[j] == '-' :
#                         outstack.append(opstack.pop())
#                     else :
#                         opstack.append(arr[i])
#                         break
#         elif arr[i] == '-' :
#             if len(opstack) == 0  :
#                  opstack.append(arr[i])
                 
#             else :
#                 for j in range(len(opstack)-1, -1, -1) :
#                     if opstack[j] == '*' or opstack[j] == '/' or opstack[j] == '+' :
#                         outstack.append(opstack.pop())
#                     else :
#                         opstack.append(arr[i])
#                         break
#         elif arr[i] == "(" :
#             opstack.append(arr[i])
#         elif arr[i] == ")" :
#             for h in range(len(opstack)-1, -1, -1 ):
#                 if opstack[h] == "(" :
#                    opstack.pop()
#                    break 
#                 else :
#                     outstack.append(opstack.pop())
#         else :
#             outstack.append(arr[i])
        
#         print("answer: ", outstack)
#         print("opstack: ",opstack)    
#     while len(opstack) != 0 :
#         outstack.append(opstack.pop())
                    
#     return outstack 
# # 계산하는 로직 구현
# def calculate (arr) :
#     arr2 = collections.deque()
#     for i in arr :
#         arr2.append(i)
        
#     stack = []
#     while len(arr2) != 0 :
        
#         temp = arr2.popleft()
        
#         if temp == "*" or temp == "/" or temp == "+" or temp == "-" :
#             a = stack.pop()
#             c = stack.pop()
#             if temp == "*":
#                 stack.append(int(a) * int(c))
#             elif temp == "/" :
#                 stack.append(int(c) / int(a))
#             elif temp == "+" :
#                 stack.append(int(a) + int(c))
#             elif temp == "-" :
#                 stack.append(int(a) - int(c))
#         else :
#             stack.append(temp)
        
#         if len(arr2) == 0 :
#             break
        
#     print(stack[0])
