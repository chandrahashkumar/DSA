# num = int(input("Enter a number: "))
# rem , rev = 0, 1
# for i in range(num):
#     rem = num % 10
#     rev = rev * 10 + rem
#     num /=10
# print(rev)

# for n in range(11, 100):
#     if n >50:
#         break
#     tens = n // 10
#     units = n % 10
#     if tens + units == 5:
#         print(n)


#
# for n in range(11, 999):
#     if n < 100:
#         tens = n // 10
#         units = n % 10
#         digit_sum = tens + units
#     else:
#         hundreds = n // 100
#         tens = (n // 10) % 10
#         units = n % 10
#         digit_sum = hundreds + tens + units
#     if digit_sum == 5:
#         print(n)

# num = int(input("Enter a number: "))
# k = 1
# fact = 0
# for i in range(num+1):
#     if i % k == 0:
#         fact +=1
#
# if fact == 2:
#     print("prime")


# class Stack:
#     def __init__(self,size):
#         self.stack = [None] * size
#         self.top = -1
#         self.size = size
#     def push(self,data):
#         if self.top == self.size -1:
#             print("Stack is Full")
#             return
#         self.top += 1
#         self.stack[self.top] = data
#     def pop(self):
#         if self.top == - 1:
#             print("Stack is Empty")
#             return None
#         value = self.stack[self.top]
#         self.top -= 1
#         return value
#     def peek(self):
#         if self.top == -1:
#             print("Stack is Empty")
#             return None
#         return self.stack[self.top]
#     def stack_empty(self):
#         return self.top == -1
#     def display(self):
#         if self.top == -1:
#             print("Stack is Empty")
#             return
#         print(self.stack[:self.top+1])
#
#
#
# stack = Stack(5)
# stack.push(4)
# stack.push(5)
# stack.push(5)
# stack.push(6)
# stack.push(3)
# print(f"Popped: {stack.pop()}")
# print(f"Peed: {stack.peek()}")
# stack.display()
# print(stack.stack_empty())

# class car:
#     def __init__(self, carNumber):
#         self.carNumber = -1
#         self.carnumber = carNumber
#     def add(self):
#         self.carNumber += 1
#         print(self.carNumber)
#     def remove_l(self):
#         # self.carNumber -= 1
#         print("==============")
#         print(self.carNumber)
#
#
# c = car(5)
# c.add()
# c.add()
# c.add()
# c.remove_l()
# # c.add()
#
# queue = []
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# print(queue.pop(0))
# print(queue)


class Queue:
    def __init__(self,size):
        self.queue = [None] * size
        self.front = self.rear = -1
        self.size = size
    def enqueue(self,data):
        if self.rear == self.size - 1:
            print("Queue is overflow")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = data
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
            return None
        data = self.queue[self.front]
        self.front += 1
        return data
    def peek(self):
        if  self.front == -1 or self.front > self.rear:
            print("Queue is empty")
            return None
        return self.queue[self.front]
    def queue_empty(self):
        return self.front == -1 or self.front > self.rear
    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is Empty")
            return
        print(self.queue[self.front:self.rear + 1])






queue = Queue(4)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.display()
print(queue.dequeue())
print(queue.peek())
print(queue.queue_empty())
queue.display()