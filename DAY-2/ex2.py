class Node :
    def __init__(self, data):
        self.prev = None
        self.data = data 
        self.next = None

def lowest(head):
    minValue = head.data

    current = head 

    while current :
        if current.data < minValue:
            minValue = current.data

        current = current.next

    return minValue
# creates nodes
node1 = Node(1)
node2 = Node(23)
node3 = Node(45)
node4 = Node(67)
node5 = Node(54)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.prev = node1

print('lowestvalue:',lowest(node1))