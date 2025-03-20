class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def reverse_recursive(self, node):
        # Base case: if node is empty or it's the last node
        if not node or not node.next:
            return node
        # Recursively reverse the rest of the list
        new_head = self.reverse_recursive(node.next)
        # Adjust pointers
        node.next.next = node
        node.next = None
        return new_head

    def reverse(self):
        self.head = self.reverse_recursive(self.head)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage:
ll = LinkedList()
for i in [1, 2, 3, 4]:
    ll.append(i)

print("Original Linked List:")
ll.print_list()

ll.reverse()
print("Reversed Linked List:")
ll.print_list()
