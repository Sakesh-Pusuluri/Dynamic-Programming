"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def findParent(self,node):
        while(node.parent is not None):
            node = node.parent
        return node   
        
    def lowestCommonAncestor2(self, p: 'Node', q: 'Node') -> 'Node':
        root = self.findParent(p)
        parent=[root]
        ancestors=set()
        d={root:None}
        while(p not in d and q not in d):
            ele = parent.pop()
            if(ele.left):
                parent.append(ele.left)
                d[ele.left] = ele
            if(ele.right):
                parent.append(ele.right)
                d[ele.right] = ele
        while p:
            ancestors.add(p)
            p = p.parent
        while q not in ancestors:
            q = q.parent
        return q
        
            
            
        
        
