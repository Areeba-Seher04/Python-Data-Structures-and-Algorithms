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
    def del_x(self,x):
        if self.head == None:
            return
        self.sh=self.head
        temp=Node()
        while self.sh != None:
            if self.head.data == x:
                self.head=self.head.next
                self.sh=self.head
            elif self.sh.data == x:
                temp.next=self.sh.next
                self.sh=temp.next
            else:
                temp=self.sh
                self.sh=self.sh.next


    def display_list(self):
        self.show=self.head
        if self.head is None:
            print("The list is Empty")
        else:
            while self.show != None:
                print(self.show.data)
                self.show=self.show.next
lk=Linked_list()

lk.push(4)
lk.push(5)
lk.push(6)
lk.push(4)
lk.push(2)
lk.push(4)
lk.display_list()
lk.del_x(4)
lk.push(11)
print("now display")
lk.display_list()
