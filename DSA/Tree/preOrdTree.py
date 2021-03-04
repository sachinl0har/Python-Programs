# creating a node class
class Node:
    def __init__(self,val):
        self.leftchild = None
        self.rightchild = None
        self.nodedata = val

# creating an instance of the Node class to to construct the tree.
root = Node(1)
root.leftchild = Node(2)
root.rightchild = Node(3)
root.leftchild.leftchild = Node(4)
root.leftchild.rightchild = Node(5)

# PreOrder Function
def PreOrd(root):
    if root:
        print(root.nodedata)
        PreOrd(root.leftchild)
        PreOrd(root.rightchild)
PreOrd(root)