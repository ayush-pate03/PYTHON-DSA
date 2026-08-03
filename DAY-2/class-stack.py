class stack:

  def __init__(self):
    self.stack = []

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    if not self.isEmpty():
      return self.stack.pop()
    return "Stack is empty"

  def peek(self):
    if not self.isEmpty():
      return self.stack[-1]
    return "Stack is empty"

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)


# Your existing test code
mystack = stack()

mystack.push("a")
mystack.push("b")
mystack.push("c")

print("Stack: ", mystack.stack)
print("Pop: ", mystack.pop())
print("Stack after Pop: ", mystack.stack)
print("Peek: ", mystack.peek())
print("isEmpty: ", mystack.isEmpty())
print("Size: ", mystack.size())