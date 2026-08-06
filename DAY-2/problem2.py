class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


def reverse_linked_list(head):
  prev = None
  current = head

  while current is not None:
    next_node = current.next  # Step 1: Store the next node safely
    current.next = prev  # Step 2: Reverse the pointer backward
    prev = current  # Step 3: Move 'prev' and 'current' one step forward
    current = next_node

  # 'prev' will be the new head of the reversed linked list
  return prev


# Helper function to print the linked list
def print_list(head):
  current = head
  elements = []
  while current:
    elements.append(str(current.data))
    current = current.next
  print(" -> ".join(elements) + " -> None")


# --- Testing ---
# Create nodes: 1 -> 2 -> 3 -> 4 -> None
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original Linked List:")
print_list(node1)

# Reverse the linked list
new_head = reverse_linked_list(node1)

print("Reversed Linked List:")
print_list(new_head)