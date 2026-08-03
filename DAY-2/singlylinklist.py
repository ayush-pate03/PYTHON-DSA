class Node :
    def __init__(self, data):
        self.data = data
        self.next =None

# create 
node1 = Node(11)
node2 = Node(12)
node3 = Node(13)

# connect
node1.next = node2
node2.next = node3

# visit every node
current = node1

while current is not None :
    print(current.data)
    current = current.next
        