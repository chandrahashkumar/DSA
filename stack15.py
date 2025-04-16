class Stack:
    def __init__(self):
        self.list = []
    def push(self,elem):
        self.list.append(elem)
    def pop(self):
        if len(self.list) == 0:
            return f"Stack is empty. Cannot pop."
        else:
            print(f"{self.list.pop()}")
    def peek(self):
        print(self.list[-1])
    def display(self):
        print(self.list)
    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

stack = Stack()
print(stack.pop())
# stack.push(10)
# stack.push(30)
# stack.push(40)
# stack.push(3)
# stack.push(-4)
# stack.display()