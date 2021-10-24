class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

import queue
def takeinput():
    q=queue.Queue()
    print("ENTER THE VALUE OF ROOT : ")
    rootdata=int(input())
    if rootdata==-1:
        return None
    root=BinaryTree(rootdata)
    q.put(root)
    while (not(q.empty())):
        curr=q.get()
        print("ENTER THE VALUE OF LEFTCHILD OF",curr.data,": ")
        leftdata=int(input())
        if leftdata!=-1:
            leftchild=BinaryTree(leftdata)
            curr.left=leftchild
            q.put(leftchild)
        print("ENTER THE VALUE OF RIGHTCHILD OF",curr.data,": ")
        rightdata=int(input())
        if rightdata!=-1:
            rightchild=BinaryTree(rightdata)
            curr.right=rightchild
            q.put(rightchild)        
    return root
            
def printTree(root):
    if root==None:
        return
    inputq=queue.Queue()
    outputq=queue.Queue()
    inputq.put(root)
    while (not(inputq.empty())):
        while (not(inputq.empty())):
            curr=inputq.get()
            print(curr.data,end=" ")
            if curr.left!=None:
                outputq.put(curr.left)
            if curr.right!=None:
                outputq.put(curr.right)
        print()
        inputq,outputq=outputq,inputq
        
def targetpath(root,t,k):
    if root==None:
        return -1
    
    if root.data==t:
        kdepthnode(root,k)
        return 0
    
    leftd=targetpath(root.left,t,k)
    if leftd!=-1:
        if leftd+1==k:
            print(root.data)
        else:
            kdepthnode(root.right,k-leftd-2)
        return 1+leftd

    rightd=targetpath(root.right,t,k)
    if rightd!=-1:
        if rightd+1==k:
            print(root.data)
        else:
            kdepthnode(root.left,k-rightd-2)
        return 1+rightd
    
    return -1

def kdepthnode(root,k):
    if root==None or k<0:
        return
    if k==0:
        print(root.data,end=" ")
        return
    kdepthnode(root.left,k-1)
    kdepthnode(root.right,k-1)

root=takeinput()
print("BINARY TREE IS :")
printTree(root)
t=int(input("ENTER THE VALUE OF THE TARGET NODE : "))
k=int(input("ENTER THE VALUE OF K : "))
print("ALL NODES WHICH ARE AT",k,"DISTANCE FROM THE",t,"ARE :",end=" ")
targetpath(root,t,k)