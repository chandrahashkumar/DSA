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
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(itr, data, None)
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(itr, data, itr.next)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1



dll = DoublyLinkList()
dll.insert_at_begining(5)
dll.insert_at_begining(89)
dll.insert_at_begining(78)
dll.insert_at_begining(56)
dll.insert_at_end(100)
dll.insert_at(2, 45)
dll.get_length()
dll.print_list()