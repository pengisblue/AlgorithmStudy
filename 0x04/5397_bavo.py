## 1406이랑 거의 비슷함

class Node:
    def __init__(self, val, next = None, prev = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev
    
    def print_node(self):
        start_node = self
        while start_node.next is not None:
            start_node = start_node.next
            print(start_node.val, end='')
        print()


T = int(input())

for _ in range(T):
    head_node = Node(None)
    curr_node = head_node

    input_text = input()

    for char in input_text:
        if char == '<':
            if curr_node.prev is not None:
                curr_node = curr_node.prev
        elif char == '>':
            if curr_node.next is not None:
                curr_node = curr_node.next
        elif char == '-':
            if curr_node.prev is not None:
                temp_prev = curr_node.prev
                temp_prev.next = curr_node.next
                if curr_node.next is not None:
                    curr_node.next.prev = temp_prev
                curr_node = temp_prev
        else:
            new_node = Node(char, next = curr_node.next, prev = curr_node)
            temp_next = curr_node.next
            curr_node.next = new_node
            if temp_next is not None:
                temp_next.prev = new_node
            curr_node = new_node

    head_node.print_node()