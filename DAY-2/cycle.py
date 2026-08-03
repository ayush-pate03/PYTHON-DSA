class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

  def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

      if slow == fast:
        return True

    # Moved outside the while loop!
    return False


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

# Test 1: Let's test it BEFORE adding the cycle
print("Test 1 (No Cycle):", Node.has_cycle(node1))

# Now add the cycle
node4.next = node2

# Test 2: Test AFTER adding the cycle
print("Test 2 (With Cycle):", Node.has_cycle(node1))