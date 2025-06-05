class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head =None

    def add_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self,node):
        if not node or not node.next:
            return node
        new_node = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return new_node

    def reverse_list(self):
        self.head = self.reverse(self.head)

    def print_list(self):
        if self.head is None:
            print("List is Empty")
            return
        itr = self.head
        while itr:
            print(itr.data, end='-->')
            itr = itr.next
        print("None")
    def add_values(self,lis):
        for data in lis:
            self.add_at_beginning(data)
ll = linkedlist()
ll.add_values([4,5,6,95,9889,82,8,78])
ll.print_list()
ll.reverse_list()
ll.print_list()