import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) # 정점 수
A = list(map(int,list(input().strip()))) # 실내/외 여부 

graph = [[] for _ in range(n+1)] # 연결리스트
place = [0 for _ in range(n+1)] # 실내: 1, 실외: 0
visited = [False for _ in range(n+1)] # 방문 여부

# place  초기화
for i in range(len(A)):
    if A[i] == 1:
        place[i+1] = 1

# 연결리스트 입력
for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs함수
def dfs(i):
    res = 0
    for next_node in graph[i]: ##이렇게 쓸 수도 있군
        if place[next_node] == 0: #다음 노드가 실외고
            if not visited[next_node]: #방문 안했으면
                visited[next_node] = True
                res += dfs(next_node)
        else: #실내라면
            res += 1
    return res

ans = 0
for i in range(1, n+1):
    if place[i] == 0: # 실외인 경우
        if not visited[i]:
            visited[i] = True
            res = dfs(i)
            ans += res * (res - 1)
    else: #실내인 경우 따로 더하면 된다
        for next_node in graph[i]:
            if place[next_node] == 1: # 연속된 실내인 경우
                ans += 1
print(ans)

    # if not visited[i]:
    #     next_place = i + 1
    #     visited[i] = True
    #     if place[i] == 0: # 현재 실외
    #         if place[next_place] == 0:
    #             dfs_walk(next_place) # 계속 내려감
    #         else:
    #             cnt += 1 # cnt += 1
    #             dfs_walk(next_place)
    #     else: 
    #         # 현재 실내
    # return cnt

# # dfs 시작 노드: 실외
# for i in range(n+1):
#     if place[i] == 0:
#         dfs(i)


# 현재가 실외이고 -다음이 실내인 경우: cnt+=1
#       실외이고 -다음이 실외인 경우: 계속 내려감
# 현재가 실내이고 -다음이 실내인 경우: 별개 조건으로 서로 출발/도착이 되는 경우를 추가한다
#       실내이고 -다음이 실외인 경우: 다음 그래프로 분류한다.
# 각 노드들은 내려갈 수 있는지 계속해서 판단해야한다.

# # 참고 코드
# from sys import stdin, setrecursionlimit
# setrecursionlimit(10**9)

# stdin = open('example.txt', 'r')

# def dfs(v, cnt): # v: 정점 번호, cnt : 실외와 연결된 실내 노드 개수 카운트
#     visited[v] = True

#     for i in graph[v]: # 노드 v와 연결된 인접 노드를 하나씩 불러온다
#         if location[i] == 1: # 해당 노드의 위치가 실내이면
#             cnt += 1 # 실내 개수 카운트에 +1 해준다.
#         elif not visited[i] and location[i] == 0: # 방문하지 않았고, 해당 i점의 위치가 실외라면
#             cnt = dfs(i, cnt) # 해당 실외점을 기준으로 dfs를 돈다
#     return cnt

# ans = 0
# n = int(stdin.readline()) # 정점수 받기

# # location 정보 받아오기 : 앞에 0이 추가되는 이유는 노드의 인덱스 번호를 1부터 시작하기 위해
# location = [0]+list(map(int, stdin.readline().strip()))

# graph = [[] for _ in range(n+1)] # 1번 노드부터 n번까지 받아오기위해 빈 공간 생성

# for _ in range(n-1): 
#     a, b = map(int, stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#     if location[a] == 1 and location[b] == 1: # 둘다 실내이면
#         ans +=2 # 서로 방문하는 케이스가 2가지이니 바로 2개 세기

# sum = 0
# visited = [False] * (n+1)
# for i in range(1, n+1):
#     if not visited[i] and location[i] == 0: # 실외를 기준으로
#         x = dfs(i, 0) # 현재 cnt는 0
#         sum += x*(x-1) # 실외인 노드를 기준으로 인접 노드 애들 개수 세는 것이 n * (n -1)이므로 실외 노드 걸릴때마다 전부 세기

# print(sum+ans)
