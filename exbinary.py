# Binary Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the Binary Tree
root = Node(10)

root.left = Node(5)
root.right = Node(20)

root.left.left = Node(3)
root.left.right = Node(7)

root.right.left = Node(15)
root.right.right = Node(25)

# Inorder Traversal (Left -> Root -> Right)
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)


# Preorder Traversal (Root -> Left -> Right)
def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)


# Postorder Traversal (Left -> Right -> Root)
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")


# Display Output
print("Binary Tree")

print("\nInorder Traversal:")
inorder(root)

print("\n\nPreorder Traversal:")
preorder(root)

print("\n\nPostorder Traversal:")
postorder(root)