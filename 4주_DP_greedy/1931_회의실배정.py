import sys
input = sys.stdin.readline

N = int(input())

times = [list(map(int, input().split())) for _ in range(N)]
# print(times)
ans = []
times.sort(key = lambda x: x[0]) #한 줄에 쓸 수도 있군
times.sort(key=lambda x: x[1])
# print(times)
ans.append(times[0])
k = 0
for i in range(1, len(times)):
    if(times[i][0] >= ans[k][1]):
        ans.append(times[i])
        k += 1
# print(ans)
print(len(ans))