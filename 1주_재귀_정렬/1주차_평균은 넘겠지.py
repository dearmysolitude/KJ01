
TC = int(input())
points = [list(map(int, input().split())) for _ in range(TC)]

Sum=[0]*TC
Average=[0]*TC
Count=[0]*TC
Portion=[0]*TC
pNum=[0]*TC
for i in range(TC):
    pNum[i]=points[i][0]
    for j in range(1, pNum[i]+1):
        Sum[i] += points[i][j]
    Average[i] = Sum[i] / pNum[i]
    for k in range(1, pNum[i]+1):
        if Average[i] < points[i][k]:
            Count[i] += 1
    Portion[i] = Count[i] / pNum[i]

ans=[0]*TC
for i in range(TC):
    ans[i]=Portion[i]*100
    ans[i] = round(ans[i], 3)

    print(f'{ans[i]:.3f}%', sep='')