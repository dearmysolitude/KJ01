import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().rstrip().split())

minimum = 1e9
maximum = -1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global minimum, maximum

    if depth == N-1:
        minimum = min(total, minimum)
        maximum = max(total, maximum)
        return
    
    if plus:
        dfs(depth + 1, total + nums[depth+1], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth+1], plus, minus -1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth+1], plus, minus, multiply -1, divide)
    if divide:
        dfs(depth + 1, int(total/nums[depth+1]), plus, minus, multiply, divide-1)

dfs(0, nums[0], plus, minus, multiply, divide)
print(maximum)
print(minimum)

