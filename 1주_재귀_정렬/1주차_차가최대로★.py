import math
inNum = int(input())
A = [] 
#퐁당퐁당
for i in range(inNum):
    A.append(int(input()))

summation = 0
maximum = 0
B = sorted(A)
moveIdx = math.floor(inNum/2)
C = []

for i in range(-moveIdx, inNum):
    C.append(B[i].pop())

k=0
for j in range(0, moveIdx):
    B.insert(j, C[k])
    k += 1

B.insert(0, B[-1].pop())
       
for i in range(1, inNum):
        summation += abs(B[i-1]-B[i])


# 혹은 permutation을 통해서


