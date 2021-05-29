import random
import sys
#Patrick James
#Binary Tree Data Structure Work
class Node:
    #typical definition of a node having a right and left node 
    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data
    def insertNode(self, newNodeData):
        #calls recursively if child is not none
        if self.data > newNodeData:
            if self.leftChild == None:
                self.leftChild = Node(newNodeData) 
            else:
                self.leftChild.insertNode(newNodeData)
        elif self.data < newNodeData:
            if self.rightChild == None:
                self.rightChild = Node(newNodeData)        
            else:
                self.rightChild.insertNode(newNodeData)
        else:
            print("Attempted to insert: ", newNodeData, ", yet this already exists.")

    def inOrderTraversal(self):
        if self.leftChild != None:
            self.leftChild.inOrderTraversal()
        print(self.data, end=' ')
        if self.rightChild != None:
            self.rightChild.inOrderTraversal()


    def fillTree(self, numNodes):
        for x in range(numNodes-1):
            #newData = random.randint(-sys.maxsize, sys.maxsize)
            #easier to check validity
            newData = random.randint(0, 1000)
            self.insertNode(newData)
       



        

root = Node(500)
root.fillTree(100)
root.inOrderTraversal()

