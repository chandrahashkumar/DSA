class Node:
    def __init__(self,key):
        self.left= None
        self.right = None
        self.val = key

def search(root,key):
    if root is None or root.val ==key:
        return root
    if key < root.val:
        return search(root.left,key)
    return search(root.right,key)

def insert(root,key):
    if root is None:
        return Node(key)
    if  key < root.val:
        root.left =insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root,key):
    if root is Node:
        return root
    if key < root.val:
        root.left = delete(root.left,key)
    elif key> root.val:
        root.right = delete(root.right,key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        root.val = minValueNode(root.right).val
        root.right = delete(root.right,root.val)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Create a BST
root = Node(50)
root = insert(root,30)
root = insert(root,10)
root = insert(root,50)
root = insert(root,20)
root = insert(root,60)

# In-order traversal to display the tree
print("Inorder traversal:")
inorder_traversal(root)
print("\n")

# Search for a value in the tree
search_key = 60
result = search(root, search_key)
if result:
    print(f"Element {search_key} found in the tree.")
else:
    print(f"Element {search_key} not found in the tree.")

# Delete a node from the tree
delete_key = 30
root = delete(root,delete_key)

# Inorder traversal after deletion
print("Inorder traversal after deleting 30.")
inorder_traversal(root)
