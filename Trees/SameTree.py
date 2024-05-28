from typing import Optional
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not q and not p:
                return True
            
            if not p or not q:
                return False
            
            pQueue = Queue()
            qQueue = Queue()
            
            pQueue.put(p)
            qQueue.put(q)
            
            while not pQueue.empty() and qQueue.empty():
                pNode = pQueue.get()
                qNode = qQueue.get()
                
                if not pNode and not qNode:
                    continue
                
                if not pNode or not qNode:
                    return False
                
                if pNode.val != qNode.val:
                    return False
                
                pNode.put(pNode.left())
                pNode.put(pNode.right())
                qNode.put(pNode.left())
                qNode.put(pNode.right())
                
            return pNode.empty() and qNode.empty()
        
        #this will also work
        #  if not q and not p:
        #     return True
        
        # if not p or not q or p.val != q.val:
        #     return False
        
        # return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
            