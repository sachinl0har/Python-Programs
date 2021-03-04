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

# InOrder Function
def InOrd(root):
    if root:
        InOrd(root.leftchild)
        print(root.nodedata)
        InOrd(root.rightchild)
InOrd(root)