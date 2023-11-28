# 에디터
# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함

import sys
input = sys.stdin.readline

init = input().rstrip()
cnt = int(input().rstrip())

ors = []
for i in range(cnt):
    ors.append(input().rstrip())
    
# 리스트보다 스택이 나을 것 같다.
# 커서 앞에 있는 문자 컨테이너 + 커서 뒤에 있는 문자 컨테이너

def editor(init, orders, cnt):
    front = []
    back = []
    for i in init:
        front.append(i)
    
    for i in orders:
        do_edit(front, back, list(i))
    
    for i in front:
        print(i, end='')
    for j in range(len(back)-1, -1, -1):
        print(back[j], end='')

def do_edit(front, back, order):
    if order[0] == 'L':
        if len(front) == 0:
            return
        back.append(front.pop())
    elif order[0] == 'D':
        if len(back) == 0:
            return
        front.append(back.pop())
    elif order[0] == 'B': # 백스페이스 구현
        if len(front) == 0:
            return
        front.pop()
    elif order[0] == 'P':
        front.append(order[2])

editor(init, ors, cnt)


# 리스트로 시도

# cursor은 0부터 처음 주어진 문자열의 갯수 n까지의 인덱스를 가질 수 있음
# def do_edit(input_txt, cursor, order):
#     if order[0] == 'L':
#         if cursor == 0:
#             return
#         cursor = cursor - 1
#     elif order[0] == 'D':
#         if cursor == len(input_txt):
#             return
#         cursor = cursor + 1
#     elif order[0] == 'B': # 백스페이스 구현
#         if cursor == 0:
#             return
#         input_txt[cursor] = 0
#     elif order[0] == 'P':
                  
