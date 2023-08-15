import sys
input = sys.stdin.readline

class Node:
    def __init__(self, val, next = None, prev = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


# 커서가 위치할 수 있는 경우의 수 = L + 1
# 맨 앞에 더미 노드 있어야함
head_dummy = Node(None)

# current_node == 현재 커서 위치
current_node = head_dummy

# 시작 문장
input_text = input()


for char in input_text:
    # double linked list로 초기화
    new_node = Node(char, prev= current_node)
    current_node.next = new_node
    current_node = new_node

M = int(input())

for _ in range(M):
    command = input().rstrip()
    # 왼쪽
    if command == 'L':
        # 현재 노드가 더미노드(헤드)가 아닐때 앞으로
        if current_node.prev is not None:
            current_node = current_node.prev
    #오른쪽
    elif command == 'D':
        # 현재 노드가 꼬리가 아닐때 뒤로
        if current_node.next is not None:
            current_node = current_node.next
    #삭제
    elif command == 'B':
        #현재 노드가 더미노드(헤드) 아닐때 현재 노드 삭제
        if current_node.prev is not None:
            # 현재노드의 앞노드
            temp_node = current_node.prev
            # '123'이면 1이 원래 2를 가리켰는데 3을 가리키게
            temp_node.next = current_node.next
            # 꼬리노드가 현재일 때 삭제하면 next node가 None이라 next node의 prev를 수정할 필요 없음
            if current_node.next is not None:
                current_node.next.prev = temp_node
            # 지우기 전 기준으로 prev노드가 지운 후 커서의 위치
            current_node = temp_node
    else:
        # 글 입력할때
        temp_next = current_node.next
        new_node = Node(command[2], next = temp_next, prev = current_node)
        current_node.next = new_node
        # 맨 끝에서 입력하면 next가 None임
        if temp_next is not None:
            temp_next.prev = new_node
        current_node = new_node
        
current_node = head_dummy

while current_node.next is not None:
    current_node = current_node.next
    print(current_node.val, end='')

