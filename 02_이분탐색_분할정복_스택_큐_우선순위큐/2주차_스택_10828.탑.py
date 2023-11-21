# 2493 탑
import sys
N = int(input())
towers = list(map(int, sys.stdin.readline().split())) # 너는 이제부터 스택이다
def whichTower(arr, a):
    ans = [0]*a
    ans[0] = 0
    while len(arr) > 0:
        you = arr.pop() #꺼내서
        now = len(arr) #지금 arr에 남아있는 데이터의 갯수만큼
        if now != 0: #원소가 남아있다면
            for i in range(now-1, -1, -1): #마지막 탑부터 찾아본다, "인덱스"
                if you <= arr[i]: #꺼낸 값과 비교 
                    ans[now] = i+1 ##now는 뽑아낸 후 길이이지만 인덱스이므로 뽑아낸 수의 index는 now임/ 인덱스는 0부터지만 타워 셀 때에는 1부터 센다(i+1)
                    break #처음 뽑은 애보다 큰걸 만나면 처리 후 나간다
                else:
                    if i == 0:
                        ans[now] = 0
    for answer in ans: print(answer, end=' ')
    return
whichTower(towers, N) # 시간 초과 O(N2)
#스택으로 구현하면 모두 검사할 필요 없다
#스택을 뽑아내면서 답을 추가해나가보자
import sys
N = int(input())
towers = list(map(int, sys.stdin.readline().split())) # 너는 이제부터 스택이다
stack = []
answer = []
#==================================================
for i in range(N):
    while stack:
        if stack[-1][1] > towers[i]:
            answer.append(stack[-1][0]+1)
            break
        stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, towers[i]])
#==================================================
for i in range(N):
    print(answer[i], end=' ')