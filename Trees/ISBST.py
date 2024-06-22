class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
    def checkBST(root):
        return True
    
    
a = Node(4)
a.left = Node(2)
a.right = Node(6)
a.left.left = Node(1)
a.left.right = Node(3)
a.right.left = Node(5)
a.right.right = Node(7)

print(a)
