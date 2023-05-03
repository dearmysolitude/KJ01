#10869 사칙연산/입출력
# A, B = map(int, input().split())

def sol1(A, B):
    print(A+B, A-B, A*B, A//B, A%B, sep='\n')
    return

# sol1 (A, B)
#==========================================================================
# 2588 곱셈/입출력

def sol2(A, B):
    BH = B//100
    BD = B//10 - 10* BH
    BA = B - BH * 100 -BD * 10
    print(A * BA, A * BD, A * BH, A * B, sep='\n')
    return

#inputs = [input() for _ in range(2)]
#a = int(inputs[0])
#b = int(inputs[1])

#sol2(a, b)
#==========================================================================
# 9498 시험 성적/조건문
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
#==========================================================================
# 2753 윤년/조건문
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
#==========================================================================
# 1085 직사각형에서 탈출/조건문
# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

def sol5(compareList):
    X1 = compareList[2] - compareList[0]
    X2 = compareList[0]
    Y1 = compareList[3] - compareList[1]
    Y2 = compareList[1]
    list = [X1, X2, Y1, Y2]
    #반복문
    # min = list[0]
    # for i in range(len(list) -1):
    #     if list[i] > list[i+1]:
    #         min = list[i+1]
    #     else:
    #         min = list[i]
    # return print(min)
    #조건문
    if (X1 > X2): #pick X2
        if (Y1 > Y2): #pick Y2
            if (X2 > Y2): #pick Y2
                return print(Y2)
            else:
                return print(X2)
        else: #pick Y1
            if (X2 > Y1): #pick Y1
                return print(Y1)
            else: #pick X2
                return print(X2)
    else: #pick X1
        if (Y1 > Y2): #pick Y2
            if(X1 > Y2):
                return print(Y2)
            else:
                return print(X1)
        else: #pick Y1
            if(X1 > Y1):
                return print(Y1)
            else:
                return print(X1)
    #min 함수
    # # a = min(list) 숫자가 아닌 iterable 자료형인 경우 iteration에 있는 첫 번째 요소를 리턴
    # a = min(list)
    # return print(a)
    #리스트 정렬 함수
    # list.sort()
    # return print(list[0])

#compareList = list(map(int, input().split()))
# sol5(compareList)
#==========================================================================
# 2739 구구단/반복문
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

# num = int(input())
# format()함수
def sol6(a):
    for i in range(1, 10):
        str(a), str(i)
        print(a, "*", i, "=", a*i)
# sol6(num)
#==========================================================================
# 10950 A + B -3/반복문
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# for _ in range(int(input())): #함수로 만들지 않고 입력 오는대로 처리하여 보여 줌
#     a, b = map(int, input().split())
#     print(a + b)

def sol7(list, k):
    for i in range(k):
        print(list[i][0] + list[i][1])
# i = int(input()) #함수로 만들기 위해 입력을 배열로 받았다
# arr = [[0]*2 for _ in range(i)]
# for k in range(i):
#     arr[k] = list(map(int, input().split()))
# sol7(arr, i)
#============================================================================
# 2438 별찍기 - 1 / 반복문
#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
def sol8(a):
    for i in range(1, a+1):
        for j in range(1, i+1):
            print("*", end='')
        print('')
# num = int(input())
# sol8(num) 
#============================================================================
# 10871 X보다 작은 수 / 반복문
#List Comprehension <<파이썬 리스트의 이해
# [ ( 변수를 활용한 값 ) for ( 사용할 변수 이름 ) in ( 순회할 수 있는 값 )]
# nums = [list(map(int, (input().split()))) for _ in 행의 수] 2차원 배열 입력
def sol9(nums, input):
    for num in nums:
        if input > num:
            print(num, end=' ')

# a, b = map(int, input().split())
# numbers = list(map(int, (input().split()))) # << 주의: 1차원 배열 입력

# sol9(numbers, b)

#============================================================================
# 2562 최댓값 / 배열
#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#리스트
# arr = [] 하면 아무것도 초기화하지 않음
# arr.append(0)을 하면 arr의 0번째 인덱스이 값이 0이 됨
# 리스트에서 for문을 사용할 경우 앞쪽이 숫자더라도 인덱스가 아님!!!!!!!
def sol10(nums):
    maximum = 0
    i = 0
    for num in nums:
        if maximum < num:
            maximum = num
            maxindex = i
        i += 1
    print(maximum)
    print(maxindex+1)
# numbers = [int(input()) for _ in range(9)]
# numbers=[]
# for i in range(9):
#     numbers.append(int(input())) #input은 문자열로 인식
# sol10(numbers)
#============================================================================
# 8958 평균은 넘겠지 / 배열
def sol11(inputs):
    for input in inputs:
        point = 0
        os = input.split('X')
        for k in os:
            a = len(k)
            for x in range(1, a+1):
                point += x
        print(point)

# num = int(input())
# ans = [input() for _ in range(num)]

# sol11(ans)
#=============================================================================
# 2577 숫자의 개수 / 배열
def sol12(input):
    a = input[0]*input[1]*input[2]
    b = str(a)
    zero = b.count('0')
    one = b.count('1')
    two = b.count('2')
    three = b.count('3')
    four = b.count('4')
    five = b.count('5')
    six = b.count('6')
    seven = b.count('7')
    eight = b.count('8')
    nine = b.count('9')
    print(zero, one, two, three, four, five, six, seven, eight, nine, sep='\n')
# nums = [int(input()) for _ in range(3)]
# sol12(nums)

# 비교!
# print("dlf", "dl", "tka", end=':::')a
# print("dlf", "dl", "tka", sep=':::')
#=============================================================================
# 15596 정수 N개의 합 / 함수
def sol13(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
#=============================================================================
# 11654 아스키 코드 / 문자열
# a = input()
# b = ord(a)
# print(b)
#=============================================================================
#2675 문자열 반복 / 문자열
# import sys
def sol14(chars, num):
    for i in range(0, num):
        mul = int(chars[i][0]) # multiplication
        char = list(chars[i][1]) #문자열
        for k in range(0, len(char)):
            print(char[k]*mul, end='')
        print('')
# numb = int(input())
# chars = [sys.stdin.readline().split() for _ in range(numb)]
# sol14(chars, numb)
# chars = []
# chars.append(list(map(input().split())) for _ in range(numb))
# 정수 입력받을 경우
# for i in range(numb):
#     chars = list(map(int, sys.stdin.readline().split))

# number = 2
# string = [[3, 'ABC'], [5, '/HTP']]

#=============================================================================
# 1152 단어의 개수 / 문자열
import sys
def sol15(chars):
    n = 0
    for i in range(0, len(chars)):
        n += 1
    print(n)
# sentence = list(input().split())
# sol15(sentence)
#=============================================================================
# 2908 상수 / 문자열
#reverse 함수는 아무것도 반환하지 않는다 대신 해당 리스트에 변형이 생김
#reversed함수는 반환 함
def sol16(num1, num2):
    num1s = list(num1)
    num2s = list(num2)
    num1r = reversed(num1s) #반복자 타입으로 반환-메모리 상의 이득
    num2r = reversed(num2s) #반복자 타입으로 반환
    a = '' # string
    b = ''
    for letter in num1r:
        a += letter
    for letter2 in num2r:
        b += letter2
    if int(a) < int(b): #여기에서 형변환을 하여 비교했지만 실제 자료 값은 변하지 않음
        print(b)
    elif int(a) > int(b):
        print(a)
# a, b = map(str, input().split())
# sol16(a, b)
#=============================================================================
# 2869 달팽이는 올라가고 싶다 / 수학
import math
def sol17(a, b, v):
    n = (v-a)/(a-b)+1
    ans = math.ceil(n)
    print(ans)
# num1, num2, num3 = map(int, input().split())
# sol17(num1, num2, num3)
#=============================================================================
# 1978 소수 찾기 / 수학
import sys, math
def prime(number):
    if number == 1:
        return False
    else:
        i = 2
        while i <= math.ceil(number/2): #2 , 짝수!
            if(number % i == 0):
                return False
            i += 1
        return True
def sol18(numbers):
    n = 0
    for number in numbers:
        if (prime(number) == True):
            n += 1
    print(n)
# n = input()
# nums = list(map(int, input().split()))
# sol18(nums)
#=============================================================================
# 9020 골드바흐의 추측 / 수학
import sys, math
def prime(number):
    if number == 1:
        return False
    else:
        i = 2
        while i <= math.ceil(number/2): #2 , 짝수!
            if(number % i == 0):
                return False
            i += 1
        return True
def goldbach(numbers):
    for number in numbers:
        base = int(number/2)
        for i in range(0, base):
            a = base + i
            b = base - i
            if (prime(a) == True and prime(b) == True):
                print(b, a)
                break
# n = int(input())
# nums = list(int(sys.stdin.readline()) for _ in range(n))
# goldbach(nums)
#=============================================================================
# 1065 한수 / 수학
def sol19(number):
    if number < 100:
        print(number)
    else:
        n = 99
        for num in range(100, number+1):
            nh = num // 100
            nt = num // 10 - nh*10
            no = num % 10
            if (nt*2 == (nh + no)):
                n += 1
        print(n)
# num = int(input())
# sol19(num)
#=============================================================================
# 2628 종이자르기 / 수학
import sys
def sol20(square, num, cuts) -> None:
    pla = 0
    hor = 0 #자르는 횟수#
    plaPoints = []
    horPoints = []
    if num != 0: #예외 처리
        for i in range(0, num):
            if (cuts[i][0] == 0): #가로로 자른다면
                pla += 1 #가로로 자르는 횟수
                plaPoints.append(cuts[i][1])
            else: #세로로 자른다면
                hor += 1 #세로로 자르는 횟수
                horPoints.append(cuts[i][1])
    elif num == 0:
        print(square[0]*square[1])
        return
    # 리스트 오름차순으로 정렬 각 좌표계의 0과 최대값을 추가하여 나중에 길이를 만들 for문이 복잡해지지 않도록 하자
    # pla와 hor하나씩 추가하여 #길이 수#로 맞춰준다.
    plaPoints.sort()
    horPoints.sort()
    plaPoints.insert(0, 0)
    plaPoints.append(square[1]) #주의: 가로로 자른 경우 좌표의 최대값은 y축임
    pla += 1
    horPoints.insert(0, 0)
    horPoints.append(square[0]) #
    hor += 1
    #길이들의 리스트를 만들어 값들을 추가하여보자. 가로로 잘라서 만들어진 길이는 y축 상에 있으므로 세로라고 표기해야 맞지만 편의상 plaLen으로 한다
    plaLen = []
    horLen = []
    for j in range(0, pla):
        plaLen.append(plaPoints[j+1]-plaPoints[j])
    for k in range(0, hor):
        horLen.append(horPoints[k+1]-horPoints[k])
    # 다시 오름차순 정럴하여 가장 큰 면적을 구하면 된다.
    plaLen.sort()
    horLen.sort()
    Biggist = plaLen[-1]*horLen[-1]
    print(Biggist)
    return

# sq = [10, 8]
# numb = 3
# cuts = [[0, 3], [1, 4], [0, 2]]

# sq = list(map(int, input().split())) # list(int(input().split()))<-잘못
# numb = int(input())
# cuts = [list(map(int, input().split())) for _ in range(numb)]
# sol20(sq, numb, cuts)
#=============================================================================
# 10872 팩토리얼 / 재귀함수
def sol21(num,ans) -> None:
    if num > 1:
        ans = ans*num
        sol21(num-1, ans)
    elif num == 1 or num == 0:
        print(ans)
# number = int(input())
# sol21(number, 1)
#=============================================================================
# 하노이 탑 / 재귀함수
def hanoy(num) -> int:
    # 옮겨야 하는 디스크의 숫자를 재귀 함수의 번호로 생각한다. hanoy(1)은 1개 디스크를 옮기는 데 필요한 횟수
    if num == 0: # 재귀함수의 기저
        return 0
    ans = 2 * hanoy(num-1) + 1
    return ans

def hanoysteps(num, startP, endP):
    if num == 1: #<<- 처음 할 때에는 기저 설정이 잘못되어 있었다
        print(startP, endP)
        return
        #<
    indi = ['', 0, 0, 0] #3개의 탑 중에서 스타트 포인트와 엔드 포인트가 아닌 포인트를 찾는 과정
    #print(indi) indicator를 사용하다보니 i가 0, 1, 2를 도는 것을 확인하지 못했다
    for i in range(1, 4):
        if startP == i:
            indi[i] = 1 #startpoint가 있는곳의 index를 1로 바꾼다
        if endP == i:
            indi[i] = 1 # endpoint가 있는 곳의 index를 1로 바꾼다
    neither = indi.index(0)

    hanoysteps(num-1, startP, neither)
    print(startP, endP)
    hanoysteps(num-1, neither, endP)

def sol22(number):
    if number > 20:
        stp = hanoy(number)
        print(stp)
    else:
        stp = hanoy(number)
        print(stp)
        hanoysteps(number, 1, 3)
# num = int(input())
# sol22(num)
#=============================================================================
# # N-Queen 재귀함수
# # 가이드(<Do it! 자료구조와 함께 배우는 알고리즘 입문> 참고)
# # flag 를 추가하여 한 열씩 퀸을 추가하되 같은 행, 대각선 두 방향을 확인할 수 있는 flag로 확인한다
# # 대각선의 위치가 i와 j로 특정지어질 수 있음을 떠올릴 수 있어야 한다.
# def N_queen_part(i,fRaw, num, f1, f2, qPos, canDo) -> int: # qPos: 여왕을 배치하는 2차원 배열 / idx: 여왕의 위치 중 i
#     if i == num-1:
#         return canDo
#     pot = num-i #이번에 갈 수 있는 potential 위치#
#     for j in range(0, num):#
#         if (i-j)+

#     canDo *= pot #지금까지 생성된 가짓수
#     N_queen_part(i+1, fRaw, num, f1, f2, qPos, canDo)

# def N_queen(num):
#     count = 0
#     fRaw = [True]*num #raw
#     f1 = [True]*2*(num-1) #대각선 1, i+j
#     f2 = [True]*2*(num-1) #대각선 2, i-j
#=============================================================================
# def sol23(N, r, c):
#     r//2

#=============================================================================
#2750 수 정렬하기 / 정렬 *여러가지 정렬로 만들어보자*
def bubble24_1(nums): #버블
    #쉐이커 정렬로도 바로 구현 가능
    while True:
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                count =+ 1
        if count == 0:
            break
    for i in range(len(nums)):
        print(nums[i])

def bubble24_2(nums): # 좋은 예시**
    #개선: 버블 단계 중 다음 리스트들이 정렬이 완료되어 있으면 더이상 그 부분은 정렬하지 않도록
    n = len(nums)
    k = 0
    while k < n-1:
        last = n - 1
        for i in range(n-1, k, -1):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                last = i
        k = last
    printArray(nums)
  
def sSelection(nums): #단순 선택
    n = len(nums)
    for i in range(n-1):
        min = i #정렬할 부분 중 작은 것의 인덱스
        for j in range(i+1, n):
            if nums[j]< nums[min]:
                min=j
        nums[i], nums[min] = nums[min], nums[i]
    printArray(nums)

def printArray(nums):
    for j in range(len(nums)):
        print(nums[j])
        
# count = int(input())
# numbers = [int(input()) for _ in range(count)]
# bubble24_2(numbers)

#=============================================================================
# 2751 수 정렬하기 2 정렬
# 재귀적 퀵소트
import sys
def qSortpart(nums, left, right):
    pL = left
    pR = right

    mid = nums[(left + right) // 2]
    while pL <= pR:
        while nums[pL] < mid: pL += 1
        while nums[pR] > mid: pR -= 1
        if pL <= pR:
            nums[pL], nums[pR] = nums[pR], nums[pL]
            pR -= 1
            pL += 1

    if left < pR: qSortpart(nums, left, pR) # **
    if pL < right: qSortpart(nums, pL, right) # **
    return

def qSort(nums):
    n = len(nums)
    qSortpart(nums, 0, n-1)
    for i in range(n):
        print(nums[i])

# tc = int(input())
# numbers = [int(sys.stdin.readline()) for _ in range(tc)]
# qSort(numbers)
# recursion을 너무 많이 돌아 오류가...

import sys
def sort(nums):
    nums.sort()
    for i in range(len(nums)): print(nums[i])
    return
# tc = int(input())
# numbers = [int(sys.stdin.readline()) for _ in range(tc)]
# sort(numbers)


#=============================================================================
# 10989 도수정렬 수 정렬하기
# import sys
# tc = int(input())
# nums = [0] * 10001

# for i in range(tc):
#     input = int(sys.stdin.readline())
#     nums[input] = nums[input] + 1

# for i in range(len(nums)):
#     if nums[input] != 0:
#         print(i)

# import sys
# tc = int(input())
# nums = [0] * 10001

# for i in range(tc):
#     input = int(sys.stdin.readline())
#     nums[input] += 1

# for i in range(len(nums)):
#     for k in range(nums[i]):
#         if nums[i] != 0:
#             print(i)


# def countingSort(nums):
#     maximum = max(nums)
#     count = [0] * (maximum+1)
#     n = len(nums)
#     for i in range(n):
#         count[nums[i]] += 1

#     for i in range(1, maximum+1):
#         if count[i] != 0:
#             for k in range(count[i]):
#                 print(i)
    # for i in range(1, len(count)):
    #     if count[i] != 0:
    #         for k in range(count[i-1], count[i]):
    #             nums[k] = i
    # for i in range(n): print(nums[i])
    # return
# countingSort(numbers)
# 카운트 배열의 크기 줄이기 / In-place sorting 적용 / 메모리 최적화 방법: 입력 데이터 분할
# 배열 바꾸기보다 인쇄만 하면 되지!
#=============================================================================
#1181 단어 정렬
inN = int(input())
letters=[]
for i in range(inN):
    letters.append(input())
temp = list(set(letters))

sortedW= []
for i in temp:
    sortedW.append((len(i), i))

result = sorted(sortedW)
for len_word, word in result:
    print(word)