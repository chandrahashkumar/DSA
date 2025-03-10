class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        itr = self.head
        list = ''
        while itr:
            list += str(itr.data) + '--->' if itr.next else str(itr.data)
            itr = itr.next
        print(list)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count  = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


# list_l = LinkedList()
# list_l.insert_at_beginning(5)
# list_l.insert_at_beginning(10)
# list_l.insert_at_end(11)
# list_l.insert_at(2,3)
# list_l.remove_at()
# list_l.print_list()
# print(dir(Node))


print(dir(LinkedList))




# ll = LinkedList()
# ll.insert_at_begining(10)
# ll.insert_at_begining(50)
# ll.insert_at(1, 30)
# ll.insert_at_end(100)
# ll.print_list()

# ll.insert_values([4,6,8,9,1,5])
# ll.insert_at(3, 10)
# ll.remove_at(4)
# ll.print_list()


# ll.insert_values(['banana','mango','grapes','orange'])
# ll.insert_at(2, 'apple')
# ll.remove_at(4)
# ll.print_list()


        