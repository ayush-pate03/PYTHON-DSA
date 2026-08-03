class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create nodes
node1 = Node(54)
node2 = Node(32)
node3 = Node(8)
node4 = Node(31)
node5 = Node(6)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


print("Before insertion:")
traverse(node1)


# Insert new node at beginning
newNode = Node(100)

newNode.next = node1
node1 = newNode


print("After insertion:")
traverse(node1)