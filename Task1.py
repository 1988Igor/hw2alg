# Реализовать сортировку пузырьком для двухсвязного списка
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
    
    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
    
    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next


linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.add_node(5)

print("Original List: ", end='')
linked_list.print_list()

linked_list.reverse()

print("\nReversed List: ", end='')
linked_list.print_list()
