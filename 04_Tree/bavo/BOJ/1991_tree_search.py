def pre(node):
    print(node, end='')
    if tree[node][0] is not None:
        pre(tree[node][0])
    if tree[node][1] is not None:
        pre(tree[node][1])


def inorder(node):
    if tree[node][0] is not None:
        inorder(tree[node][0])
    print(node, end='')
    if tree[node][1] is not None:
        inorder(tree[node][1])


def post(node):
    if tree[node][0] is not None:
        post(tree[node][0])
    if tree[node][1] is not None:
        post(tree[node][1])
    print(node, end='')


tree = dict()

N = int(input())

for _ in range(N):
    p, c1, c2 = input().split()
    tree[p] = [None, None]
    if c1 != '.':
        tree[p][0] = c1

    if c2 != '.':
        tree[p][1] = c2

pre('A')
print()
inorder('A')
print()
post('A')

