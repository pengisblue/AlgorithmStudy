import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

string = input().rstrip()

head = Node(0)
node = head


for char in string:
    # double linked list로 초기화
    new_node = Node(char, prev= node)
    node.next = new_node
    node = new_node

M = int(input())
for i in range(M):
    ip = input()
    if ip[0] == 'L':
        if node.prev is not None:
            node = node.prev
    elif ip[0] == 'D':
        if node.next is not None:
            node = node.next
    elif ip[0] == 'B':
        if node.prev is not None:
            temp_node = node.prev
            temp_node.next = node.next
            if node.next is not None:
                node.next.prev = temp_node
            node = temp_node
    else:
        temp_node = node.next
        new_node = Node(ip[2], next = temp_node, prev = node)
        node.next = new_node
        if temp_node is not None:
            temp_node.prev = new_node
        node = new_node

node = head

while node.next is not None:
    node = node.next
    print(node.data, end = '')