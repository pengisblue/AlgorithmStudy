import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.base = self.root
            while True:
                if data == self.base.data:
                    print("중복된 KEY 값")
                    break
                elif data > self.base.data:
                    if self.base.right is None:
                        self.base.right = Node(data)
                        break
                    else:
                        self.base = self.base.right
                else:
                    if self.base.left is None:
                        self.base.left = Node(data)
                        break
                    else:
                        self.base = self.base.left

    def search(self, data):
        self.base = self.root
        while self.base:
            if self.base.data == data:
                return True
            elif self.base.data > data:
                self.base = self.base.left
            else:
                self.base = self.base.right
        return False

    def remove(self, data):
        self.searched = False
        self.cur_node = self.root
        self.parent = self.root
        while self.cur_node:
            if self.cur_node.data == data:
                self.searched = True
                break
            elif self.cur_node.data > data:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.left
            else:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.right
        if self.searched:
            # root를 지우는 경우
            if self.cur_node.data == self.parent.data:
                self.root = None
            else:
                # [CASE 1] 삭제하는 node가 leaf node인 경우
                if self.cur_node.left is None and self.cur_node.right is None:
                    if self.parent.data > self.cur_node.data:
                        self.parent.left = None
                    else:
                        self.parent.right = None

                # [CASE 2] 삭제하는 node의 자식이 하나인 경우
                elif self.cur_node.left is not None and self.cur_node.right is None:
                    if self.parent.data > data:
                        self.parent.left = self.cur_node.left
                    else:
                        self.parent.right = self.cur_node.left
                elif self.cur_node.left is None and self.cur_node.right is not None:
                    if self.parent.data > data:
                        self.parent.left = self.cur_node.right
                    else:
                        self.parent.right = self.cur_node.right

                # [CASE 3] 삭제하는 node의 자식이 둘인 경우
                elif self.cur_node.left is not None and self.cur_node.right is not None:
                    self.tmp_parent = self.cur_node.right
                    self.tmp_cur = self.cur_node.right
                    while self.tmp_cur.left:
                        self.tmp_parent = self.tmp_cur
                        self.tmp_cur = self.tmp_cur.left
                    if self.tmp_cur.right is not None:
                        self.tmp_parent.left = self.tmp_cur.right
                    else:
                        self.tmp_parent.left = None
                    if self.parent.data > data:
                        self.parent.left = self.tmp_cur
                    else:
                        self.parent.right = self.tmp_cur
                    self.tmp_cur.left = self.cur_node.left
                    self.tmp_cur.right = self.cur_node.right
        else:
            print("존재하지 않는 데이터")

    # 전위 순회
    def pre_order_traverse(self, node):
        if not node:
            return
        print(node.data, end=' ')
        self.pre_order_traverse(node.left)
        self.pre_order_traverse(node.right)

    # 중위 순회
    def in_order_traverse(self, node):
        if not node:
            return
        self.in_order_traverse(node.left)
        print(node.data, end=' ')
        self.in_order_traverse(node.right)

    # 후위 순회
    def post_order_traverse(self, node):
        if not node:
            return
        self.post_order_traverse(node.left)
        self.post_order_traverse(node.right)
        print(node.data, end=' ')


T = int(input())
for t in range(1, T + 1):
    bst = Binary_Search_Tree()
    N = int(input())
    E = N - 1  # 간선의 수
    arr = []
    for n in range(1, N + 1):
        bst.insert(n)

    bst.pre_order_traverse(bst.root)
    print()
    bst.in_order_traverse(bst.root)
    print()
    bst.post_order_traverse(bst.root)
    print()
