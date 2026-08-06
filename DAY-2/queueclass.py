
class Queue:

  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    if not self.isEmpty():
      return self.queue.pop(0)
    return "Queue is empty"

  def peek(self):
    if not self.isEmpty():
      return self.queue[0]
    return "Queue is empty"

  def isEmpty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)


# Initialize the queue and add some items for testing
myQueue = Queue()
myQueue.enqueue("a")
myQueue.enqueue("b")
myQueue.enqueue("c")

# Your print statements
print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())