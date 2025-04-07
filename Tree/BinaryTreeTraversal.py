class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

        # Pre order traversal
def preorder_travel(root):
    if root:
        print(root.value, end=" ")
        preorder_travel(root.left)
        preorder_travel(root.right)

        #Post order traversal
def postorder_travel(root):
    if root:
        postorder_travel(root.left)
        postorder_travel(root.right)
        print(root.value, end=" ")

        #In order traversal
def inorder_travel(root):
    if root:
        inorder_travel(root.left)
        print(root.value, end=" ")
        inorder_travel(root.right)



root = Node(5)
root.left = Node(4)
root.right = Node(9)
root.left.left = Node(7)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(11)

print("Pre order traversal")
preorder_travel(root)

print("\nPost order traversal")
postorder_travel(root)

print("\nIn order traversal")
inorder_travel(root)