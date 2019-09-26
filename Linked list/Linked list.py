#Linked list in Python
from os import system
import time
import sys
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
    def append(self,item):
        self.new_node=Node(item)
        self.last=self.head
        if self.head is None:
            self.new_node.next=None
            self.head=self.new_node
        else:
            while self.last.next is not None:
                self.last=self.last.next
            self.new_node.next=self.last.next
            self.last.next=self.new_node
    def insert(self,item,pos):
        self.new_node=Node(item)
        self.target=self.head
        self.count=0
        while self.target is not None:
            self.target=self.target.next
            self.count+=1
        if pos > self.count:
            print("Position out of range")
            return False
        self.target=self.head
        if pos is 0:
            self.new_node.next=self.head
            self.head=self.new_node
            return True
        for self.i in range(0,pos-1):
            self.target=self.target.next
        self.new_node.next=self.target.next
        self.target.next=self.new_node
        return True
    def isempty(self):
        if self.head is None:
            return True
        else:
            return False
    def pop(self):
        if self.isempty():
            print("The list is Empty")
            return False
        self.last=self.head
        self.temp=Node()
        while self.last.next is not None:
            self.temp=self.last
            self.last=self.last.next
        self.last=None
        self.temp.next=None
        return True
    def delete(self,item):
        if self.isempty():
            print("The list is Empty")
            return False
        self.target=self.head
        self.temp=Node()
        self.temp1=Node()
        if self.head.data is item:
            self.target=self.head.next
            self.head=None
            self.head=self.target
            return True
        self.pos=0
        self.target=self.head
        while self.target is not None:
            if self.target.data is item:
                break
            else:
                self.pos+=1
                self.target=self.target.next
        if self.pos >= self.sizeof():
            print("The item ",item," is not in the list")
            return False
        self.target=self.head
        for self.i in range(0,self.pos-1):
            self.target=self.target.next
            self.temp=self.target.next
        self.temp1=self.temp.next
        self.target.next=self.temp1
        self.temp=None
        return True
    def display_list(self):
        self.show=self.head
        if self.head is None:
            print("The list is Empty")
        else:
            while self.show != None:
                print(self.show.data)
                self.show=self.show.next
def linklist():
    list1=Linked_list()
    check = 'y'
    while check is 'y':
        system("cls")
        print("\t\tWelcome to the Manhus universe of Linked list\n\n")
        print("Addition Functions --->>> \t 1)Push\t2)Append\t3)Insert")
        print("Deletion Functions --->>> \t 4)Pop\t5)Delete Any Element")
        print("Press 'd' to display list\nPress 'e' to exit")
        op=input("Enter the Operation you want to apply in Linked List: ")
        if op == '1':
            system("cls")
            element=int(input("Enter the element to add: "))
            list1.push(element)
            print("Element ",element," added successfully")
            time.sleep(1)
        elif op == '2':
            system("cls")
            element=int(input("Enter the element to add: "))
            list1.append(element)
            print("Element ",element," added successfully")
            time.sleep(1)
        elif op == '3':
            system("cls")
            element=int(input("Enter the element to add: "))
            pos=int(input("Enter the position: "))
            if list1.insert(element,pos) is True:
                print("Element ",element," added successfully")
            time.sleep(1)
        elif op == '4':
            system("cls")
            if list1.pop() is True:
                print("Element deleted successfully")
            time.sleep(1)
        elif op == '5':
            system("cls")
            element=int(input("Enter the element to delete: "))
            if list1.delete(element) is True:
                print("Element deleted successfully")
            time.sleep(1)
        elif op == 'd':
            system("cls")
            list1.display_list()
            time.sleep(1)
        elif op == 'e':
            system("cls")
            print("Exiting the system")
            time.sleep(1)
            print("\t\tThanks For Your Kind Cooperation")
            system("pause")
            sys.exit(0)
        else:
            system("cls")
            print("Invalid Operation gadhy")
if __name__=="__main__":
    linklist()
