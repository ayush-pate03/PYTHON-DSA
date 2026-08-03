class Player :
    def __init__(self, name):
        self.name = name 
        self.next = None

#create 
p1 = Player("Amit")
p2 = Player("anuj")
p3 = Player("priya")
p4 = Player("vedant")

#connect 
p1.next = p2
p2.next = p3
p3.next = p4

# make it circular
p4.next = p1

# visit 
current = p1

while current is not None :
    print(current.name)
    current = current.next

    if current == p1 :
        break
       