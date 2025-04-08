class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def preorder_travel(root):
    if root:
        print(root.data, end=" ")
        preorder_travel(root.left)
        preorder_travel(root.right)
def inorder_travel(root):
    if root:


root = Node(10)
root.left = Node(30)
root.right = Node(4)
root.left.left = Node(20)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right =Node(3)
root.left.left.left.left = Node(1)

