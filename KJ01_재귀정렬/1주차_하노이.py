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