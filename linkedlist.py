#Node class
class Node:
    #function to initialize the node object
    def __init__(self, data):
        self.data = data #assign the data
        self.next = None #initialize the next as null

#linked list class
class LinkedList:
    #function to intiliaze the Linked  List Object
    def __init__(self):
        self.head = None
