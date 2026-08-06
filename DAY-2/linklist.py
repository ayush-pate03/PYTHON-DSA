class Node:
    def __init__(self, data):
        self.data = data # value
        self.next = None # link to the next node

# creates 3 nodes 
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# connect them 
node1.next = node2
node2.next = node3

# visit every node 
current = node1

while current is not None:
    print(current.data)
    current = current.next
        