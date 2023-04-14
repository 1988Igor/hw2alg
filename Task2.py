# Реализовать сортировку пузырьком для двухсвязного списка
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            new_node.prev = last_node
    
    def bubble_sort(self):
        if self.head is None:
            return
        
        end_node = None
        while end_node != self.head:
            curr_node = self.head
            while curr_node.next != end_node:
                next_node = curr_node.next
                if curr_node.data > next_node.data:
                    # swap nodes
                    prev_node = curr_node.prev
                    if prev_node:
                        prev_node.next = next_node
                    else:
                        self.head = next_node
                    next_node.prev = prev_node
                    curr_node.next = next_node.next
                    if next_node.next:
                        next_node.next.prev = curr_node
                    next_node.next = curr_node
                    curr_node.prev = next_node
                
                else:
                    curr_node = curr_node.next
            end_node = curr_node
    
    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next

# Пример использования
linked_list = DoublyLinkedList()
linked_list.add_node(4)
linked_list.add_node(2)
linked_list.add_node(5)
linked_list.add_node(1)
linked_list.add_node(3)

print("Initial list: ", end='')
linked_list.print_list()

linked_list.bubble_sort()

print("\nSorted list: ", end='')
linked_list.print_list()
