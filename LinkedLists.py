class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, newData):
        if self.next is not None:
            self.next.append(newData)
        else:
            self.next = Node(newData)

    def print(self):
        if self.next is None:
            print(self.data, end =" ")
            return
        else:
            print(self.data, end =" ")
            self.next.print()

    def printLast(self):
        if self.next is None:
            print("\n Last node data: ", self.data)
            return
        else:
            self.next.printLast()


list = Node(0)
list.append(1)
list.append(2)
list.append(3)
list.print()
list.printLast()
