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

    def inorder(self,root):

        if root is not None:
            self.inorder(root.leftChild)
            print(root)
            self.inorder(root.rightChild)

    def preOrder(self,root):
        if root is not None:
            print(root)
            self.preOrder(root.leftChild)
            self.preOrder(root.rightChild)

    def postOrder(self,root):
        if root is not None:
            self.postOrder(root.leftChild)
            self.postOrder(root.rightChild)
            print(root)


    def displayTree(self):
        
        print(self.root,self.root.leftChild)
        
tree=Tree()
tree.insert(12)
tree.insert(13)
tree.insert(14)
tree.insert(10)
tree.insert(8)
tree.insert(11)
#print(tree.root)
print("Inorder Traversal")
tree.inorder(tree.root)
print("PreOrder Traversal")
tree.preOrder(tree.root)
print("PostOrder Traversal")
tree.postOrder(tree.root)

