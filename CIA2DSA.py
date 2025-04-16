# # stack implementation using list

# stack = []
# stack.append(5)
# stack.append(6)
# stack.append(9)
# stack.append(0)
# print(stack)
# print(stack.pop())
# print(stack)

# # Queue implementation using deque

# from collections import deque
# queue = deque()
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.append(40)
# print(queue)
# print(queue.popleft())
# print(queue.popleft())
# print(queue)

# Linked list implementation
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def insert_at_beginning(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def remove(self,data):
#         if not self.head:
#             print("LinkedList is empty")
#             return
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#         current = self.head
#         while current.next:
#             if current.next.data == data:
#                 current.next = current.next.next
#                 return
#             current = current.next
#
#     def print_list(self):
#         itr = self.head
#         while itr:
#             print(itr.data,end="→")
#             itr = itr.next
#         print("None")
#
#
# ll = LinkedList()
# ll.insert_at_beginning(10)
# ll.insert_at_beginning(20)
# ll.insert_at_beginning(30)
# ll.insert_at_beginning(40)
# ll.print_list()
# ll.remove(10)
# ll.print_list()

#
# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self,data):
#         self.stack.append(data)
#     def pop(self):
#         print(self.stack.pop())
#     def peek(self):
#        print(self.stack[-1])
#     def print_stack(self):
#         print(self.stack)
#
# s = Stack()
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.push(6)
# s.print_stack()
# s.pop()
# s.print_stack()
from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        print(self.queue.popleft())

    def display(self):
        print(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.dequeue()
q.display()