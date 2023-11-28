# 히든 넘버

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

ListofUnknown = deque(list(input().rstrip()))

def findNum(unkwonList):
    ans = []
    while unkwonList:
        tmp = unkwonList.popleft()
        if tmp.isdigit(): # 숫자라면
            a = int(tmp)
            while unkwonList and unkwonList[0].isdigit(): # 여기서 unknown list가 있는지 확인부터해야한다.
                tmp1 = int(unkwonList.popleft())
                a = a*10 + tmp1
            ans.append(a)
            if not unkwonList:
                break
        else: # 글자라면
            continue
    print(sum(ans))

findNum(ListofUnknown)