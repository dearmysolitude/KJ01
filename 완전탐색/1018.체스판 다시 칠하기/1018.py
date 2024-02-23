import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rock = []

for _ in range(N):
    a = list(input().rstrip())
    rock.append(a)

cnt = []

for i in range(0, N-8+1): # 사각형 여러개 만들기: 가로
    for j in range(0, M-8+1): # 사각형 여러개 만들기: 세로

        w_index = 0
        b_index = 0

        for a in range(i, i + 8): # 사각형 내부 확인하기
            for b in range(j, j + 8):

                if (a + b) % 2 == 0: # 사각형 내부 인덱스 합이 짝수의 경우 
                    if rock[a][b] != 'W':
                        w_index += 1
                    else:
                        b_index += 1
                else: # 홀수인 경우
                    if rock[a][b] != 'W':
                        b_index += 1
                    else:
                        w_index += 1

        cnt.append(w_index)
        cnt.append(b_index)

print(min(cnt))