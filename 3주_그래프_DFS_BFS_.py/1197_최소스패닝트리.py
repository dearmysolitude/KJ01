import sys
input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())

# Kruskal Algorithm

edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C)) # ###리스트로 받아진다###
edges.sort(key=lambda x: x[2]) #Cost 오름차순으로 정렬, 이대로 for하므로 작은 것부터 고려된다

#Union_Find
parent = [i for i in range(V+1)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x]) #get_parent거슬러 올라가면서 parent[x]값도 갱신
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b: #작은 쪽이 부모가 된다.(한 집합관계라 부모가 따로 있지 않음)
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

##여기까지가 Union-Find를 사용하는 크루스칼 알고리즘

answer = 0
for a, b, cost in edges:
    #cost가 작은 edge부터 추가해 가면서 같은 부모를 공유하지 않을 때만 추가
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost
print(answer)