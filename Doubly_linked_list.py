class Node:
    def __init__(self, prev = None, data = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev
class DoublyLinkList:
    def __init__(self):
        self.head = None
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        itr = self.head
        listr = " "
        while itr:
            listr += str(itr.data)+"<--->" if itr.next else str(itr.data)
            itr = itr.next
        print(listr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        node = Node(None, data, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        


dll = DoublyLinkList()
dll.insert_at_begining(5)
dll.insert_at_begining(89)
dll.insert_at_begining(78)
dll.insert_at_begining(56)
dll.get_length()
dll.print_list()