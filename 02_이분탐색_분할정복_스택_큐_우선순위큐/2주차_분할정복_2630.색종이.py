import sys
N = int(input())
cube = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(cube)

b_cnt = 0
w_cnt = 0
# 질문: arr같은 자료구조의 경우 전역에서 선언하고 변수로 전달받지 않아도 접근할 수 있다?
# (global <매개변수>해야하는 매개변수랑 다르게. 접근 제어하려면 클래스를 사용해야 하나? )
# 재귀함수를 설정할 때에는 조작할 자료와 매개 변수에 다음 재귀조건을 받을 수 있는 변수를 받도록 하자
# 데이터 읽기만 하고 조작은 안해서 전달 안해도 되긴 한다.
def sectionCount(arr, startX, startY, N): # 한 구역이 채워져 있는지 아닌지 확인하는 함수
    tmp_cnt = 0
    global b_cnt
    global w_cnt
    # 왜 배열은 unboundlocal error가 뜨지 않지?
    for i in range(startX, startX+N):
        for j in range(startY, startY+N):
            if arr[i][j]:                    # 이렇게도 쓸 수 있다.
                tmp_cnt += 1
    if not tmp_cnt: # 아무것도 없음! 값들이 모두 0
        w_cnt += 1
    elif tmp_cnt == N**2:
        b_cnt += 1
    else: # 나누어지는 다음 단계를 모두 재귀한다
        sectionCount(arr, startX, startY, N//2)  #나머지 없이 몫으로 나누면 1칸까지 커버 가능
        sectionCount(arr, startX + N//2, startY, N//2)
        sectionCount(arr, startX, startY + N//2, N//2)
        sectionCount(arr, startX + N//2, startY + N//2, N//2)
    return
sectionCount(cube, 0, 0, N)
print(w_cnt)
print(b_cnt)