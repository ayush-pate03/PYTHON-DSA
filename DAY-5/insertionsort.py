mylist = [32, 56, 78, 65, 34, 23, 43, 12]
n = len(mylist)
for i in range(1, n):
    insert_index = i
    current_value = mylist.pop(i)

    for j in range(i-1, -1, -1):
            if mylist[j] > current_value:
                  insert_index = j


    mylist.insert(insert_index, current_value)
    print(mylist)