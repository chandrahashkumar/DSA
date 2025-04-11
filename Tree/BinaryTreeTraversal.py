from collections import deque

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

        # Level order traversal
def level_order_travel(root):
    if not root:
        return
    queue = deque()
    queue.append(root)
    while queue:
        print(queue)
        current = queue.popleft()
        print(current.value, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        print(queue)
root = Node('N1')
root.left = Node("N2")
root.right = Node("N3")
root.right.left = Node("NA")


print("Pre order traversal")
preorder_travel(root)

print("\nPost order traversal")
postorder_travel(root)

print("\nIn order traversal")
inorder_travel(root)
print("\nLevel order traversal")
level_order_travel(root)

