# 10773 제로
K = int(input())
def helper(number):
    stack = []
    ans = 0
    for _ in range(number):
        a = int(input())
        if a == 0:
            if len(stack) == 0:
                continue
            stack.pop()
        else:
            stack.append(a)
    for num in stack:
        ans += num
    print(ans)
helper(K)
