class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None
    def sizeof(self):
        self.count=0
        self.last=self.head
        while self.last is not None:
            self.count+=1
            self.last=self.last.next
        return self.count
    def push(self,item):
        self.new_node=Node(item)
        if self.head is None:
            self.new_node.next=None
            self.head=self.new_node
        else:
            self.new_node.next=self.head
            self.head=self.new_node
    def break_into(self,negative_list):
        if self.head is None:
            print("The list is Empty")
            return
        self.show=self.head
        while self.show != None:
            if self.show.data < 0:
                negative_list.head=self.show.next
                self.show.next=None
                return
            self.show=self.show.next
            
    def display_list(self):
        self.show=self.head
        if self.head is None:
            print("The list is Empty")
        else:
            while self.show != None:
                print(self.show.data)
                self.show=self.show.next
l1=Linked_list()
l1.push(-4)
l1.push(-5)
l1.push(-6)
l1.push(4)
l1.push(12)
l1.push(15)
l1.push(17)
l1.push(20)
print("The general list")
l1.display_list()
negative_list=Linked_list()
l1.break_into(negative_list)
print("\\n The Furst list")
l1.display_list()
print("\n\nthe negative list")
negative_list.display_list()
