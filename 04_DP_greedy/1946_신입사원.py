import sys
input = sys.stdin.readline

testCase = int(input())

candi=[[] for _ in range(testCase)]
# print(candi)
for i in range(testCase):
    N = int(input())
    
    for j in range(N):
        candi[i].append(list(map(int, input().split())))
    # print(candi[i])
    ans = []
    candi[i].sort(key = lambda x: x[0])
    ans.append(candi[i][0])
    print('ans init =', ans)
    for k in range(1, len(candi[i])): # 서류 순위가 나보다 높은 사람보다 면접 점수가 높으면 된다.
        target = candi[i][k][1]
        print('target===========', candi[i][k])  
        for l in range(0, k):
            betterPaper = candi[i][l][1] # interview변수 보다 서류가 높은 사람과 비교할 면접 점수들
            print('betterPaper', candi[i][l])
            if target < betterPaper: # 나은 페이퍼를 쓴 사람보다 면접 순위가 높으면(수가 작으면)
                ans.append(candi[i][k])
                print('ans = ', ans)
                break
    print(len(ans))

    # print(candi[i])

## 문제 이해를 잘못했다: 나보다 서류 순위가 높은 지원자들의 면접순위보다 제일 높아야 한다##
# 테스트 케이스 반복도 두 번 나누어 저장하기 보다 그냥 반복문으로 반복하면 된다.

import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    applied = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    applied.sort()
    min_rank = applied[0][1]
    cnt = 1
    for i in range(n):
        rank = applied[i][1]
        if rank < min_rank:
            min_rank = rank
            cnt += 1
    print(cnt)