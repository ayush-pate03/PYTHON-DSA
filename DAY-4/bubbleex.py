list = [32, 65, 78, 11, 2, 987, 543]
n = len(list)
for i in range (n-1):
    for j in range(n-i-1):
       if list[j] > list[j+1]:
        list[j], list[j+1] = list[j+1], list[j]
print(list)