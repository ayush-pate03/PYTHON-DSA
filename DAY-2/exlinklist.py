# train coaches 
class   Coach:
    def __init__(self, data):
        self.data = data
        self.next = None
 # creates nodes 
coach1 = Coach("A")
coach2 = Coach("B")
coach3 = Coach("C")

#connect them
coach1.next = coach2
coach2.next = coach3

# checking 
current = coach1
while current :
    print(current.data)
    current = current.next


        