
#10869 사칙연산================================
# A, B = map(int, input().split())

def sol1(A, B):
    print(A+B, A-B, A*B, A//B, A%B, sep='\n')
    return

# sol1 (A, B)

# 2588 곱셈 ====================================
#inputs = [input() for _ in range(2)]

def sol2(A, B):
    BH = B//100
    BD = B//10 - 10* BH
    BA = B - BH * 100 -BD * 10
    print(A * BA, A * BD, A * BH, A * B, sep='\n')
    return

#a = int(inputs[0])
#b = int(inputs[1])

#sol2(a, b)

# 9498 시험 성적 ===============================
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

#input = int(input())

def sol3(a):
    if a >= 90:
        print("A")
        return 
    elif a >= 80 and a < 90:
        print("B")
        return
    elif a >= 70 and a < 80:
        print("C")
        return
    elif a >= 60 and a < 70:
        print("D")
        return
    else:
        print("F")
        return
    
#sol3(input)

# 2753 윤년=======================================
#연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
#윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

# i = int(input())

def sol4(a):
    if (a % 400 == 0):
        return print(1)
    elif(a % 4 == 0 and a % 100 != 0):
        return print(1)
    else:
        return print(0)

# sol4(i)

# 1085 ============================================
# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

def sol5(compareList):
    list = [compareList[2] - compareList[0], compareList[0], compareList[3] - compareList[1], compareList[3]]
    a = min(list)

    return print(a)
    # if (X1 > X2): #pick X2
    #     if (Y1 > Y2): #pick Y2
    #         if (X2 > Y2): #pick Y2
    #             return print(Y2)
    #         else:
    #             return print(X2)
    #     else: #pick Y1
    #         if (X2 > Y1): #pick Y1
    #             return print(Y1)
    #         else: #pick X2
    #             return print(X2)
    # else: #pick X1
    #     if (Y1 > Y2): #pick Y2
    #         if(X1 > Y2):
    #             return print(Y2)
    #         else:
    #             return print(X1)
    #     else: #pick Y1
    #         if(X1 > Y1):
    #             return print(Y1)
    #         else:
    #             return print(X1)

#compareList = list(map(int, input().split()))

compareList = [2, 1, 4, 5]
sol5(compareList)