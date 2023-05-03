# 9095
number = int(input())
nums = list(int(input()) for i in range(number))
def sol(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return sol(num-1) + sol(num-2) + sol(num-3)
for num in nums:
    print(sol(num))


# 동적계획법