class node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right           
A=node(5)
B=node(6)
C=node(7)
A.left=B
A.right=C
D=node(8)
E=node(9)
F=node(10)
G=node(11)
B.left=D
B.right=E
C.left=F
C.right=G
def inorder(node):
    if node==None:
        return
    else:
        inorder(node.left)
        print(node.val)
        inorder(node.right)
def preorder(node):
    if node==None:
        return
    else:
        print(node.val)
        preorder(node.left)
        preorder(node.right)
def postorder(node):
    if node==None:
        return
    else:
        postorder(node.left)
        postorder(node.right)
        print(node.val)
print("inorder is:")
inorder(A)
print("preorder is:")
preorder(A)
print("postorder is:")
postorder(A)
    
    
    
    
    
    
    



