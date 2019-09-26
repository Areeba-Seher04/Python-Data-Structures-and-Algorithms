class Node:
    def __init__(self,data=0):
        
        self.key=data
        self.leftChild=None
        self.rightChild=None
        
    def __str__(self):
        
        return "{0}".format(self.key)

class Tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        
        self.newNode=Node(data)
        
        if self.root == None:
            self.root=self.newNode
            
        else:
            self.parent=self.root
            
            while(1):
                
                if data < self.parent.key:
                    
                    if self.parent.leftChild == None:
                        self.parent.leftChild=self.newNode
                        return
                    else:
                        self.parent=self.parent.leftChild
                        
                elif data >= self.parent.key:
                    
                    if self.parent.rightChild == None:
                        self.parent.rightChild=self.newNode
                        return
                    else:
                        self.parent=self.parent.rightChild

    def search(self,data):

        if self.root.key == data:
            return "Found At Root"

        else:
            self.parent=self.root
            level=1
            while(True):
                
                if data < self.parent.key:
                    
                    if self.parent.leftChild == None:
                        return "Not Found"
                    elif self.parent.leftChild.key == data:
                        return "Found On Left Side at level {0}".format(level)
                    else:
                        self.parent=self.parent.leftChild
                        level+=1
                        
                elif data >= self.parent.key:
                    
                    if self.parent.rightChild == None:
                        return "Not Found"
                    elif self.parent.rightChild.key == data:
                        return "Found On Right Side at level {0}".format(level)
                    else:
                        self.parent=self.parent.rightChild
                        level+=1

    def MinimumValue(self,node):
        self.current=node

        while(self.current.leftChild is not None):
            self.current=self.current.leftChild
        return self.current

    def Delete(self,root,data):
        
        if root is None:
            return root
        elif data < root.key:
            
            root.leftChild=self.Delete(root.leftChild,data)
        elif data > root.key:
            root.rightChild=self.Delete(root.rightChild,data)

        else:
            
            if root.leftChild is None:
                temp=root.rightChild
                root=None
                return temp
            
            elif root.rightChild is None:
                temp=root.leftChild
                root=None
                return temp
            
            temp=self.MinimumValue(root.rightChild)
            root.key=temp.key
            root.rightChild=self.Delete(root.rightChild,temp.key)
        return root

    def inorder(self,root):

        if root is not None:
            self.inorder(root.leftChild)
            print(root)
            self.inorder(root.rightChild)           


tree=Tree()
tree.insert(12)
tree.insert(13)
tree.insert(14)
tree.insert(10)
tree.insert(9)
tree.insert(11)
tree.insert(20)
tree.insert(15)
tree.root=tree.Delete(tree.root,15)
print("--")
tree.inorder(tree.root)

