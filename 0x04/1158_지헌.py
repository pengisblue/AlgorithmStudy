class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


N, K = map(int, input().split())

head = Node(1)
node = head

for i in range(1, N):
    while node:
        if node.next is None:
            node.next = Node(i+1)
            break
        node = node.next

node = head

while node:
    if node.next is None:
        node.next = head
        break
    node = node.next

ls = []

for i in range(N):
    for j in range(K-1):
        node = node.next
    ls.append(str(node.next.data))
    node.next = node.next.next

print('<', end = '')
print(', '.join(ls), end = '')
print('>')
    
