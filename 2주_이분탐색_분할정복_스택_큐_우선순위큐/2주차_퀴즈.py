



























# 해답 예

# def moo(start, end, N): # (25, 5, 11)
#     mid = (start-end)//2 # mid = 10
#     if N <= mid:
#         return moo(mid, end-1, N)
#     elif N > mid+end:
#         return moo(mid, end-1, N-mid-end)
#     else:
#         return “o” if N-mid-1 else “m” # N 이 가운데 부분의 첫번째면 m 이고 아니면 o 이다.
#                                        # if N-mid-1 == 0 return m else return 0
# start, n = 3, 0
# while N > start: # 11 > 3, 11 > 10
#     n += 1 # 가운데 부분의 길이 n 이 1씩 증가
#     start = start*2+n+3 # 10 = 3*2+1+3, 25 = 10*2+2+3,
# print(moo(start, n+3, N)) # (25, 5, 11)





