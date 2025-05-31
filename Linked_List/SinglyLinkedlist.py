class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singly_linkedlist:
    def __init__(self):
        self.head = None

    def add_at_head(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_tail(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        current = self.head
        while current.next:
            current =current.next
        current.next = new_node

    def delete_node(self,data):
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
            print(current.data,end="-->")
            current = current.next
        print("None")

    def add_nodes(self,datas):
        for data in datas:
            self.add_at_head(data)

if __name__=="__main__":
    sll = singly_linkedlist()
    sll.add_at_head(10)
    sll.add_at_head(20)
    sll.add_at_tail(200)
    sll.add_at_head(30)
    sll.add_at_head(40)
    sll.add_at_tail(100)
    sll.add_at_tail(300)
    sll.add_at_tail(400)
    sll.add_nodes([1000,2000,3000])
    sll.display() #3000-->2000-->1000-->40-->30-->20-->10-->200-->100-->300-->400-->None