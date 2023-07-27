# 1406 에디터와 거의 비슷한 문제!

class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


N = int(input())

for i in range(N):
    log = input()
    head = Node(None)
    
    node = head

    for i in log:
        if i == '<':
            if node.prev is not None:
                node = node.prev
        elif i == '>':
            if node.next is not None:
                node = node.next
        elif i == '-':
            if node.prev is not None:
                temp_node = node.prev
                temp_node.next = node.next
                if node.next is not None:
                    node.next.prev = temp_node
                node = temp_node
        else:
            temp_node = node.next
            new_node = Node(i, next = temp_node, prev = node)
            node.next = new_node
            if temp_node is not None:
                temp_node.prev = new_node
            node = new_node
            
    
    node = head

    while node.next is not None:
        node = node.next
        print(node.data, end = '')
    print()