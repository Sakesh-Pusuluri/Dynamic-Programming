# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 
        q = queue.Queue()
        q.put(root)
        while(q.qsize()>0):
            _count = q.qsize()
            _sum=0
            for idx in range(_count):
                ele = q.get()
                if(ele.left):
                    q.put(ele.left)
                if(ele.right):
                    q.put(ele.right)
                _sum +=ele.val
        return _sum
