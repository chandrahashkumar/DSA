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