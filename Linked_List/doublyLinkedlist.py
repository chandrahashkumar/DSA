class Node:
    def __init__(self,prev = None, data = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_ll:
    def __init__(self):
        self.head = None

    def add_at_beginning(self,data):
        new_node = Node(None, data,self.head)
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def add_at_end(self,data):
        if self.head is None:
            self.head = Node(None,data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(itr,data,None)

    def print_list(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        while itr:
            print(itr.data,end='<-->')
            itr = itr.next
        print("None")


dll = Doubly_ll()
# dll.add_at_end(100)
# dll.add_at_beginning(10)
# dll.add_at_beginning(10)
# dll.add_at_beginning(20)
# dll.add_at_beginning(30)
# dll.add_at_end(100)
# dll.add_at_end(200)
# dll.add_at_end(300)
# dll.print_list()



dll.add_at_beginning(5)
dll.add_at_beginning(6)
dll.add_at_end(60)
dll.add_at_beginning(10)
dll.print_list()