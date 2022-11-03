import sys
input = sys.stdin.readline

n = int(input())

tree = {}
for i in range(n):
    line = list(input().split())
    tree[line[0]] = [line[1], line[2]]


def preorder(node):     # (루트) (왼쪽 자식) (오른쪽 자식)
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):      # (왼쪽 자식) (루트) (오른쪽 자식)
    # print(node)
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])


def postorder(node):    # (왼쪽 자식) (오른쪽 자식) (루트)
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')