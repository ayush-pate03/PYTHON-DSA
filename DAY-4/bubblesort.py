mylist = [34, 56, 65, 77, 21, 98, 66]
n = len(mylist)
for i in range (n-1):
    for j in range(n-i-1):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
print(mylist)