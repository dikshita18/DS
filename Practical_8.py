#Program for preorder, inorder and postorder traversal of tree
class Node :
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self,data):
       if self.val:
           if data < self.val:
               if self.left is None:
                   self.left = Node(data)
               else:
                    self.left.insert(data)
           elif data>self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
       else :
            self.val = data

    def PrintTree(self):
        if  self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()


    def printPreorder(self):
        if self.val:
            print(self.val)
            if self.left:
                self.left.printPreorder()
            if self.right:
                self.right.printPreorder()
                    
    def  printInorder(self):
        if self.val :
            if self.left:
                self.left.printInorder()
            print(self.val)
            if self.right:
                self.right.printInorder()

    def printPostorder(self):
        if self.val:
            if self.left:
                self.left.printPostorder()
            if self.right:
                self.right.printPostorder()
            print(self.val)

            
root1 = Node(None)
root1.insert(60)
root1.insert(1)
root1.insert(4)
root1.insert(12)
root1.insert(100)
root1.insert(90)

print("Node: ")
root1.PrintTree()

print("Preorder: ")
root1.printPreorder()

print("Inorder: ")
root1.printInorder()

print("Postorder: ")
root1.printPostorder()
