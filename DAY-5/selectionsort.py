mylist = [66, 75, 32, 99, 11]
n = len(mylist)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if mylist[j]< mylist[min_index]:
            min_index = j
    min_value = mylist.pop(min_index)
    mylist.insert(i, min_value)

print(mylist)