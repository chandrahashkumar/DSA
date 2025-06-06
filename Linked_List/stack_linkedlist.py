class Stack:
    def __init__(self,size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def push(self,data):
        if self.top == self.size -1:
            print("Stack is Full")
            return
        self.top +=1
        self.stack[self.top] = data
    def pop(self):
        if self.top == -1:
            print("Stack is Empty")
            return None
        value = self.stack[self.top]
        self.top -=1
        return value

    def peek(self):
        if self.top == -1:
            print('Stack is Empty')
            return None
        return self.stack[self.top]

    def stack_is_empty(self):
        return self.top == -1

    def display(self):
        if self.top == -1:
            print("Stack is Empty")
            return
        print(self.stack[:self.top+1])

s = Stack(20)
for i in range(6):
    s.push(i)

s.display()
print(s.peek())
print(s.pop())
print(s.peek())
s.push(9)
s.push(10)
s.push(77)
s.push(91)
s.display()
