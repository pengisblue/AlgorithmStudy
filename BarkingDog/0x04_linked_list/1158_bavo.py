class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data          
        self.next = next or self


N, K = map(int,input().split())

head_node = Node(1, None)
curr_node = head_node

for i in range(2, N + 1):
    new_node = Node(i, None)
    curr_node.next = new_node
    curr_node = new_node
else:
    # 리스트 연결 다하면 꼬리가 헤드를 물어야함
    curr_node.next = head_node

result_list = []

#노드가 자가 참조하면 끝
while curr_node.next != curr_node:
    for _ in range(K - 1): 
        curr_node = curr_node.next
    result_list.append(curr_node.next.data)
    curr_node.next = curr_node.next.next
else: # 다 돌고나면 남은 노드 data도 append
    result_list.append(curr_node.data)


print('<' ,', '.join(map(str, result_list)), '>', sep='')