# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result=[]
        def helperInorder(root):
            if root is None:
                return
            helperInorder(root.left)
            result.append(root.val)
            helperInorder(root.right)
        helperInorder(root)
        for i in range(1,len(result)):
            if(result[i-1]>=result[i]):
                return False
        return True
        
