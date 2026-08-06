stack = []
# push 
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
print('stack:', stack)

# peek
peekelement = stack[-1] # view of element 
print('peekelement:', stack)

# pop
popelement = stack.pop()# Removes and returns the top element from the stack.
print('popelement:', stack)

# stack after this operation
print('after this operation:', stack)
