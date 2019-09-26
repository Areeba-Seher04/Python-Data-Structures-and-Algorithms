class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

        
class LinkedList:
    def __init__(self):
        self.head=None
        self.count=0
        self.maxSize=3
        
    def printList(self):
        if self.head is None:
            print("List is Empty")
            return
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    
        
    def push(self,data):
        if self.count>=self.maxSize:
            print("Stack full")
            return
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        print(self.head.data)
        self.count += 1
        

    def pop(self):
        if self.head==None:
            return("stack Empty!")
        previousHead=self.head
        self.head=self.head.next
        previousHead.next=None
        print(previousHead.data)
        self.count -= 1
        
    def size(self):
        print(self.count)
    
    def delete(self):
        self.head=None
        self.top=0

    def isEmpty(self):
        if self.head==None:
            print("True")
        else:
            print("False")

    
    def peek(self):
        if self.head==None:
            return("Empty no peek value")
        print(self.head.data)

    def isFull(self):
        if self.count==self.maxSize:
            print("True")
        else:
            print("False")
        
llist=LinkedList()
llist.push("Areeb")
llist.push("Saad")
llist.push("asad")
llist.isFull()
llist.push("Muneeb")
llist.pop()
print("_____")
llist.printList()
llist.isEmpty()
llist.size()
