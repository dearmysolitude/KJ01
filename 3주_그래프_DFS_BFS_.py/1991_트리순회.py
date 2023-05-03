
# # #노드와 트리의 초기화
# class Node(object):
#     def __init__(self, item):
#         self.item = item
#         self.left = self.right = None

# # class BinaryTree(object):
#     def __init__(self):
#         self.root = None

# #전위 순회
# ans1 = []
# ans2 = []
# ans3 = []

# def preorder(i):
#     ans1.append(tree[i][0])
#     for k in range(1, 3):
#         if tree[i][k] != '.':

#             for j in range(i, N):
#                 if tree[i][k] == tree[j][0]:
#                     preorder(j)

# def inorder(i):
#     if tree[i][1] != '.':
#         for j in range(i, N):
#             if tree[j][0] == tree[i][1]:
#                 preorder(j)
#     ans2.append(tree[i][0])
#     if tree[i][2] != '.':
#         for j in range(i, N):
#             if tree[j][0] == tree[i][2]:
#                 preorder(j)

# def postorder(i):
#     for k in range(1, 3):
#         if tree[i][k] != '.':
#             for j in range(i, N):
#                 if tree[j][0] == tree[i][k]:
#                     preorder(j)
#     ans3.append(tree[i][0])

# preorder(0)
# inorder(0)
# postorder(0)
# for x in ans1:
#     print(x, end='')
# print()

# for x in ans2:
#     print(x, end='')
# print()
# for x in ans3:
#     print(x, end='')

# import sys
# N = int(input())
# tree = []
# for i in range(N):
#     tree.append(sys.stdin.readline().rstrip().split())

# ans =[]
# def sol(i):
#     global N
#     ans.append(tree[i][0])#전위 탐색
#     left = 2*i+1 #모든 노드에 수치가 들어있지 않기 때문에 이렇게 접근하면 안됩니다.
#     right = 2*i+2 
#     if tree[i][1] != '.':
#         if left >= N:
#             return
#         sol(left)
#     if tree[i][2] != '.':
#         if right >= N:
#             return    
#         sol(right)
#     return
# sol(0)
# print(ans)

# 딕셔너리
import sys
N = int(input())
tree = {}
for i in range(N):
    root, left, right = sys.stdin.readline().rstrip().split()
    tree[root] = [left, right]
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')