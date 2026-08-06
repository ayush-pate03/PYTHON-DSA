class node :
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

# create
node1 = node(10)
node2 = node(20)
node3 = node(30)

#connect 
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

# visit every node
current = node1

while current is not None:
    print(current.data)
    current = current.next
    # example google youtube github
    