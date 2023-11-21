# 대칭 차집합

# 대칭 차집합:(A-B) 와 (B-A)의 합집합
import sys
input = sys.stdin.readline

Na, Nb = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sym_diff = list(set(A) ^ set(B))
print(len(sym_diff))