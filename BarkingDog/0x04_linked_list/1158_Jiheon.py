class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


N, K = map(int, input().split())

head = Node(1)
node = head

# 주어진 N 길이로 Node 를 연결
for i in range(1, N):
    while node:
        if node.next is None:
            node.next = Node(i+1)
            break
        node = node.next

node = head

# N 번째 Node 와 head를 연결하여 순환리스트 형성
while node:
    if node.next is None:
        node.next = head
        break
    node = node.next

ls = []

# K-1 번째 노드의 next값을 print
# next.next 값을 연결하여 node.next 값을 연결에서 탈락
for i in range(N):
    for j in range(K-1):
        node = node.next
    ls.append(str(node.next.data))
    node.next = node.next.next

print('<', end = '')
print(', '.join(ls), end = '')
print('>')
    
