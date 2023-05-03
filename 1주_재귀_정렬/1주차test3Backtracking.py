#backtracking
import sys
N, S = map(int, input().split())
nums = list(map(int, sys.stdin.readline()))
temp = []

cnt = 0
def sol(num):
    global cnt
    if sum(temp) == S and len(temp) > 0:
        cnt += 1
    for i in range(num, N): #현재 시작 인덱스 뒤 원소부터 고려
        temp.append(nums[i])
        sol(i + 1)
        temp.pop()
    
sol(0)
print(cnt)
