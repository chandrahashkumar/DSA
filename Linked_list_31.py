class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

        # add node to the end of the linked list
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        # Prepend a new node to the beginning of the linked list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

       # Delete a node with a specific value from the linked list
    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next


    def display(self):
        current = self.head
        while current:
            print(current.data, end='→')
            current = current.next
        print("None")


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(10)
    ll.append(78)
    ll.append(23)
    ll.append(42)
    ll.display()
    ll.prepend(23)
    ll.display()
    ll.delete(78)
    ll.display()






