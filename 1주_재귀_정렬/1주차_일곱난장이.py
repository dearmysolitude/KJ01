height = [0]*9
summ = 0
for i in range(9):
    height[i] = int(input())
    summ += height[i]
def func(height, summ):
    for i in range(9):
        for j in range(9):
            if i==j:
                continue
            if summ - height[i] - height[j] == 100:
                height[i] = 0
                height[j] = 0
                return
func(height, summ)
ans = sorted(height)
for i in range(2, 9): print(ans[i])


