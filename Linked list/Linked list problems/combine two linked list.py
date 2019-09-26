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
    def combine(self,head_2):
        if self.head == None:
            self.head=head_2
            return
        temp=self.head
        while temp.next != None:
            temp=temp.next
        temp.next=head_2
        return
    def display_list(self):
        self.show=self.head
        if self.head is None:
            print("The list is Empty")
        else:
            while self.show != None:
                print(self.show.data)
                self.show=self.show.next
l1=Linked_list()

l1.push(4)
l1.push(5)
l1.push(6)
l1.push(4)
print("The first list")
l1.display_list()
l2=Linked_list()
l2.push(15)
l2.push(2)
l2.push(4)
l2.push(11)
l2.combine(l1.head)
print("\n\nthe combined list")
l2.display_list()
