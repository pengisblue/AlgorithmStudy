# 에디터

import sys
class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self

    def __str__(self):
        return str(self.key)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def __iter__(self):
        current_node = self.head.next
        while current_node != self.head:
            yield current_node
            current_node = current_node.next

    def __str__(self):
        return "".join(str(node.key) for node in self)

    def splice(self, start_node, end_node, insertion_point):
        if start_node is None or end_node is None or insertion_point is None:
            return

        start_node.prev.next = end_node.next
        end_node.next.prev = start_node.prev

        insertion_point.next.prev = end_node
        end_node.next = insertion_point.next
        start_node.prev = insertion_point
        insertion_point.next = start_node

    def move_after(self, node_to_move, insertion_point):
        self.splice(node_to_move, node_to_move, insertion_point)

    def move_before(self, node_to_move, insertion_point):
        self.splice(node_to_move, node_to_move, insertion_point.prev)

    def insert_before(self, node_to_insert, insertion_point):
        self.move_before(node_to_insert, insertion_point)

    def delete_node(self, node_to_delete):
        if node_to_delete is None or node_to_delete == self.head:
            return

        node_to_delete.prev.next, node_to_delete.next.prev = node_to_delete.next, node_to_delete.prev



linked_list = DoublyLinkedList()

cursor_node = Node('|')
cursor_node.next = linked_list.head
cursor_node.prev = linked_list.head

linked_list.head.next = cursor_node
linked_list.head.prev = cursor_node

text = list(sys.stdin.readline().strip())
for char in text:
    linked_list.insert_before(Node(char), cursor_node)

N = int(sys.stdin.readline().strip())
for _ in range(N):
    command = sys.stdin.readline().strip()
    if command[0] == "L" and cursor_node.prev.key is not None:
        linked_list.move_before(cursor_node, cursor_node.prev)
    elif command[0] == "D" and cursor_node.next.key is not None:
        linked_list.move_after(cursor_node, cursor_node.next)
    elif command[0] == "B" and cursor_node.prev.key is not None:
        linked_list.delete_node(cursor_node.prev)
    elif command[0] == "P":
        linked_list.insert_before(Node(command[2]), cursor_node)

linked_list.delete_node(cursor_node)
print(linked_list)