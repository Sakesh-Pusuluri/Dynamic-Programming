# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def lowestCommonAncestorIterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return 
        parent=[root]
        ancestors=set()
        d={root:None}
        while (p not in d or q not in d):
            ele = parent.pop()
            if(ele.left):
                parent.append(ele.left)
                d[ele.left]=ele
            if(ele.right):
                parent.append(ele.right)
                d[ele.right]=ele
        while p:
            ancestors.add(p)
            p=d[p]
        while q not in ancestors:
            q=d[q]
        return q
            
        
                
        
