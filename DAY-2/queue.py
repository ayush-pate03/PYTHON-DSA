queue = []
# enqueue add
queue.append('a')
queue.append('b')
queue.append('c')
print('Queue:', queue)

# peek
peekelement = queue[0]
print('peekelement:', queue)

# dequeue removes
popelement = queue.pop(0)
print('popelement:', queue)

print('quese after dequeue:', queue)

# is empty
isEmpty = not bool(queue)
print('isempty:', isEmpty)

# size
print('size :', queue)