# # 큐를 다룰 때 front / tail를 인덱스에서만 다루는 게 아니라 리스트를 조작해야 할까?
# import sys
# N = int(input())
# def queue(N):
#     queue = []
#     tail = -1 # tail를 리스트의 끝
#     front = 0 # front 을 리스트의 시작으로
#     for i in range(N):
#         user_input= sys.stdin.readline().split()
#         if user_input[0] == 'push':
#             queue.append(int(user_input[1]))
#         elif user_input[0] == 'pop':
#             if len(queue) != 0:
#                 print(queue[front])
#                 del queue[front]
#             else: print(-1)
#         elif user_input[0] == 'size':
#             print(len(queue))
#         elif user_input[0] == 'empty':
#             if len(queue) == 0:
#                 print(1)
#             else:
#                 print(0)
#         elif user_input[0] == 'front':
#             if len(queue) != 0:
#                 print(queue[front])
#             else: print(-1)
#         elif user_input[0] == 'back':
#             if len(queue) != 0:
#                 print(queue[tail])
#             else: print(-1)
# queue(N) # 시간 초과
#======================================================================
# import sys
# from collections import deque
# N = int(input())
def queue(N):
    q = deque()
    for i in range(N):
        user_input= sys.stdin.readline().split()
        if user_input[0] == 'push':
            q.append(user_input[1])

        elif user_input[0] == 'pop':
            if len(q) != 0:
                print(q.popleft())
            else: print(-1)

        elif user_input[0] == 'size':
            print(len(q))

        elif user_input[0] == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)

        elif user_input[0] == 'front':
            if len(q) != 0:
                print(q[0])
            else: print(-1)

        elif user_input[0] == 'back':
            if len(q) != 0:
                print(q[-1])
            else: print(-1)
# queue(N) # deque의 시간복잡도는 O(1)
#======================================================================
# 카드 2
# import sys
# from collections import deque
# N = int(input())
def cardDeck2(N):
    cards = deque(maxlen=N+1)
    for i in range(N):
        cards.append(i+1)
    while not len(cards) == 1:
        cards.popleft()
        a = cards.popleft()
        cards.append(a)
    print(cards[0])
# cardDeck2(N)
#======================================================================
# 요세푸스 문제
from collections import deque
N, K = map(int, input().split())
def josephus(n, k):
    q = deque(maxlen = n+1)
    ans = []
    for i in range(n):
        q.append(i+1)
    while len(q) != 0:
        q.rotate(-k+1)
        ans.append(q.popleft())
    print('<', end='')
    for i in range(n-1) :print(ans[i], end=', ')
    print(ans[-1], '>', sep='')
josephus(N, K)
#======================================================================
# 최대 힙
N = int(input())
numbers = list(int(input()) for _ in range(N))

