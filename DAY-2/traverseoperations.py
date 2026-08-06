class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Traverse
current = node1

while current is not None:
    print(current.data)
    current = current.next