class Node :
    def __init__(self, data):
        self.data= data
        self.next = None

def lowestvalue(head):
    #assume first node has small value
    minValue = head.data

    # start from the first node
    current = head

    while current :
        if current.data < minValue:
            minValue = current.data

        current = current.next

    return minValue

# createes nodes 
node1 = Node(11)
node2 = Node(34)
node3 = Node(22)
node4 = Node(13)        
node5 = Node(66)

# connecct nodes 
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print('lowestvalue:', lowestvalue(node1))