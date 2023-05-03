test = [1, 2, 3]
test_len = len(test)

N = 2 #뽑을 순열의 개수
visit = [0] * test_len #해당 index의 값을 사용했는지 여부
arr = [0] * N #현재 순열을 담을 배열
arr_list = [] #모든 순열을 담을 배열

def permutation(level):
    if level >= N:
        arr_list.append(arr[:])#얕은 복사 통해서 현재 순열을 추가한다.
        return
    else:
        for i in range(test_len):
            if visit[i]: continue #이미 순열로 들어가 있다면 통과
            visit[i] = 1
            arr[level] = test[i] #순열을 선택
            permutation(level + 1) #재귀를 통해 반복
            visit[i] = 0 #다음 트리로 내려가기 위해서 이전의 방문처리를 롤백

permutation(0) #0개의 원소를 선택한 경우부터 시작
print(arr_list)

def Combination(arr, r):
    #1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    #2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return
        
        #3. 
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])