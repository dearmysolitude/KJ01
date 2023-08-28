# 배열 합치기

# 정렬되어 있는 두 배열 A와 B가 주어진다. (1 <= N, M <= 1,000,000)
# 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.
# 파이썬 set()을 사용한다면 정말 쉽게 풀 수 있는데...
# 정렬과 투포인터를 사용해서 풀 수 있는지 확인해보자

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A+B
print(*sorted(C))