class Treenode :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Treenode('R')
nodeA = Treenode('A')
nodeB = Treenode('B')        
nodeC = Treenode('C')
nodeD = Treenode('D')
nodeE = Treenode('E')
nodeF = Treenode('F')
nodeG = Treenode('G')

root.left = nodeA 
root.right = nodeB
nodeA.left = nodeC
nodeB.right = nodeF
nodeA.right = nodeD
nodeB.left = nodeE
nodeF.left = nodeG

#    test
print("root.right.left.data:", root.right.left.data)