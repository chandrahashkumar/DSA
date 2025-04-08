class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,node):
        node.next = self.head
        self.head = node

n = Node(10)
l = LinkedList()
l.insert_at_beginning(n)
